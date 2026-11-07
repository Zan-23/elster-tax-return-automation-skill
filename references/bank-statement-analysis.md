# Bank statement analysis

Ask for the tax year's bank exports (CSV preferred, PDF fine) from **every** account the user has, current and savings. Then base the estimate on what the transactions show, not on what the user remembers. Here they tend to differ: amounts are rounded, items turn out to be reimbursed, gifted or private, and interest gets forgotten.

## How to ask

- "Export CSV (or PDF) statements for 1 Jan – 31 Dec <year> from all your accounts, including savings vaults or sub-accounts."
- Say up front that you'll only use them for this return and won't save transaction details to memory, and that they can delete the files afterwards.
- Say they'll get a list of candidate deductions, each with a date and amount, to confirm before anything goes into ELSTER.

## What to look for

| Pattern in the statements | What it means | Action |
| --- | --- | --- |
| Incoming transfers from the employer other than salary (often with reference codes), matching an earlier purchase | Expense reimbursement | **Exclude** that cost. Match by amount and date (e.g. course, exam, train ticket) |
| Payments to the tax advisor | Exact fee and payment date | Use the exact amount. Deductibility follows the **payment year** |
| Direct debits to charities and associations | Exact donation or membership fee | Replace remembered amounts. Separate event fees and ticket payments, which aren't donations |
| Payments to a training provider, exam provider or course platform | Training costs | Claim only if not reimbursed |
| Software and AI tool subscriptions (IDE, assistants, cloud) | Possible work equipment | Ask about work use. Exclude streaming and other private subscriptions |
| Online-retail charges | Content unknown | Ask the user to check their order history for work items and keep the invoices |
| Charges at a client's canteen or near a client site | Evidence of client-site days | Note the dates as evidence for the meal allowance. They don't give an exact count |
| Train or flight tickets around colleague transfers that mention a city | Possible business trip | Ask whether it was work-related and how many days. Check whether it was reimbursed |
| Bike shop or car-sharing payments | Vehicle costs | Bike costs count only for the business-trip share. Car-sharing counts only for business trips |
| Gift transfers whose reference names an item (e.g. "birthday gift – backpack") | Item was a gift or is private | Challenge a claim for that item. If the user says it's a different item paid in cash, accept it and record a note |
| Savings vault or sub-account top-ups, especially at **foreign banks** (e.g. EU neobanks) | Interest that may not be taxed at source | Ask for the interest summary. Foreign interest goes in Anlage KAP (foreign capital income), with the saver's allowance already used noted |
| Employer-paid ticket shown as matching plus and minus lines on the payslip, or ticket purchases refunded by others | Ticket not the user's own cost | No ticket costs to claim |
| Cash payments the user mentions (no transaction) | No statement evidence | Allowed if real. Advise a short written note (item, date, price). Flag as the most likely point of query |

## Output to the user

1. **Corrections**: planned vs statement amount, with the change.
2. **Remove or confirm**: items contradicted by the evidence, with the reason.
3. **New findings**: reimbursed items to exclude, new candidate deductions, evidence for day counts.
4. **Tax-relevant income found**: interest, bonuses, other income.
5. **Updated refund estimate**, and the specific questions that would change it.

Only enter items the user confirms. Keep it short: list dates and amounts, not their private spending.
