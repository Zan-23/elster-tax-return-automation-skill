# Intake checklist

Work through this before calculating. Each applicable item needs an explicit answer: a value, a date range, yes/no, "none", "not applicable", "already taxed", "reimbursed", or "unknown after checking the document". Never assume zero because something wasn't mentioned.

**Ask in small batches.** Before asking, check what the uploaded documents already answer. The "Source" column says where to look first.

## 0. Documents to request up front

| Document | What it answers |
| --- | --- |
| Lohnsteuerbescheinigung (one per employer) | Gross pay, wage tax, solidarity surcharge, church tax, tax class, social insurance, tax-free employer travel benefits, tax-free per diems |
| Last year's return or ELSTER transfer protocol, and the last Steuerbescheid | Tax number, what was claimed before, why last year's refund was what it was |
| One recent payslip (Entgeltbescheinigung) | Job ticket or travel subsidy, benefits in kind, insurance rates, vacation entitlement |
| Bank or broker tax certificates (Jahressteuerbescheinigung) | Capital income, withheld tax, used saver's allowance |
| Utility statement (Nebenkostenabrechnung) | Labour share of household services and tradespeople |
| Invoices and receipts | Equipment, training, donations, tax advice, repairs |
| Bank exports for the tax year (all accounts, savings included) | Exact amounts, employer reimbursements, forgotten interest, evidence of work days. See `bank-statement-analysis.md` |

If the user can log in to ELSTER, the certificates already held there can be read under *Bescheinigungen verwalten* (see `elster-browser-workflow.md`).

## 1. Scope and status

| Item | Source |
| --- | --- |
| Tax year | Ask |
| Estimate only, field mapping, or prefilled draft | Ask |
| Mandatory or voluntary filing, e.g. several employers at once, tax class combinations, wage-replacement benefits, other income above the official threshold | Ask, then verify triggers for the year |
| Marital status; joint or separate assessment | Ask |
| Children | Ask |
| Church tax liability | Lohnsteuerbescheinigung, ELSTER religion certificate |
| Address, and moves during the year | ELSTER master data, ask |
| Tax number (Steuernummer) and tax office | Last Bescheid |

## 2. Employment

For each employer:
- Employment period, and periods without pay
- Certificate values: gross pay, wage tax, solidarity surcharge, church tax
- Pension, health, care and unemployment insurance contributions
- Tax-free employer travel benefits (job ticket) and flat-taxed travel benefits
- Tax-free per diems and travel reimbursements
- Salary changes during the year (only to explain withholding effects)
- Whether the data already appears in ELSTER

## 3. Wage-replacement and progression-relevant benefits

Arbeitslosengeld, Krankengeld, Elterngeld, Kurzarbeitergeld, Insolvenzgeld and similar.

For each: the type, the period, and the amount from the certificate. These are tax-free but raise the rate on other income, and they usually make filing mandatory.

## 4. Other income (each: yes/no, then details)

| Income | Details to collect |
| --- | --- |
| Self-employment or business | Activity, receipts, expenses, profit, existing EÜR, advance payments. Usually advisor territory |
| Rental income | Property, rent, costs, interest, depreciation |
| Capital income | Each institution, German or foreign, whether tax was withheld, used saver's allowance, losses, and whether a review of withholding is wanted |
| Foreign income | Country, type, gross amount, foreign tax, treaty or exemption |
| Pensions | Type and certificate |
| Private sales, other income | Type, amount, dates |

## 5. Work-related expenses (Werbungskosten)

### 5.1 Workplace and commuting
- Regular workplace address (erste Tätigkeitsstätte) and home address
- Days actually spent there, one-way distance, means of transport
- Employer-paid ticket or subsidy

### 5.2 Business travel (Auswärtstätigkeit)
- Client sites or other locations outside the regular workplace: address, period, days per week
- Typical time away from home on those days: above or below the official threshold for a meal allowance
- Means of transport for each, and the user's own costs for it
- One-day events, trainings, offsites
- Employer reimbursements for meals or travel

### 5.3 Own vehicle used for business trips
- Car, motorbike or bike, used for business trips
- For actual-cost claims: purchase, repair and running costs in the year, and a rough split of km (business / commute / private)

### 5.4 Home office, by period
- Days worked mainly from home without visiting the regular workplace
- Whether another workplace was available
- A dedicated room that is the centre of all work? Only then do room costs apply: size, rent and utilities share

### 5.5 Work equipment
For each item: what it is, purchase date, gross price, work-use share, whether reimbursed, and whether already claimed in an earlier year.

### 5.6 Phone, internet, software
- Monthly phone and internet bills
- Work-used subscriptions or software, with the work share

### 5.7 Job search
- Number and type of applications (online or posted)
- Interview travel, platform fees

### 5.8 Training
- Courses and certifications paid by the user, and whether reimbursed

### 5.9 Other
Union and professional association fees, account fees, work-related moving, double household, typical work clothing, and tax-advice costs (and what they covered).

## 6. Special expenses and insurance
- Donations and memberships to tax-privileged organisations (with or without a confirmation)
- Church tax paid
- Insurance or pension contributions not already on the certificate: private health, Rürup, Riester, liability
- Tax-advice costs only if the current rules allow them in this category

## 7. Household services and tradespeople
- Labour cost in invoices paid by bank transfer: cleaning, garden, household help, repairs
- Labour items in the utility statement: caretaker, stair cleaning, chimney sweep, maintenance
- Do-it-yourself work and materials: not eligible, but record that they were asked about

## 8. Family and extraordinary burdens
Childcare, maintenance payments, disability, unreimbursed medical costs, care costs, funeral costs.

For medical costs, check against the user's own share (zumutbare Belastung) before collecting detail.

## 8b. Savings and interest
- Every account with interest, including savings vaults at foreign banks and neobanks, and the interest amount for the year
- Exemption orders (Freistellungsaufträge) and how much of the saver's allowance they used (bank certificate or the ELSTER certificate list)

## 9. Taxes already paid
Wage tax, solidarity surcharge and church tax withheld; capital gains tax withheld; advance income tax payments; foreign tax paid.

## Completion rule

The intake is complete only when every applicable section has an explicit answer. If one unresolved value blocks the estimate, name it and ask for it instead of guessing.
