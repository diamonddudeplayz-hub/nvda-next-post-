# Discount Rate — CAPM Build, Real-Rate Basis & Reconciliation
*The discount rate is the valuation's single largest driver, so it is disclosed in full. This note explains (i) how CAPM is used, (ii) why the model is in real dollars, (iii) why the base case discounts at 6% real, (iv) counterparty credit risk, and (v) the full reconciliation.*

## 1. How we use CAPM

We compute CAPM in full and present it on the WACC tab — it is a required deliverable. We use it as a **benchmark and transparency reference**, and we show what the DCF is worth *at* the CAPM rate (§6). We do **not** use it as the base-case discount rate, for the reasons in §2–§5. In one line: **CAPM is computed, shown, and reconciled — not discounted at.**

| CAPM input | Value | Source |
|---|---|---|
| Risk-free rate | 4.93% | Long-dated US Treasury |
| Equity risk premium | 5.00% | Standard |
| Beta (adjusted, Blume) | 1.17 | Raw 1.26 (Refinitiv, 5-yr monthly) → ⅔·1.26 + ⅓·1.0 |
| **CAPM cost of equity** | **10.78% (nominal)** | Rf + β·ERP = 4.93% + 1.17×5.00% |
| WACC | 10.58% (nominal) | ~3% target debt weight, after-tax Kd 4.25% |

## 2. The model is in constant (real) dollars

The forecast **holds metal prices flat** — gold $4,200, silver $53.9 from 2027 onward — and holds **costs fixed per GEO**; only **volume grows** (the funded production ramp, gold oz 378k → 570k). There is **no inflation escalation anywhere in the cash flows.**

Why this matters: the iron rule of DCF is that **the inflation assumption in the discount rate must match the inflation assumption in the cash flows.** A stream with no inflation baked in must be discounted at a **real (inflation-stripped) rate**, not a nominal one. Discounting flat-price cash flows at the full nominal CAPM (which embeds ~2.5% expected inflation) would strip out inflation that was never added to the numerator — understating value.

*(Nuance: flat **nominal** prices imply slowly **declining real** prices, so this setup is if anything more conservative than a textbook real model. Either way: no inflation in the cash flows → real discount rate.)*

→ This is exactly the street/NAV convention: **constant long-term price deck + ~5% real discount rate.** Our 6% is a real rate on a real model — same basis, slightly more conservative.

## 3. Why not discount at the full CAPM 10.78%

**(a) Real vs. nominal.** CAPM's 10.78% is nominal; its real equivalent is ≈ **8.3%** (−2.5% inflation). Comparing 10.78% nominal to a real-dollar DCF is apples-to-oranges.

**(b) It double-counts metal-price risk.** WPM's beta (1.17) is overwhelmingly a *gold-price* beta — precious-metals equities are volatile because the metal is. We already model that systematic risk **explicitly** via bull/base/bear gold & silver decks and sensitivity tables. Using the full beta **and** stressing the price charges the same systematic risk twice. Stripping the gold-price factor from beta leaves only WPM's **residual, non-gold systematic risk**, which is low.

**(c) Streaming/credit convention** (§4).

**Step-by-step reconciliation:**
`10.78% nominal` → (−2.5% inflation) → `~8.3% real` → (−gold-price systematic risk already in the scenarios, + streaming/credit convention) → **`~6% real`** → matches street 5% real (we sit just above = conservative).

## 4. Counterparty credit risk

Per WPM's Investor Day: the industry values *"every single stream at a flat 5%, irrespective of counterparty."* Two identical-cash-flow streams should **not** carry the same rate if one counterparty is riskier — e.g. +4% (→9%) turns a $100M stream value into $74M, a 26% credit haircut. Credit risk is real and belongs in the rate.

For WPM this cuts **in its favour**, because the producing base is **investment-grade-weighted**:

| Core producing stream | Operator | Credit |
|---|---|---|
| Salobo (largest single asset) | **Vale** | BBB (IG) |
| Antamina | **Glencore / BHP / Teck** | BBB–A (IG) |
| Peñasquito | **Newmont** | BBB+ (IG) |
| Voisey's Bay / Sudbury | **Vale** | BBB (IG) |
| Constancia | Hudbay | BB |
| Stillwater | Sibanye | BB |

The genuine credit risk sits in the **smaller development streams** (B2Gold/Goose, Artemis/Blackwater, Adventus/El Domo, Allied/Kurmuk) — but those ramp later and are **under-weighted in our conservative base** (we credit only funded/contracted production).

→ Our **6% = ~5% base + ~100bps blended credit/residual-systematic premium.** We are explicitly **not** naively flat-5%-ing — we haircut it, and that premium more than covers the minority of weaker counterparties given a book anchored by Vale, Newmont and Glencore.

## 5. Our choice: 6% real

6% real ≈ real risk-free + a modest premium for residual (non-gold) systematic risk and blended counterparty credit. It sits **above** the 5% real that WPM's management and sell-side NAV models apply (conservative), and **below** real-CAPM (~8.3%) because that double-counts the gold-price risk already in the scenarios.

## 6. Full reconciliation — base case ($4,200 flat gold)

| Discount rate | Value / share | Basis / meaning |
|---|---|---|
| 5.00% real | **$176** | WPM / street NAV convention — ≈ analyst price targets |
| **6.00% real** | **$145** | **Base case — conservative vs. the 5% convention** |
| 7.00% real | $126 | |
| 8.00% real | $112 | ≈ current market price ($110) |
| ~8.3% real | ~$108 | Real-equivalent of CAPM (10.78% nominal − 2.5% infl.) |
| 10.58% nominal | $89 | CAPM WACC (shown as nominal benchmark) |
| 10.78% nominal | $88 | CAPM cost of equity (shown as nominal benchmark) |

**Reads directly off this table:**
- At the street/company's own 5% real, WPM is worth **$176** — in line with analyst targets ($172–215). We do not claim this; it bounds the upside.
- Our 6% base ($145) is **conservative relative to the people who own and cover the asset.**
- At full CAPM (10.78% nominal), the DCF is **$88 — essentially identical to the comparable-company result (~$87)**. That convergence is expected: both bury metal-price risk in the rate/multiple and hold price at today's compressed spot, so both are a **floor**, not fair value.

## 7. Minor consistency note — terminal growth

Terminal growth is set at 2%. In a **real** model that is 2% *real* growth, which is slightly high for a depleting-resource streamer. Either restate as ~1% real, or justify the 2% as reserve-replacement + modest new-stream additions (the base case otherwise credits no new streams). Low valuation impact.

## 8. One-paragraph version for the report

> The discount rate is the valuation's largest single driver, so we disclose it in full. Our CAPM build yields a 10.78% **nominal** cost of equity (β 1.17, Rf 4.93%, ERP 5.0%), shown on the WACC tab and used as a benchmark. We do not discount the base case at that rate, for two reasons. First, the model is built in **constant (real) dollars** — metal prices held flat, costs fixed, only volume growing — so the correct discount rate is a **real** rate; the nominal CAPM embeds ~2.5% inflation the cash flows never contain. Second, WPM's beta is almost entirely **metal-price risk**, which we already model explicitly through the gold and silver scenario decks and sensitivity tables; discounting at the full beta *and* stressing price double-counts the same risk. Reflecting only WPM's residual, non-gold systematic risk and blended counterparty credit — a book anchored by investment-grade operators (Vale, Newmont, Glencore) — we discount at **6% real**: above the flat 5% real that WPM's management and sell-side NAV models apply to the asset, and conservative accordingly. At 6% the base case is **$145**; at the street's 5% it is $176, and at full CAPM it is $88 (which coincides with our comparable-company analysis and marks the floor). We adopt the conservative 6%.

---
*Prepared for RSM332 WPM valuation. The WACC tab shows the CAPM build; the DCF tabs carry a base-vs-CAPM reconciliation block; this note explains the applied-rate choice across the full range.*
