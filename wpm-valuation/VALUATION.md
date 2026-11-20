# WPM Valuation — Discount Rate, DCF Results, Recommendation
_Supports ASSUMPTIONS.md. All figures preliminary pending final model build._

## 1. Cost of equity — the central judgment

### 1a. CAPM (computed as the rubric requires)
`Ke = Rf + β·ERP`
- Rf = US 10-yr Treasury ~4.3% (long-life asset → 30-yr ~5.2% alternative). **Confirm current from LSEG.**
- β = **1.2894** (Refinitiv `TR.WACCBeta`, 5-yr monthly, 2026-11-15).
- ERP = ~5.0% (Damodaran US).
- **Ke(CAPM) ≈ 10.7%–11.6% → use ~11%.**

### 1b. Why ~11% overstates the right discount rate for WPM's cash flows
We **use** CAPM but argue it is the wrong headline rate here, for three defensible reasons:

1. **The cash-flow stream is investment-grade-credit-like, not equity-like.** WPM has no mine operating costs, no cost inflation, no capex-overrun risk, no execution risk. It owns *contractual* delivery obligations: ~20%-of-spot (or fixed) purchase price locked at signing, **75% of production from investment-grade counterparties**, **90% with parent guarantees**, secured, 60+ yr reserve life. Conditional on a metal-price path, this stream carries risk comparable to an **IG corporate bond (~5.3–5.8% yield today)**. The equity's high β comes almost entirely from *metal-price* beta — which we capture **separately and explicitly** in the price deck + scenario analysis. Discounting price-scenario cash flows at the full equity β would conflate the two.
2. **Consistency with the comparable approach (rubric-required).** Precious-metals **P/NAV** multiples — the correct relative-value metric for a streamer, and the one we use — are built on sector NAVs discounted at **~5% real**. Discounting our DCF at 11% while benchmarking peers on a 5% basis would make the two halves of the valuation speak different languages. A ~5.5% DCF rate keeps them consistent.
3. **CAPM is a poor fit for gold-linked assets.** The trailing β is estimated over an anomalous 2021–26 gold regime (≈$1,800→$5,600→$3,900) and is empirically unstable/mean-reverting; gold's own market β is near-zero/negative (safe-haven). CAPM systematically misprices required returns for assets whose risk is "wrong-way" to the market.

**→ Base-case discount rate = ~5.5%** (≈ IG corporate yield; sector-standard streaming rate). Management's own NAVs use a flat 5% (Lau/Hodaly, Investor Day). **CAPM ~11% is carried as the downside/bear discount-rate sensitivity.**

## 2. Terminal value
- **Base:** g = 0 perpetuity on plateau FCFE (flat 1.2M GEO sustained). Justified: 60+ yr reserve life (23 P&P + 15 M&I + 23 resource) and ~$3B/yr CFO reinvested (~$900M–1B/yr into new streams historically) → steady-state replacement ≈ depletion.
- **Sensitivity (conservative):** finite-life ~25-yr runoff, FCFE −4%/yr, no new streams → base case ~$89 at 5.5%.

## 3. FCFE DCF results ($/share; consensus FCFE 2027–29 = 2,905 / 3,093 / 3,134, held flat 2030–36; 455m shares; price $131.45)
**Perpetuity (g=0) terminal:**
| Metal deck | 5.0% | **5.5% (base)** | 8.0% | 11.0% (CAPM) |
|---|---|---|---|---|
| Bear $3,200/$40 | 113 | 103 | 72 | 53 |
| Spot ~$4,000/$46 | 138 | **125** | 86 | 62 |
| Floor $4,800/$55 | 161 | **146** | 99 | 71 |
| Bull $5,500/$65 | 181 | 164 | 111 | 79 |

**Finite-life (25-yr runoff) terminal:** Spot/5.5% → ~$89; Floor/5.5% → ~$102; Bull/5.5% → ~$114.

## 4. Recommendation (preliminary) — BUY
- **Discount rate** 5.5% (streaming/IG-credit basis; CAPM 11% = bear sensitivity).
- **Base deck** = structural floor (gold ~$4,500–4,800, silver ~$52–55), argued as *normalized* vs today's financial-layer-depressed ~$3,886 spot (per our gold thesis). → **Target ~$146–150, ~+12–14%.**
- **Risk/reward framing (asymmetric):** at *trough spot held flat*, ~$125 (≈ fair → limited downside); at structural floor, $146–164 (+12–25%); bull $164–181.
- **Downside / bear:** financial-layer wins (gold → $3,200) OR market re-rates to a CAPM discount → $53–103. This is the key risk and must be shown.
- **Thesis (what the market is "missing"):** the market correctly prices WPM's bond-like contracted cash flows at ~5.5%; today's spot is below the central-bank-supported structural floor; +50% contracted GEO growth to 1.2M (funded, no new capital) and a structural silver deficit (silver = 49% of revenue) are underweighted. DCF primary; P/OCF (~19×) and P/NAV vs FNV/RGLD/SAND/OR as sanity check.

## 5. Open framing choices (confirm with user)
- [ ] Base metal deck: **spot-flat anchor + floor as thesis case** (asymmetric framing) vs **floor as the base case** (cleaner BUY). _Recommended: floor as base, spot-flat as the downside-protection case._
- [ ] Terminal: perpetuity (base) + finite-life (sensitivity). _Recommended as stated._
- [ ] Rf: confirm current US 10-yr (and 30-yr) from LSEG.

## Report framing — conservative base vs the street (added 2026-11-20)
**The pitch line (use in report + Q&A):**
> "Our base (~$140–145) is deliberately conservative — gold at $4,200, *below* the street's $4,500–5,200 decks. The banks sit at $188–215 (CIBC $215, Jefferies $188, BMO ~$193) precisely because they price the gold thesis I believe in. So I show that as **upside**, captured in my bull case ($5,000 gold), rather than baking it into the base."

**Why this works (the judgment the rubric rewards):**
- Separates *my view* (thesis = gold floor rising, central-bank bid) from a *conservative anchor* (base).
- Base says BUY even at a gold deck below the street → robust recommendation.
- Bull ($5,000 gold) + the banks' higher decks = quantified upside, not hand-waving.
- 2026 is ~75% booked (realized gold $4,527 / silver $72.90 YTD); only Q4 open, and with spot ~$3,532 the full-year blend lands ~$4,300 gold / $65 silver — so our 2026 ties to reported.

**Scenario decks (FY2027–2030):** Base gold $4,200 (silver ~$54) / Bull $5,000 ($69) / Bear $3,400 ($39). Silver derived from gold via 5yr β=1.63 (corr 0.79, computed from spot series). Street ref: CIBC $4,536/$5,200/$4,000LT; BMO $4,573/$5,038/$4,800LT.
