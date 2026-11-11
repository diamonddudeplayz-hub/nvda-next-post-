# OSIS — Operational Metrics Database (17 quarters, built from SEC filings)

*The Itron treatment. Every number below is pulled straight from OSI's SEC filings — the EDGAR XBRL
companyfacts feed (balance-sheet + expense tags) and the product/service split parsed off the face of
each 10-Q/10-K income statement (the `R4.htm` financial-report file). Nothing here is sell-side; these
are the operational ratios **no analyst note tracks** because you have to reconstruct them quarter-by-
quarter from primary docs. Period: Q1 FY23 (Sep-22) → Q1 FY27 (Sep-26). $ in millions unless noted.
Fiscal year ends June 30. Built 10 Nov 2026.*

> **Why this exists:** the thesis (doc 03) rests on claims — "service is a growing high-margin annuity,"
> "margins are a U-curve not a decline," "Mexico working-capital is unwinding," "inventory is being
> built to ship the 2H backlog," "it's a clean owner-operator with low dilution." Those are *testable*
> against the filings. This doc tests them. Where the data supports the thesis I say so; where it
> complicates it I say that too.

---

## The master table (raw, from filings)

Product/Service revenue + COGS are off the income-statement face (current-qtr and prior-year-qtr
columns across the trailing 10-Qs; Q4 = fiscal-year 10-K annual minus the three reported quarters).
Balance items are instants from companyfacts. Q4 SBC derived (annual − 9-mo).

| Qtr | Total rev | Product | Service | **Svc%** | Raw | WIP | FG | Contract liab (C+NC) | AR | R&D | SBC | Capex |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 FY23 | 268.1 | 197.0 | 71.1 | 26.5% | 225.6 | 72.0 | 64.3 | 70.8 | 313.5 | 14.5 | 7.2 | 3.3 |
| Q2 FY23 | 295.6 | 216.9 | 78.7 | 26.6% | 236.7 | 56.8 | 67.9 | 64.5 | 322.8 | 14.5 | 7.2 | 3.7 |
| Q3 FY23 | 302.9 | 223.7 | 79.2 | 26.1% | 233.5 | 63.2 | 75.2 | 66.4 | 300.7 | 14.9 | 7.1 | 5.7 |
| Q4 FY23 | 411.9 | 321.3 | 90.6 | 22.0% | 233.2 | 56.3 | 48.5 | 66.1 | 380.8 | 15.5 | 7.3* | 3.1 |
| Q1 FY24 | 279.2 | 199.7 | 79.5 | 28.5% | 271.4 | 83.0 | 64.4 | 58.7 | 323.8 | 15.9 | 7.1 | 5.2 |
| Q2 FY24 | 373.2 | 290.2 | 83.1 | 22.3% | 265.7 | 89.6 | 90.6 | 57.8 | 370.2 | 16.4 | 7.3 | 3.5 |
| Q3 FY24 | 405.4 | 327.4 | 78.0 | 19.3% | 257.8 | 88.3 | 96.6 | 69.2 | 503.8 | 17.1 | 7.1 | 4.9 |
| Q4 FY24 | 480.9 | 390.3 | 90.6 | 18.8% | 238.1 | 66.9 | 92.9 | 69.7 | 648.2 | 15.9 | 7.6* | 8.5 |
| Q1 FY25 | 344.0 | 255.8 | 88.2 | 25.6% | 242.7 | 86.4 | 126.9 | 80.6 | 687.6 | 17.8 | 6.4 | 7.7 |
| Q2 FY25 | 419.8 | 333.7 | 86.1 | 20.5% | 246.4 | 83.4 | 112.0 | 85.4 | 703.9 | 18.3 | 8.5 | 5.5 |
| Q3 FY25 | 444.4 | 341.2 | 103.2 | 23.2% | 243.1 | 99.8 | 96.0 | 94.1 | 672.2 | 18.6 | 7.6 | 4.5 |
| Q4 FY25 | 505.0 | 392.6 | 112.4 | 22.2% | 246.0 | 72.1 | 89.1 | 96.6 | 837.7 | 18.8 | 8.8* | 6.1 |
| Q1 FY26 | 384.6 | 275.8 | 108.8 | 28.3% | 259.8 | 95.3 | 98.9 | 93.8 | 828.2 | 20.4 | 6.2 | 7.0 |
| Q2 FY26 | 464.1 | 350.8 | 113.3 | 24.4% | 267.8 | 83.6 | 101.1 | 114.4 | 833.2 | 19.8 | 7.1 | 6.7 |
| Q3 FY26 | 453.2 | 344.9 | 108.3 | 23.9% | 260.7 | 107.3 | 67.2 | 108.7 | 870.5 | 19.5 | 6.6 | 7.6 |
| Q4 FY26 | 484.1 | 373.2 | 110.8 | 22.9% | 261.6 | 77.3 | 76.6 | 111.9 | 764.6 | 19.5 | 7.0* | 9.3 |
| **Q1 FY27** | **403.5** | **289.8** | **113.6** | **28.2%** | **297.7** | **86.9** | **78.8** | **110.2** | **746.9** | **19.4** | **6.0** | **7.7** |

*\*Q4 SBC derived (10-K annual − 9-mo YTD).* Totals tie to reported revenue to the dollar (e.g. FY26
service Q1–Q4 sums to $441.3M = reported $441M; Q1 FY27 289.8+113.6 = $403.5M).

---

## 1. Service gross margin vs product gross margin — the single most useful split [NOT in any note]
Parsed from the separate Product / Service COGS lines on the income-statement face:

| | Service GM | Product GM | Spread |
|---|---|---|---|
| FY23 avg | ~46.5% | ~29% | ~17pt |
| FY25 avg | ~44% | ~31% | ~13pt |
| **Q1 FY27** | **42.0%** | **26.2%** | **15.8pt** |

**Findings that matter:**
- **Service carries a ~16-point gross-margin premium over product, every single quarter** (service
  40–48%, product 26–35%). This is the *quantified* engine behind the whole "service-mix = margin"
  argument — and it's a hard number off the filings, not a mgmt adjective.
- **The recent blended-margin erosion is a PRODUCT-margin story, not a service one.** Product GM fell
  from a **35.4% peak (Q2 FY24) to 26.2% (Q1 FY27)** — ~9 points — as the mix went to lower-margin
  cargo/border scanners + Mexico + tariff drag. Service GM held in a 42–48% band the whole time. So
  "gross margin fell 36%→33%" (the bear line, doc 03) is **almost entirely product dilution**; the
  high-margin annuity underneath is intact. That's a *more* bullish read of the U-curve than the thesis
  doc gave it — the margin recovery just needs the product wave to stop diluting the mix.
- **Caveat (honest):** service GM is *not* monotonically rising — it dipped to 40–42% in FY24-25 when
  Mexico install/commissioning (lower-margin service) was heavy. Even "service" has mix inside it. So
  model service GM flat-to-slightly-up (~44%), not expanding.

## 2. Service share of revenue — the U-curve denominator effect, proven [NOT in any note]
TTM service as % of TTM total revenue:

| | Svc % of TTM rev |
|---|---|
| FY23 (TTM to Q4) | **25.0%** |
| FY24 (TTM to Q4) | **21.5%** ← trough |
| FY25 (TTM to Q4) | 22.8% |
| **Q1 FY27 (TTM)** | **24.7%** ← recovered |

**This is the mechanism, visible in the data:** during the FY24–25 Mexico **product** super-cycle,
service revenue *kept growing* (it never fell) but product grew so much faster that **service share
FELL from 25% → 21.5%.** Now that the product wave is maturing, service share is climbing back (24.7%
TTM, and 28.2% in the seasonally-light Q1 FY27 quarter). **This is the primary-source fingerprint of
exactly the U-curve doc 09 describes:** a product super-cycle *dilutes* the service mix on the way up,
then the installed base rolls into service on the way down. It's why "service only ~1pt/yr" understates
it — the gross service dollars compounded **+60% (Q1 FY23 $71M → Q1 FY27 $114M)**; the *share* was
masked by the product surge. Watch service share keep climbing through FY27-28 = the annuity thesis
confirming in the mix.

## 3. The Itron "unearned revenue" metric — contract liabilities [NOT in any note]
Contract liabilities (current + non-current) = customer cash collected / billed ahead of delivery.
This is OSI's version of Itron's deferred-revenue leading indicator.

- **Grew +56%: $66M (Q4 FY23) → $110M (Q1 FY27).** As % of TTM service revenue it rose from
  **~21% → ~25%.**
- **Read:** rising advance billings = customers funding orders ahead of shipment, consistent with a
  building book. It's a soft *corroborant* of the backlog/book-to-bill story from a different ledger line.
- **IMPORTANT caveat (why this is weaker for OSI than for Itron):** OSI's contract liabilities include
  **milestone/advance billings on big product (scanner) contracts**, not just prepaid service. So it is
  **not** a clean "unearned software/service" signal the way Itron's is — it's part product-milestone,
  part service-prepay. Treat the *trend* (steadily up) as mildly confirmatory, not as a pure recurring-
  revenue gauge. Don't over-read it.

## 4. DSO / the Mexico working-capital unwind — quantified [the "FCF > NI" engine]
Days sales outstanding (AR ÷ TTM revenue × 365):

| | AR | DSO (days) |
|---|---|---|
| Q1 FY23 (pre-Mexico) | $314M | ~90 |
| Q4 FY24 | $648M | 154 |
| **Q4 FY25 (peak)** | **$838M** | **178** |
| Q3 FY26 | $870M | 176 |
| **Q1 FY27** | **$747M** | **151** |

**Findings:**
- **DSO doubled (90 → 178 days) through the Mexico cycle** — the government-contract receivable balloon
  that is the *whole reason* OCF lagged net income in FY24-25. This is the balance-sheet cost of a
  government super-cycle, in hard numbers.
- **It's now unwinding: AR down $123M from the Q3 FY26 peak ($870M → $747M), DSO 176 → 151.** This is
  the **"FCF > net income" story made physical** — the cash is being collected. It directly supports
  the FY27 FCF ~$209M (Mexico collection) estimate in doc 02. **But 151 days is still very high** — OSI
  is structurally working-capital-intensive (a lumpy gov-hardware trait), so don't model it normalizing
  to a software-like level. The *direction* is the win; the *level* confirms the bear's "WC-heavy" point.

## 5. Inventory composition — the 2H-ship signal (extends doc 08)
Full series now available. The thesis read: **raw + WIP building while finished goods stays flat/low =
buying inputs to ship backlog, not piling unsold units.**
- **Q1 FY27: raw materials jumped to $297.7M (+$36M QoQ, a series high); WIP $86.9M; finished goods
  only $78.8M.** (raw+WIP)/FG ≈ **4.9x** — near the high end of the 17-qtr range (3.3–6.0x).
- The build is upstream (raw/WIP), not downstream (FG). **Consistent with "inventory built for 2H
  scheduled deliveries."** WATCH into Q2: raw/WIP keep building = ramp on track; finished goods
  ballooning = something isn't shipping. (Fuller discussion + table in doc 08.)

## 6. Quality screens — R&D, SBC, capex intensity [the "what kind of company is this" ratios]
| Metric | Level | Read |
|---|---|---|
| **R&D / revenue** | ~4–5% (steady; $14.5M→$19.4M/qtr) | Modest, stable. Not a heavy-R&D compounder; it's an integrator/manufacturer with a regulatory moat, not a tech-R&D moat. R&D dollars +34% over the period — growing with the business, not outrunning it. |
| **SBC / revenue** | **~1.5%, and FALLING (2.7% → 1.5%)** | **Genuinely low dilution — an owner-operator signal.** Most "quality compounders" run 4–10% SBC. OSI's ~1.5% means reported EPS isn't propped by stock comp, and buybacks actually shrink the count (16.9M → 15.7M). A real quality mark the screens miss. |
| **Capex / revenue** | ~1.5–2.0% ($3–9M/qtr) | **Asset-light for a hardware name** — OSI assembles/integrates more than it fabricates. Low capex intensity = FCF converts well *once* the working-capital swing normalizes. |

**Net quality read:** low SBC + low capex + real buyback = clean, cash-generative, shareholder-friendly
structure. The knock is **working-capital intensity** (sections 4 + the AR/inventory lines), not
dilution or capex. That's the correct, data-grounded version of "adequate, not a fortress."

---

## What the database CONFIRMS vs COMPLICATES (the honest scorecard)

**Confirms:**
1. **Service is a real ~16pt-higher-margin annuity** that compounded +60% in dollars (§1, §2).
2. **The margin "decline" is product-mix dilution, not a broken service annuity** — supports the
   U-curve, arguably more than doc 09 claimed (§1).
3. **The Mexico WC unwind is real and measurable** — AR down $123M, DSO 178→151, the engine of
   "FCF > NI" (§4).
4. **Clean owner-operator structure** — SBC ~1.5% and falling, capex ~2%, count actually shrinking (§6).
5. **Inventory is being built upstream to ship 2H backlog** (§5).

**Complicates / caps the bull:**
1. **Working capital is structurally heavy** — 151-day DSO even after the unwind; this is a
   cash-conversion drag that never fully goes away (§4).
2. **Contract liabilities are NOT a clean recurring-revenue signal** (product milestones mixed in) —
   don't over-weight the "unearned revenue rising" line the way you would for Itron (§3).
3. **Service share is still only ~25%** and service GM itself wobbles with install mix — the annuity is
   real but it's a *slow* mix-shift, not a step-change (§1, §2).
4. **R&D is modest** — this is a regulatory/position moat, not an innovation flywheel; don't pay a
   tech multiple for it (§6).

**Bottom line:** the primary-source operating data **supports the core thesis** — high-margin service
annuity intact, margin pressure is product-mix (recoverable), Mexico cash is physically unwinding,
clean capital structure — while **confirming the bear's working-capital and "slow mix-shift" points.**
Nothing here breaks the thesis; it sharpens it. The edge is the same as Itron: *these ratios aren't in
any note, and they line up with the "de-rated quality name with a real annuity underneath" read.*

---

*Sources: SEC EDGAR XBRL companyfacts (CIK 0001039065) for balance-sheet/expense tags; 10-Q/10-K
`R4.htm` income-statement financial reports (accession-level) for the product/service revenue + COGS
split. All figures recomputed from filings 10 Nov 2026; quarterly values for Q4 derived as annual minus
nine-month YTD. Cross-checked: segment-level revenue totals tie to reported consolidated revenue.*
