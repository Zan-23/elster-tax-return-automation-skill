#!/usr/bin/env python3
"""Estimate a German income tax refund for an employee.

Usage:
    python3 estimate_tax.py year-config.json case.json

year-config.json: a filled copy of assets/year-config.template.json (verified values only).
case.json example:
{
  "gross_wage": 0,                 # Lohnsteuerbescheinigung: Bruttoarbeitslohn
  "withheld_wage_tax": 0,          # Lohnsteuer
  "withheld_solidarity": 0,
  "withheld_church_tax": 0,
  "church_tax_rate": 0,            # e.g. state rate if liable, else 0
  "pension_employee": 0,           # employee share (Arbeitnehmeranteil RV)
  "pension_employer": 0,           # employer share (Arbeitgeberanteil RV)
  "health_basic": 0,               # employee health contributions
  "health_entitled_sick_pay": true,
  "care": 0,                       # long-term care contributions
  "other_insurance": 0,            # unemployment + other sonstige Vorsorge
  "work_expenses": {"Home office": 0, "...": 0},
  "special_expenses": {"Donations": 0},
  "tax_credits": {"Household services (35a)": 0},
  "scenarios": {"Name": {"work_expenses_delta": 0}}
}
No amounts are built in: everything comes from the two files.
"""
import json
import math
import sys


def val(cfg, key, sub="value"):
    node = cfg.get(key)
    v = node.get(sub) if isinstance(node, dict) else node
    if v is None:
        sys.exit(f"Missing verified value in year config: {key}.{sub}")
    return v


def tariff(zve, cfg):
    zones = cfg["tariff_zones"]["zones"]
    x = math.floor(zve)
    for z in zones:
        if z["up_to"] is not None and x > z["up_to"]:
            continue
        t = z["type"]
        if t == "zero":
            return 0.0
        if t == "quadratic":
            for k in ("base", "a", "b", "c"):
                if z.get(k) is None:
                    sys.exit(f"Tariff zone missing '{k}'")
            y = (x - z["base"]) / 10000
            return math.floor((z["a"] * y + z["b"]) * y + z["c"])
        if t == "linear":
            return math.floor(z["rate"] * x - z["minus"])
        sys.exit(f"Unknown tariff zone type: {t}")
    sys.exit("Taxable income above all tariff zones; check tariff_zones")


def solidarity(tax, cfg):
    s = cfg["solidarity"]
    if None in (s.get("rate"), s.get("free_limit"), s.get("mitigation_rate")):
        sys.exit("Missing verified solidarity values")
    if tax <= s["free_limit"]:
        return 0.0
    return round(min(tax * s["rate"], (tax - s["free_limit"]) * s["mitigation_rate"]), 2)


def marginal_rate(zve, cfg):
    return (tariff(zve, cfg) - tariff(zve - 100, cfg)) / 100


def assess(case, cfg, work_delta=0.0):
    work = sum(case.get("work_expenses", {}).values()) + work_delta
    work_ded = max(work, val(cfg, "employee_allowance"))
    special = sum(case.get("special_expenses", {}).values())
    special_ded = max(special, val(cfg, "special_expenses_allowance"))

    share = val(cfg, "pension_deduction_share")
    pension = max(0.0, share * (case["pension_employee"] + case["pension_employer"]) - case["pension_employer"])
    health = case["health_basic"] * (1 - (val(cfg, "health_sickpay_reduction") if case.get("health_entitled_sick_pay", True) else 0))
    basic = health + case["care"]
    cap = val(cfg, "other_insurance_cap_employee")
    other = min(case.get("other_insurance", 0), max(0.0, cap - basic))
    vorsorge = pension + basic + other

    zve = case["gross_wage"] - work_ded - vorsorge - special_ded
    tax = max(0.0, tariff(zve, cfg) - sum(case.get("tax_credits", {}).values()))
    soli = solidarity(tax, cfg)
    church = tax * case.get("church_tax_rate", 0)
    withheld = case["withheld_wage_tax"] + case.get("withheld_solidarity", 0) + case.get("withheld_church_tax", 0)
    return {
        "work_expenses_claimed": round(work, 2),
        "work_expenses_deducted": round(work_ded, 2),
        "above_flat_allowance": round(max(0.0, work - val(cfg, "employee_allowance")), 2),
        "vorsorge_deducted": round(vorsorge, 2),
        "special_expenses_deducted": round(special_ded, 2),
        "taxable_income": math.floor(zve),
        "income_tax": tax,
        "solidarity": soli,
        "church_tax": round(church, 2),
        "withheld_total": round(withheld, 2),
        "refund_(+)_or_payment_(-)": round(withheld - tax - soli - church, 2),
        "marginal_rate_income_tax": round(marginal_rate(zve, cfg), 4),
    }


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    cfg = json.load(open(sys.argv[1]))
    case = json.load(open(sys.argv[2]))
    out = {"base": assess(case, cfg)}
    for name, sc in case.get("scenarios", {}).items():
        out[name] = assess(case, cfg, sc.get("work_expenses_delta", 0))
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
