# WPM — Filled RSM332 Template Model (`model/WPM_Template_Model.xlsx`)

_Built 2026-11-19. The prof's `RSM332 DCF Base Model - TO USE` skeleton, filled with WPM.
The "Sample Submission 2" is the SAME skeleton filled for Intuit (+Salesforce comp) with raw
Capital IQ dumps pasted in the back — not a second template. One template, we fill it._

## Data source
Historicals (IS / BS / Selected Other) = WPM LSEG export `CF-Export-19-11-2026.xlsx`, FY2021–2025, USD M.
Operating map ties to the dollar every year: Revenue − Cost of Operating Revenue − G&A = reported EBIT
(2025: 2,315 − 643 − 90 = 1,582 ✓); EBIT + D&A = reported EBITDA (1,582 + 305 = 1,887 ✓). BS Check = Ok! all years.

## Adaptations for a streamer (noted on the Cover)
1. **Revenue = GEOs sold × realised gold-equiv price** (not a blanket growth %). 3 cases = 3 gold decks:
   Base $4,700 / Bull $5,500 / Bear $3,400. GEO ramp ~681k→950k (base), per WPM guidance.
2. **Cost of sales held at FY25 ~28%** (contractual fixed cost), not the 5-yr avg (too low-margin).
3. **Forecast capex = committed stream installments** (~$384M→$179M declining), not the lumpy
   historical avg (~42% of rev = one-off acquisitions; would wrongly crush FCFE).
4. **Tax 15%**; WPM effectively debt-free (net cash −$1.15B).
5. **CAPM built in full** (WACC tab: Rf 4.5% + β1.29×MRP 5.5% = Ke 11.6%, WACC 11.4%), but base case
   applies **6.0%** — metal-price risk already sits in the scenarios; residual = IG/contractual credit risk.
   Street (CIBC, BMO) uses 5.0%. Reconciliation note is on both DCF tabs.

## Outputs (current price ~$117)
| Case (gold) | Applied 6.0% (FCFF / FCFE) | CAPM 11.6% (FCFF / FCFE) |
|---|---|---|
| **Base** $4,700 | **$150 / $139**  (+28% / +19%) | $89 / $84 |
| Bull $5,500 | $190 / $176 | $112 / $106 |
| Bear $3,400 | $96 / $88 | $57 / $54 |

Terminal value both ways on both tabs (Gordon g=2% + exit 18× EBITDA, 50/50), as the sample does.
Cross-checks our independent `WPM_DCF_Model.xlsx` (base ~$154, bull $190, bear $94, CAPM ~$72): consistent.
Validated by LibreOffice headless full recalc (live formulas, no hard-coded plugs; BS balances).
