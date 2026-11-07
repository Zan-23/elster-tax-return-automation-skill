# German ELSTER Tax Return Skill

A [Claude](https://claude.com) skill that walks you through your German income tax return (*Einkommensteuererklärung*) in [Mein ELSTER](https://www.elster.de), from "where do I start?" to a checked, saved draft that you send yourself.

It's built for **employees** (income from a job, maybe some savings interest). It covers the basics of more complex cases and tells you when you need a Steuerberater.

## What it does

1. **Collects your information.** It reads your documents first (Lohnsteuerbescheinigung, last year's Bescheid, payslip, receipts) and then asks only about what's missing, a few questions at a time.
2. **Checks the rules for your tax year.** Allowances, rates and deadlines change every year. The skill looks them up in official sources (gesetze-im-internet.de, BMF, ELSTER) and cites them. It stores no fixed amounts.
3. **Finds every legitimate deduction.** Commuting, home office, work equipment, business trips, training, donations, household services and more. It also lists what *doesn't* count and why.
4. **Checks against your bank statements** (optional). It replaces remembered amounts with exact ones, removes costs your employer reimbursed, and finds forgotten income such as interest at foreign banks.
5. **Estimates your refund.** It shows the calculation, what-if scenarios for uncertain items, and how much each extra 100 € of expenses is worth.
6. **Maps everything to ELSTER.** You get a form-by-form list of what goes where.
7. **Prefills your ELSTER draft** (optional, needs [Claude in Chrome](https://claude.com/chrome)). You log in, Claude fills the forms, and you review and send.

## What it won't do

- **Log in or send for you.** You log in with your own certificate. Claude never clicks *Absenden*.
- **Type your tax ID or bank details.** ELSTER prefills these; you check them.
- **Inflate your claims.** Only real costs go in. In grey areas you see both options and choose.
- **Replace a tax advisor.** The result is an estimate, not tax advice. ELSTER's own calculation and your tax assessment (Steuerbescheid) are what count.

## Install

Copy this folder into your Claude skills directory:

```bash
git clone https://github.com/Zan-23/elster-tax-return-automation-skill.git \
  ~/.claude/skills/german-elster-tax-return
```

You can also zip the folder and upload it as a custom skill in the Claude app.

## How to use it

Just ask Claude, for example:

- "Help me do my 2025 German tax return in ELSTER."
- "Here's my Lohnsteuerbescheinigung. What can I deduct and how much will I get back?"
- "Here are my bank statements. Refine my return with exact numbers."
- "I'm logged in to ELSTER. Prefill the draft with what we planned."

**Good to have ready:**

- Lohnsteuerbescheinigung (one per employer)
- Last year's Steuerbescheid
- A recent payslip
- Receipts for work equipment, courses, donations
- Bank statements for the tax year (CSV or PDF, all accounts)

## What's inside

| File | Purpose |
| --- | --- |
| `SKILL.md` | Entry point: principles, workflow, safety rules |
| `references/required-information.md` | Intake checklist |
| `references/year-parameters.md` | Which values to look up for each tax year, and where they're defined |
| `references/official-sources.md` | Allowed sources and citation rules |
| `references/deduction-rules.md` | What counts, what doesn't, common traps |
| `references/bank-statement-analysis.md` | How to verify the estimate against bank exports |
| `references/elster-browser-workflow.md` | Step-by-step guide for prefilling Mein ELSTER |
| `references/output-template.md` | Structure of the final summary |
| `assets/year-config.template.json` | Template for the year's verified values and sources |
| `scripts/estimate_tax.py` | Refund calculator (no built-in amounts) |

### Running the estimate yourself

```bash
python3 scripts/estimate_tax.py year-config-2025.json case.json
```

- `year-config-2025.json` is a filled copy of `assets/year-config.template.json`.
- `case.json` holds your numbers; the script's docstring shows the format.
- The script stops if a value it needs is missing, so it never guesses.

## Privacy

Your tax files stay on your computer. The `.gitignore` excludes filled configs (`case*.json`, `year-config-*.json`) and PDFs so they don't end up in a repository by accident.

## Disclaimer

This is not tax advice. Rules change and every situation is different. Check the result against ELSTER's preliminary calculation, and see a Steuerberater or Lohnsteuerhilfeverein for complex cases.
