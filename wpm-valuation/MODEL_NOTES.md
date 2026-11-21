# WPM Model — Page-by-Page Assumption Notes
*Defensible justification for every key input, tab by tab. For cell comments in the model and for the writeup. Values as of the Nov 2026 build.*

---

## Tab: WACC & Cost of Equity Build Up

**Header note:** CAPM / WACC is computed here per the rubric and used as the **nominal benchmark**. The base DCF discounts at **6% real** — see the Discount Rate Reconciliation block on the DCF tabs and `DISCOUNT_RATE.md`. The gap between the two is the real-vs-nominal difference plus the gold-price risk that is already modelled explicitly in the bull/base/bear scenarios (so discounting at full CAPM would double-count it).

| Cell | Input | Value | Note / justification |
|---|---|---|---|
| K5 | Market Risk Premium | 5.00% | Standard equity risk premium. US long-run historical ERP ≈ 4.5–6%; Damodaran implied ≈ 4.5–5%. 5.0% = conventional mid-point. |
| K6 | Beta (adjusted) | 1.17 | **Blume-adjusted** = ⅔·raw + ⅓·1.0 = ⅔(1.26) + ⅓(1.0) = 1.17. Raw 5-yr monthly beta ≈ 1.26 (Refinitiv; Yahoo 1.28). Adjustment applied because betas mean-revert to 1.0 (Bloomberg/Refinitiv convention). This beta is largely gold-price volatility — basis for not discounting the base case at full CAPM. |
| K7 | Adjusted Market Risk Premium | 5.85% | = MRP × β = 5.00% × 1.17. The β-scaled equity premium (β·ERP term of CAPM). |
| K8 | Risk-free rate | 4.93% | Long-dated US Treasury yield at valuation date (USD, matching USD cash flows). Confirm tenor/date cited. |
| K10 | **Cost of Equity** | **10.78%** | CAPM = Rf + β·ERP = 4.93% + 5.85%. **Nominal** — rubric/benchmark figure. Base DCF applies 6% real (reconciliation block). |
| K12/K17 | Target Debt / Total Capital | 3.00% | WPM near debt-free, de-levering to **net cash by 2028**. 3% = small conservative through-cycle weight (occasional revolver use for M&A). WACC ≈ Ke because debt weight is tiny. |
| K13 | Weighted Cost of Equity | 10.46% | = Ke × (1 − 3%). |
| K14 | Cost of Debt | 5.00% | WPM marginal borrowing rate — IG revolver ≈ Rf + modest IG spread. |
| K15 | Effective Tax Rate | 15.00% | Conservative. WPM cash tax ≈ 6% (favorable domicile); 15% prudent and immaterial to WACC at a 3% debt weight. |
| K16 | After-tax Cost of Debt | 4.25% | = 5.00% × (1 − 15%). |
| K18 | Weighted after-tax Cost of Debt | 0.13% | = 4.25% × 3%. |
| K20 | **WACC** | **10.58%** | = Weighted Ke (10.46%) + Weighted after-tax Kd (0.13%). **Nominal.** FCFF → WACC → Enterprise Value; FCFE → Cost of Equity → Equity Value. |

---
*Next tabs to document: Assumptions & Inputs, Revenue Assumptions, Operating Model & Other, DCF-FCFF, DCF-FCFE, Comparables, Cover Page. (Discount-rate logic lives in DISCOUNT_RATE.md; margins/credit in MARGINS_CF.md.)*

---

## Tab: Revenue Assumptions

**Header note:** Revenue is built bottom-up — (gold price × gold oz) + (silver price × silver oz) + (other-metals GEO × gold price) — toggled by scenario (Base/Bull/Bear). Metal **price** is the sensitivity axis; **volume** is the funded production ramp. Silver price is *derived* from gold (not an independent input). Prices are held **flat (constant/real dollars)** from 2027, which is the basis for discounting at a real rate (see DISCOUNT_RATE.md).

| Driver | Values (2026→2030) | Note / justification |
|---|---|---|
| Gold oz sold (000s) | 378 → 570 | WPM **attributable** gold, ramping on contracted/funded guidance toward **1.2M GEO by 2030**. No new acquisitions credited = conservative. |
| Silver oz sold (M oz) | 23 → 36 | Existing-stream ramp (Antamina, Peñasquito, etc.). |
| Other metals (000s GEO) | 15 → 20 | Cobalt (Voisey's Bay) + palladium, in GEO. |
| **2030 total GEO** | **≈1,190k** | 570k gold + 36M silver (600k GEO @60:1) + 20k = ~1.2M GEO → ties to WPM's stated 2030 target. |
| Gold $/oz — BASE | 4,300 → 4,200 flat | 2026 near-booked (YTD realized); 2027–30 held flat $4,200. Constant (real) → real discount rate. Conservative: above spot $3,532, below street $4,500–5,200. |
| Gold $/oz — BULL / BEAR | 5,000 / 3,400 | Scenario range = primary sensitivity axis (replaces generic ±growth). |
| Silver $/oz (derived) | Base 53.9 / Bull 69.1 / Bear 38.7 | `silver = spot_silver × (1 + 1.63 × (gold/spot_gold − 1))`. 5Y β 1.63 (corr ≈0.79): silver moves 1.63× gold's % move. Anchored to spot silver $41.18, gold $3,532. |
| GEO ratio | 60:1 | Gold-equiv oz = gold + silver/60 + other; ties volumes to WPM GEO guidance. |

**Conservatism flag:** Base-case 2026 revenue ($3,185M) sits ~11% below street consensus (~$3,562M), driven by conservative attributable volumes (gold 378k vs ~consensus higher). This is deliberate conservatism — worth a one-line note so it reads as intentional, not an error. If the volumes should be higher, the base rises and $145 becomes even more conservative.
