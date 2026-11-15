# WPM Valuation — Master Assumptions & Data Log
**Wheaton Precious Metals (WPM — NYSE/TSX/LSE)** · RSM332 Fall 2026 Valuation Project
_Last updated: 2026-11-15. All $ in US$000s unless noted. Single source of truth — everything saved here._

---

## 0. Locked modeling decisions (confirmed with user)
- **Method:** 10-yr explicit **FCFE** DCF (2027E–2036E) + terminal; discount in **USD**. Cost of equity via **CAPM**.
- **Primary = DCF.** P/OCF + streamer comps = sanity check. Framing: _DCF = intrinsic value at a disciplined discount rate; P/OCF = what the market pays a streamer at cycle peaks._
- **Production:** ramp per **contracted, funded** guidance to **1.2M GEO by 2030**, then **flat 1.2M GEO 2030–2036** (conservative plateau — no credit for Salobo IV / Kone expansions / new streams in base).
- **Beta = 1.2894** (Refinitiv `TR.WACCBeta`, 5-yr monthly, calc 2026-11-15). NOT TIKR's 1.28-rounded.
- **Base-case metal deck = spot held flat:** Au ~$3,900/oz, Ag ~$48/oz (near 52-wk lows → maximally conservative).
  - **Gold price = #1 sensitivity axis** (replaces generic growth ±30%).
  - **Silver** modeled separately (structural supply deficit = consensus upside lever).
  - **Bull case** = rising structural-floor gold thesis (central-bank marginal buyer).
  - **Mid/street reference:** Goldman (Nov 13) Au YE2026 $4,150 / YE2027 $4,800.
- **Tax:** use effective ~16% (conservative vs. ~6% cash).
- **Reinvestment:** base = contracted book only, minimal new-stream capex (internally consistent with mgmt's "1.2M needs no new capital"). Going-concern reinvestment (~$900M/yr) = sensitivity.
- **EPS: non-GAAP only.**

---

## 1. Market data (as of Nov 13–15, 2026)
| Item | Value | Source |
|---|---|---|
| WPM price | **US$131.45** (Nov 13 close) | TIKR |
| Diluted shares (WASO 9M) | **454,992k** (Q3 455,030k; basic o/s 454,189k) | Q3 FS |
| Market cap | ~US$59.8B | calc |
| Net debt | **US$1,451,716k** (bank debt 1,597,518 − cash 145,802) | Q3 FS |
| Enterprise value | ~US$61.3B | calc |
| **Beta (CAPM)** | **1.2894** (5-yr monthly) | Refinitiv TR.WACCBeta |
| Spot gold | **~$3,886/oz** (52-wk $3,857–$5,627) | Investing.com GCZ6 |
| Spot silver | **~$48.65/oz** (52-wk $48.05–$121.79) | Investing.com SIZ6 |
| Au:Ag ratio (spot) | **~80:1** ⚠ vs guidance 60:1 | calc |
| Street target | $172.12 (~+31%) | TIKR |
| Goldman gold deck (Nov 13) | YE26 $4,150; YE27 $4,800 (cut from 4,650/5,400) | Kitco |

**CAPM pencil:** Rf (10-yr UST, _confirm_) ~4.5–4.8% + β 1.2894 × ERP ~5% ≈ **~11% cost of equity.**

---

## 2. Income statement — 9M ended Sep 30, 2026 (Q3 in parens)
| Line | 9M 2026 | Q3 2026 | Note |
|---|---|---|---|
| Sales | 2,602,404 | 771,734 | Note 6 |
| Cost of sales ex-depletion (cash cost) | 349,423 | 105,337 | **13.4% of sales** |
| Depletion | 327,247 | 127,893 | non-cash |
| Gross margin (after depletion) | 1,925,734 | 538,504 | 74.0% |
| — cash gross margin | — | — | **86.6%** |
| G&A | 34,524 | 10,225 | tiny (47 employees) |
| SBC | 28,447 | 13,528 | mostly cash PSUs |
| Donations | 9,902 | 3,740 | |
| Earnings from operations | 1,852,861 | 511,011 | |
| Finance costs | 57,599 | 25,097 | |
| Pretax earnings | 1,823,830 | 487,675 | |
| Income tax | 288,302 | 77,427 | **15.8% effective** |
| **Net earnings** | **1,535,528** | **410,248** | |
| Diluted EPS | $3.375 | $0.902 | |

## 3. Revenue by metal — 9M 2026 ⚠ silver co-equal with gold
| Metal | 9M 2026 | % |
|---|---|---|
| Gold | 1,281,792 | 49% |
| Silver (credit + concentrate) | 1,263,267 | 49% |
| Palladium | 11,553 | 0% |
| Platinum | 81 | 0% |
| Cobalt | 45,711 | 2% |
| **Total** | **2,602,404** | 100% |
_Q3 split: 51% Au / 46% Ag / 3% other. **Model gold & silver as separate price×volume lines.**_

## 4. Cash flow — 9M 2026
| Line | 9M 2026 | Note |
|---|---|---|
| CFO | **2,060,196** | Q3 644,856 |
| Cash from ops before tax/interest | 2,204,759 | |
| Cash taxes paid | (109,515) | **~6.0% cash tax rate** (defers) |
| Stream deposits (investing) | (4,621,850) | incl **Antamina $4.3B** |
| Dividends paid | (258,965) | ~$345M annualized |
| Bank debt repaid / drawn | (1,100,000) / 2,700,000 | Antamina-funded |

## 5. Balance sheet — Sep 30, 2026
| Item | Value |
|---|---|
| Cash | 145,802 |
| Bank debt (non-current; revolver ~repaid, term loan left) | 1,597,518 |
| Total equity | 10,032,004 |
| Mineral stream interests (carrying) | 11,689,979 |
| Income taxes payable (cur + non-cur) | 501,415 |
| Deferred tax liability | 34,779 |

## 6. Portfolio & production
- 45 agreements (35 PMPAs + 3 early-deposit + 7 royalties); 57 mines; 19 countries; **22 operating, 20 development, 15 exploration.**
- Reserve life: **23 yrs reserves + 15 M&I + 23 resource = 60+ yrs.**
- **Production guidance (GEO, 60:1):** 2025A ~806k → 2026E **860–940k** (9M ~640k) → **2030E 1.2M** (contracted/funded, 50% growth, _no new capital / exploration / permitting required_) → **2031–2035 flat ~1.2M.**

---

## 6b. Physical volumes, realized prices, cash costs (MD&A, Q3 2026)
| Metal | Produced Q3 | Sold Q3 | Realized $/unit | Cash cost $/unit | Depletion $/unit |
|---|---|---|---|---|---|
| Gold (oz) | 91,753 | 91,969 | 4,273 | 549 | 523 |
| Silver (koz) | 8,182 | 5,758 | 62.13 | 8.83 | 12.63 |
| Palladium (oz) | 2,228 | 2,781 | 1,326 | 236 | 479 |
| Cobalt (klb) | 403 | 661 | 26.09 | 4.98 | 8.74 |
- Q3 blended: cash cost **$548/GEO**, cash operating margin **$3,466/GEO**. 9M: cash cost **$597/GEO**, margin $3,866/GEO.
- **9M physical:** gold produced 279,448 oz / sold 283,140 oz; silver produced 21,346k / sold 17,329k; GEO produced 647,258 / sold 583,129.
- **GEO price basis (guidance):** $4,800 Au / $80 Ag / $1,500 Pd / $2,000 Pt / $25 Co → **60:1 Au:Ag.**
- **2026 guidance decomposed:** **400–430k gold oz + 27–29M silver oz + 19–21k other GEO** = 860–940k GEO.
- Cash cost per oz is ~fixed/contractual (gold ~$550, silver ~$9) → margin expands with price (operating leverage); ~13% of revenue.
- San Dimas has variable Au:Ag exchange ratio (now 70:1). Cozamin silver entitlement rising 50%→65% until 500k oz delivered.

## 6c. ⚠ VALUATION RECONCILIATION — the key finding (preliminary back-of-envelope)
**Discount rate is the whole ballgame, even more than gold.** Steady-state (1.2M GEO ≈ 620k Au oz + 31M Ag oz) FCFE ≈ **net income + depletion ≈ $2.8B at spot $3,900 Au / $48 Ag.**

Approx. implied value/share (steady-state, silver held flat $48, ramp-adjusted):
| Gold (flat) | **CAPM ~11%** (β 1.2894) | **NAV convention 5%** |
|---|---|---|
| $3,900 (spot) | ~$50 | ~$112 |
| $4,800 (GS 2027) | ~$58 | ~$130 |
| $5,500 | ~$64 | ~$145 |
| $6,500 | ~$73 | ~$165 |
_Current price $131.45 · street target $172._

**Implications:**
- Under the rubric-mandated **CAPM (~11%, β=1.29), WPM screens OVERVALUED at any sane gold deck** — can't reach $131 until ~$11k gold. A literal CAPM DCF → **SELL/HOLD**.
- The market is implicitly using the **streaming-NAV ~5% discount rate** (Vincent Lau, Investor Day: "every single stream valued at a flat 5%"). At 5%, $131 prices in **~$4,800 gold flat**; street $172 ≈ ~$6,500 gold.
- Precious-metals streamers structurally trade **rich to CAPM-DCF** (beta doesn't capture the safe-haven/inflation-hedge/optionality premium). This is the P/OCF-multiple point from the thesis, restated in DCF terms.
- **Recommendation direction hinges on how we treat the discount rate** → user decision pending (see chat).

## 6d. LSEG consensus (Mean) — from Estimate Details files (US$M except per-share)
| Measure | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|
| Gold prod (koz) | 416 | 589 | 624 | 726 | 783 | 653¹ |
| Silver prod (koz) | 21,643 | 27,480 | 28,352 | 29,122 | 28,148 | 27,959 |
| Revenue | 2,173 | 3,562 | 3,796 | 4,294 | 4,284¹ | — |
| EBITDA | 1,810 | 2,987 | 3,179 | 3,482 | 3,536¹ | — |
| CFO | 1,749 | 2,872 | 3,220 | 3,281 | 3,234 | — |
| FCF | 1,049 | (164) | 2,905 | 3,093 | 3,134 | — |
| EPS non-GAAP ($) | 3.02 | 4.49 | 4.45 | 5.10 | 5.29¹ | — |
| DPS ($) | 0.66 | 0.84 | 0.82 | 0.92 | 2.04¹ | 2.34¹ |
| Capex / stream deposits | 1,341 | 4,910 | 859 | 359 | 233 | 46¹ |
| Net debt (− = net cash) | (1,146) | 752 | (1,103) | (3,292) | (7,175)¹ | — |
| Cash cost $/GEO | 492 | 545 | 625 | 637 | 698 | — |
_¹ thin coverage (1–2 analysts) — extend/hold flat ourselves beyond 2028. Consensus implies ~$4,000 Au / ~$45 Ag (≈ spot) → consensus ≈ our spot-flat base._
_Historical quarterly actuals (16 yrs) in `CF-Export-15-11-2026.xlsx`. Analyst ratings/targets over time in `RecommendationTP (2).xlsx`._

## 6e. DCF v0 result (consensus FCFE, 10-yr, flat $3.15B plateau 2030–36)
| Cost of equity | Fair value/share | vs $131.45 |
|---|---|---|
| **CAPM ~11%** (β 1.2894) | **~$62** | **−53% (SELL)** |
| Streaming-NAV ~5.5% | ~$130 | ~fair (HOLD) |
| 5.0% | ~$140 | +7% |
→ Market's implied cost of equity ≈ **5.5%** (NAV convention), not CAPM. **The discount-rate choice IS the recommendation.** Decision pending with user.

## 7. Still needed (next steps)
- [ ] **LSEG estimate files** (user committing to repo): street production / revenue / EBITDA / CFO / EPS(non-GAAP) / DPS, 2026E–2031E + 20-yr history → calibrate 2027–2030 ramp.
- [ ] **Physical gold oz & silver oz** production/sales (from MD&A `cr22955010`) → split price deck (critical given 80:1 spot vs 60:1 guidance).
- [ ] **Per-GEO cash cost + contractual escalators** (MD&A).
- [ ] **Rf:** current US 10-yr / 30-yr Treasury yield for CAPM.
- [ ] Streamer comps: FNV, RGLD, SAND, OR — NTM P/OCF, EV/EBITDA, P/E, P/NAV.

## 8. Reference docs (in `wpm-valuation/reference/`)
RSM332 project brief · Sample Submission (report + DCF) · WPM Q3-2026 financial statements · WPM MD&A (cr22955010) · Gold thesis parts 1 & 2.
