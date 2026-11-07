# Year parameters: what to look up each time

This skill stores **no fixed amounts**. For the selected tax year, look up each parameter below in an official source (`official-sources.md`), write it into a copy of `assets/year-config.template.json` with its source URL, and use only those values.

If a value can't be verified, leave it `null`, say which estimate it blocks, and don't guess. Values from memory may be outdated.

## Search approach

1. Search the term below together with the tax year, e.g. "Arbeitnehmer-Pauschbetrag <year>". Restrict the search to official domains where the tool allows it.
2. Prefer the law text (gesetze-im-internet.de), then BMF letters, then ELSTER help and the official form instructions (Anleitung zur Einkommensteuererklärung, Anleitung zur Anlage N) for that year.
3. Watch for mid-year legislative changes. Check whether a value applies from 1 January of the year or only from a later date.

## Parameters

| Key in config | German term | Where it's defined |
| --- | --- | --- |
| `employee_allowance` | Arbeitnehmer-Pauschbetrag | § 9a EStG |
| `special_expenses_allowance` | Sonderausgaben-Pauschbetrag (single / joint) | § 10c EStG |
| `basic_allowance` | Grundfreibetrag | § 32a EStG |
| `tariff_zones` | Tariff formula (all zones and coefficients) | § 32a Abs. 1 EStG, version for the year |
| `solidarity_free_limit` | Freigrenze Solidaritätszuschlag | § 3 SolZG |
| `commute_rate_tiers` | Entfernungspauschale, per km and from which km | § 9 Abs. 1 Satz 3 Nr. 4 EStG |
| `commute_cap_non_car` | Höchstbetrag for non-car commuting | § 9 Abs. 1 Satz 3 Nr. 4 EStG |
| `home_office_day_rate`, `home_office_max_days` | Tagespauschale Homeoffice | § 4 Abs. 5 Satz 1 Nr. 6c EStG |
| `home_office_room_flat` | Jahrespauschale Arbeitszimmer (centre of activity only) | § 4 Abs. 5 Satz 1 Nr. 6b EStG |
| `meal_allowance_rates` | Verpflegungspauschalen (domestic): over 8 h, arrival/departure days, 24 h | § 9 Abs. 4a EStG |
| `meal_allowance_rule_days_per_week`, `meal_allowance_rule_months` | Dreimonatsfrist conditions | § 9 Abs. 4a Satz 6–7 EStG, BMF Reisekosten letter |
| `vehicle_km_rates` | Wegstreckenentschädigung for business trips: car, other motor vehicles | Bundesreisekostengesetz § 5, referenced by § 9 Abs. 1 Satz 3 Nr. 4a EStG |
| `telecom_flat_share`, `telecom_flat_cap_month` | Simplified work share of phone and internet | R 9.1 Abs. 5 LStR / Lohnsteuer-Handbuch |
| `account_fee_flat` | Kontoführungspauschale (administrative practice) | Official Anleitung or state tax office guidance |
| `gwg_limit` | Geringwertige Wirtschaftsgüter limit (net, and gross equivalent) | § 6 Abs. 2 EStG |
| `computer_useful_life` | Useful life for computer hardware and software | BMF letter on computer depreciation |
| `saver_allowance` | Sparer-Pauschbetrag | § 20 Abs. 9 EStG |
| `other_insurance_cap_employee` | Höchstbetrag sonstige Vorsorgeaufwendungen | § 10 Abs. 4 EStG |
| `health_sickpay_reduction` | Reduction of basic health insurance when entitled to sick pay | § 10 Abs. 1 Nr. 3 Buchst. a EStG |
| `pension_deduction_share` | Deductible share of pension contributions | § 10 Abs. 3 EStG |
| `donation_simple_proof_limit` | Vereinfachter Zuwendungsnachweis limit | § 50 EStDV |
| `reasonable_burden_rates` | Zumutbare Belastung (rates and income bands) | § 33 Abs. 3 EStG |
| `household_services_rate_caps` | Steuerermäßigung haushaltsnahe Dienstleistungen / Handwerkerleistungen | § 35a EStG |
| `filing_deadlines` | Abgabefristen: self-filed, with advisor, voluntary | § 149 AO, § 169–171 AO, current extension laws |
| `application_flat_rates` | Common flat rates for job applications (administrative practice, not law) | Mark as "not statutory" if you can only find secondary sources |

## Things that are structural, not numbers

These rarely change but still check them:
- whether the commute allowance offsets employer tax-free travel benefits (it does, via the Lohnsteuerbescheinigung line for tax-free employer travel benefits)
- whether the home-office day allowance and an Arbeitszimmer can be combined for the same days (they can't)
- whether tax-advice costs are deductible as work expenses (only the share for employment income)
