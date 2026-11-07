# Deduction rules and common traps

Amounts are referenced by their key in the year config (`year-parameters.md`). Check every rule against the official source for the year before relying on it.

## How deductions turn into a refund

- **Work expenses only help above `employee_allowance`.** The flat allowance is applied automatically. Below it, itemising changes nothing, so tell the user early whether they're likely to pass it.
- **Special expenses only help above `special_expenses_allowance`.**
- **Insurance contributions** are mostly prefilled from the Lohnsteuerbescheinigung. Other insurance is capped at `other_insurance_cap_employee`, which statutory health and care insurance usually exhaust already.
- **Household services and tradespeople** reduce the tax itself (`household_services_rate_caps`), not taxable income.
- **The refund equals withheld tax minus assessed tax.** Payroll already withholds as if the flat allowances apply, so the refund mostly comes from:
  - expenses above the allowances
  - partial-year employment (payroll annualises each month's pay)
  - tax-class effects
  - a small effect from salary changes during the year
- **Marginal effect:** the extra refund ≈ extra deduction × marginal tax rate (plus solidarity surcharge and church tax if they apply). Give this number to the user; it shows that buying things to deduct them never pays off.

## Commuting (Entfernungspauschale)

- Days actually spent at the regular workplace × one-way km × `commute_rate_tiers`. It covers **all** commuting costs: a bike, a car, repairs and tickets aren't added separately.
- Public transport: actual ticket costs can be used if they're higher than the allowance, but only costs the user bore.
- **Employer-paid or subsidised tickets** (tax-free, shown on the Lohnsteuerbescheinigung) are subtracted from the commute allowance, often down to zero. Enter the certificate value in the employer-benefits field; ELSTER usually prefills it.
- Don't count home-office days or business-travel days as commute days.

## Business travel (Auswärtstätigkeit)

- A **temporary** client or project site isn't the regular workplace. Trips there count as business travel, not commuting. The regular workplace is determined by the employer's assignment (or by the quantitative criteria in the law), so check § 9 Abs. 4 EStG.
- **Meal allowance:** `meal_allowance_rates` per qualifying day, only if no tax-free per diem was paid.
- **Three-month rule:** the meal allowance is limited to the first months at the same site only when the user is there on at least `meal_allowance_rule_days_per_week` days per week. If the pattern is near that threshold, show both scenarios and let the user decide from their calendar. Advise them to keep a day log.
- **Travel costs:** only what the user actually paid.
  - Own car or motorbike: `vehicle_km_rates` per km actually driven, both directions, or the actual costs.
  - Bike: no flat per-km rate, but actual costs (purchase, repairs) × the business share of total km may be claimed. The commute share stays excluded.
  - Employer-paid ticket used for the trip: nothing to claim.
- One-day events at other locations (conferences, workshops) also count, if they're work-related.

## Home office

- **Day allowance:** `home_office_day_rate` per day worked mainly at home without visiting the regular workplace, up to `home_office_max_days`.
- **Arbeitszimmer (room costs or the annual flat rate)** applies only if the room is the centre of all work. With a regular office and a home-office routine, that's usually not the case. Never claim both for the same days.
- Running costs of the flat (electricity, light bulbs, small repairs) are covered by the day allowance and aren't added on top.

## Work equipment (Arbeitsmittel)

- Deductible if used (almost) exclusively for work: desk, chair, lighting, monitor, headset, books, and a bag mainly used to carry work gear.
- Items above `gwg_limit` are depreciated over their useful life; computer hardware and software use `computer_useful_life`.
- Significant private use: claim only the work share, or nothing if work use is minor. State the assumption.
- Items reimbursed by the employer, or provided by them, don't count.

## Phone, internet, software

- Without itemised proof: `telecom_flat_share` of the combined bill, capped at `telecom_flat_cap_month` per month. The cap only matters if the bill is high enough; never set the claim to the cap regardless of the bill.
- A higher work share requires records for a representative period.
- Work-used subscriptions: claim the work share.

## Job search and training

- Job applications are deductible even while employed. Common flat amounts per application are administrative practice (`application_flat_rates`), so use actual costs if known. Interview travel counts as travel costs.
- Training and certifications count only if the user paid and wasn't reimbursed.

## Other work expenses

- Account fees: `account_fee_flat` is accepted without proof.
- **Tax-advice costs:** only the share for employment income or the work-expense part of the return counts. Advice on a home for own use or private matters doesn't. If the invoice is for "this tax return", the Finanzamt may accept most but not all of it.
- Union and professional association fees: check the current year's treatment (rules can change, e.g. allowing them on top of the flat allowance).
- Work clothing: only typical work clothing (uniforms, protective gear). Normal business attire never counts.

## Special expenses

- Donations and memberships to tax-privileged organisations count. Up to `donation_simple_proof_limit`, a bank statement suffices as proof. Some memberships (e.g. leisure clubs) are excluded, so check the organisation's confirmation.
- Contributions already on the certificate are prefilled; don't enter them twice.

## Household services and tradespeople

- Only **labour costs** for services or work done by third parties, with an invoice and paid by transfer. In rented flats, the labour items in the utility statement count, and each flatmate claims their own share.
- Doesn't count: materials, do-it-yourself work, cash payments.

## Extraordinary burdens (medical)

- Only the part above the user's own share (`reasonable_burden_rates`, based on income and family status) counts. Calculate that share first. For most employees, ordinary medical costs fall below it, so skipping the form is often correct.
- Non-prescription products and travel vaccinations generally don't count.

## Never claim

Gym or fitness memberships (unless medically prescribed, and then only as medical costs) · normal clothing · private travel · commute costs beyond the allowance · costs the employer paid or reimbursed · items already claimed in an earlier year.

## Capital income

- German institutions with withholding tax and an exemption order (Freistellungsauftrag) within `saver_allowance`: usually nothing to declare.
- Declare when:
  - income at foreign brokers or banks
  - exemption orders across banks exceed the allowance
  - unused allowance or losses to offset
  - a review of the tax rate (Günstigerprüfung) or church tax on capital income is wanted
  
  Foreign withholding tax goes in Anlage AUS.

## Why last year's refund may have been larger

- Partial-year employment: payroll taxed each month as if earned all year; if the real annual income was low, almost all wage tax came back, regardless of deductions.
- Deductions in a year with zero tax don't carry forward (except losses in specific cases, e.g. vocational training costs; refer to an advisor).

## Lessons from real cases

- **Employer reimbursements are common and easy to miss.** Courses, certification exams, train tickets and small purchases are often reimbursed by the employer. Match reimbursement transfers in the bank statements to purchases and exclude those costs.
- **Payment year counts.** Tax-advice fees and other expenses count in the year they were paid, even if the advice concerned an earlier year's return.
- **Gifts aren't expenses.** An item the user received as a gift, even one used for work, isn't their cost. If the evidence suggests a gift, ask before claiming.
- **Cash purchases** are deductible if real. Recommend a short written note with item, date and price, and point out that this is where the Finanzamt is most likely to ask for proof.
- **Distance to a client site** only matters through actual travel costs: car or motorbike km rates, or the actual-cost share of a bike. Employer-paid public transport gives nothing extra. The meal allowance is separate.
- **Foreign-bank interest** (e.g. savings vaults at EU neobanks) is usually taxed neither at source nor in Germany automatically. Always ask about it, and check whether the saver's allowance has already been used at German banks.
- **Refund expectations.** After a partial employment year, the next full year's refund is usually much smaller. Explain this with the user's own numbers.
