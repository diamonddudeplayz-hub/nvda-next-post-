# Discount Rate — CAPM Build & Reconciliation
*Why the base DCF discounts at 6%, and why that is conservative. The discount rate is the single largest value driver, so it is disclosed in full.*

## 1. The CAPM build (shown on the WACC tab)

| Input | Value | Source |
|---|---|---|
| Risk-free rate | 4.93% | Long-dated US Treasury |
| Equity risk premium | 5.00% | Standard |
| Beta (adjusted, Blume) | 1.17 | Raw 1.26 (Refinitiv, 5-yr monthly) → ⅔·1.26 + ⅓·1.0 |
| **CAPM cost of equity** | **10.78%** | Rf + β·ERP = 4.93% + 1.17×5.00% |
| WACC | 10.58% | ~3% target debt weight, after-tax Kd 4.25% |

We compute and present CAPM in full. We do **not** apply it as the base discount rate, for the reasons below.

## 2. Why not discount at CAPM 10.78%

**(a) It double-counts metal-price risk.** WPM's beta (1.17) is overwhelmingly a *gold-price* beta — precious-metals equities are volatile because the metal is volatile, not because the business is operationally risky. We already model that exact risk **explicitly and separately**: gold and silver are the #1 and #2 sensitivity axes, with full bull/base/bear decks and a price sensitivity table. Loading metal-price risk into the discount rate (via beta) **and** stressing the metal price in the scenarios charges shareholders for the same risk twice. The correct treatment for a scenario/decision-tree DCF is to discount each scenario's cash flows at a rate reflecting only the **residual** (non-price) risk — which for WPM is low.

**(b) WPM's residual risk is genuinely low.** Investment-grade rated; debt-light and de-levering to **net cash by 2028**; **no operating-cost or capex exposure** (streams are fixed-cost); revenue **diversified across ~40 assets and many operators**. There is little idiosyncratic risk left once the metal price is handled in the scenarios.

**(c) The company and the street value streams at ~5%.** WPM's own Investor Day values *"every single stream at a flat 5%,"* and sell-side NAV models for FNV / WPM / RGLD conventionally use **~5% real discount rates**. Precious-metals streamers structurally trade **rich to a CAPM-DCF** because beta does not capture their safe-haven / inflation-hedge / optionality premium.

## 3. Our choice: 6% — deliberately conservative

6% ≈ risk-free (4.93%) + ~1% residual-operational premium. Critically, it sits **above** the 5% that WPM and the street actually apply — we haircut the convention rather than adopt it. It sits below CAPM because CAPM double-counts price risk (§2a).

## 4. Full reconciliation (base case, $4,200 gold)

| Discount rate | Value / share | Interpretation |
|---|---|---|
| 5.00% | **$176** | WPM / street NAV convention — ≈ street price targets |
| **6.00%** | **$145** | **Base case — conservative vs. the 5% convention** |
| 7.00% | $126 | |
| 8.00% | $112 | ≈ current market price ($110) |
| 10.58% | $89 | CAPM WACC |
| 10.78% | $88 | CAPM cost of equity |

**Reads directly off this table:**
- At the street/company's own 5%, WPM is worth **$176** — in line with analyst targets ($172–215). We do not claim this; we note it bounds the upside.
- Our 6% base ($145) is **conservative relative to the people who own and cover the asset.**
- The market (~$110) is implicitly discounting $4,200 gold at **~8%**, or applying full CAPM to a *higher* gold deck — either way, pricing more risk than a net-cash, IG streamer warrants.
- At full CAPM (10.78%), the DCF is **$88 — essentially identical to the comparable-company result (~$87)**. That convergence is expected: both methods push metal-price risk into the multiple/rate and hold price at today's compressed spot, so both understate value if gold normalizes. They are the floor, not the fair value.

## 5. One-paragraph version for the report

> The discount rate is the valuation's largest single driver, so we disclose it in full. Our CAPM build yields a 10.78% cost of equity (β 1.17, Rf 4.93%, ERP 5.0%). We deliberately do **not** discount at that rate, because WPM's beta is almost entirely metal-price risk — which we already model explicitly through the gold and silver scenario decks and sensitivity tables. Discounting at CAPM *and* stressing the metal price double-counts the same risk. Reflecting only WPM's residual, non-price risk — investment-grade, de-levering to net cash by 2028, no operating-cost or capex exposure, diversified across ~40 assets — we discount at **6%**: risk-free plus a modest operational premium, and deliberately **above** the flat 5% that WPM's management and sell-side NAV models apply to the asset. At 6% the base case is **$145**; at the street's 5% it is $176, and at full CAPM it is $88 (which coincides with our comparable-company analysis). We adopt the conservative 6%.

---
*Prepared for RSM332 WPM valuation. The WACC tab shows the CAPM build; this note explains the applied-rate choice and reconciles across the full range.*
