# Cheniere (NYSE: LNG) — DCF Model Assumptions & Build Notes

Date: Nov 19, 2026. Context: full valuation build for the Vertige equity research report, done cell-by-cell in the house workbook (`LNG_Quarterly_FS_Template vJM`). This captures every assumption, where each number comes from, *why* it's set the way it is, the valuation range it produces, and — most importantly — the honest tensions the model exposes. All figures tie to the live DCF tab unless marked otherwise.

---

## The one-line view

On a strict, standalone, conservative DCF — growth capex charged, 15% cash tax, economic (not book) CQP minority — **Cheniere's base case is ~$251 and the probability-weighted DCF ~$256, about 13–15% *below* spot ($295).** It is not cheap on the fundamentals. The market is already pricing the full ramp to 75 mtpa and most of the war-era margin premium. The honest conclusion is **"roughly fairly valued once comps are blended in, real edge in the catalyst path and the floor underneath"** — not a pound-the-table buy. That's a harder story to tell and a more defensible one to walk in with.

The whole bull/bear spread ($190 → $350) reduces to **two judgment calls**: (1) do you charge growth capex or add it back like the Street does (~$60/share swing), and (2) what EV/EBITDA multiple do you put on the comps (~$100/share swing across 10–12.5x). Name your two levers and you can defend any point on the field.

---

## Headline valuation range (all tied to the live engine)

The model runs a live **Bear / Base / Bull switch** (`DCF!D10 = 1/2/3`). The three cases move on three levers — beta (→WACC), the marketed-margin run-rate, and the fixed-fee escalation horizon — everything else held constant:

| Case | Beta / WACC | Marketed run-rate (at 75mt) | Fee escalates to | Target | vs spot $295 |
|---|---|---|---|---:|---:|
| **Bear** | 0.85 / 7.99% | ~$2,700 | 2045 | **$190** | −36% |
| **Base** | 0.70 / 7.44% | ~$3,440 | 2050 | **$251** | −15% |
| **Bull** | 0.50 / 6.71% | ~$4,180 | 2060 | **$332** | +13% |
| **Weighted** (25/50/25) | | | | **~$256** | −13% |

Spot ($295) sits **between base and bull** — the single most important read in the model: the market already prices the upside case (expansion past 75mt + margin durability). You only win if the bull plays out, and most of that is in the price. That *is* the thesis.

**+ Comps (last build piece):** EV/EBITDA 10× / 11× / 12.5× on 2027E EBITDA (~$8.8B) → **$250 / $293 / $358**; blend 50/50 with the DCF for the headline PT (~$300). The exit multiple lives here (on near-term EBITDA), *not* as a DCF terminal — terminal = 0 by design.

**Analyst cross-check (Street $322–352):** TD Cowen $352 (50/50 10× EBITDA + DCF @8%), BMO $350 (50/50 DCF + SOTP), BofA $350 (split-rate DCF to 2060), Scotia $327 (12.5× 2028 EBITDA), Barclays $328, Morgan Stanley $322, Wolfe *downgrade* to Peer Perform ("fully valued"). The Street gets to $350 by (a) *not* charging growth capex and (b) blending in comps — exactly the two levers above. Wolfe's downgrade corroborates our conservative read.

---

## 1. WACC — 7.44% base (WACC tab)

| Input | Value | Source / reasoning |
|---|---:|---|
| Net debt | $21,875M | Bonds net of cash, Q3 2026 10-Q (not gross debt $23,931M, not Yahoo's lease-inclusive $27.7B) |
| Market cap | $60,206M | 204.2M diluted shares × ~$295 |
| Debt / Equity weight | 26.7% / 73.3% | from the above |
| Tax rate | 15% | blended long-run; below the 21% statutory because of NOLs / structure |
| **Beta (base)** | **0.70** | β 0.85 / 0.70 / 0.50 across bear/base/bull — see note below |
| Risk-free | 4.95% | 10Y UST, Nov 2026 |
| Equity risk premium | 5.0% | Kroll recommended US ERP (Damodaran's Nov-1 implied is 4.41%; we took the more conservative Kroll number) |
| Cost of equity (base) | 8.45% | = 4.95% + 0.70 × 5.0% (CAPM) |
| Total debt / interest exp | $23,931M / $1,073M (TTM) | Q3 2026 filings |
| Cost of debt | 5.5% | current market yield on LNG's bonds — more conservative than the 4.5% booked average (1,073 / 23,931) |
| **WACC (base)** | **7.44%** | = 0.733 × 8.45% + 0.267 × 5.5% × (1 − 0.15) |

**Beta — the one that needed real work.** LNG's *raw* market beta is near-zero (0.04 on 5Y monthly) because the stock has structurally decoupled from the index — a contracted toll-road cash flow that doesn't move with the market. That raw number is an artifact, not a risk measure. So:
- Unlevered the peer set (WMB, KMI, OKE, EPD, ET, TRGP) via Hamada (βu = βL / (1 + (1−t)·D/E)), re-levered to LNG's capital structure → **≈0.51**.
- Cross-check: LNG's own **2-year adjusted weekly beta = 0.476.** The two agree.
- We then bumped to **0.70** (base) to price commodity and execution risk that CAPM misses given LNG's low realized correlation.

**The three scenarios are one lever — your view on beta. Everything else (Rf, ERP, cost of debt, capital structure) is held constant, so WACC moves only with beta:**

| Case | Beta | WACC | Rationale |
|---|---|---|---|
| **Bear** | 0.85 | 7.99% | +0.15 over base — prices a harder downside (spot margin compresses, execution slips) |
| **Base** | 0.70 | 7.44% | computed beta (~0.50) bumped for commodity/execution risk the realized beta misses |
| **Bull** | 0.50 | 6.71% | the *literal* computed beta (peer-relevered 0.51; LNG 2Y adjusted 0.476) — takes the market's low-correlation read at face value |

One-line defense: *"the cases are three beta views — 0.50 / 0.70 / 0.85; the bull accepts the market's computed beta, the base adds a conservative bump, the bear stresses it."*

---

## 2. DCF structure — full contracted life, no perpetuity

- **Forecast window: 2026–2060 explicit.** For a contracted LNG toll road you can *see* the cash flows out to the SPA expiries (~2045–2053), so we model them directly rather than guessing them through a short-forecast-plus-perpetuity. This is arguably *better* than the Street's 10yr + terminal.
- **Terminal value = 0.** Because the explicit window already spans the full economic/contract life, there is no growing perpetuity on top. Stacking a Gordon Growth perpetuity on 2060's (already escalated) ~$12B UFCF produced a nonsense $390–409 — *above every bull* — by assuming the toll road grows forever, past the point its contracts exist. Zeroing it is the honest call. Cross-checked three ways (35yr + zero TV; to-2045 + 8× exit; 10yr + GG(1%) + 8× blend) — all land ~$320 before the conservative levers.

### Line-item drivers (Base Case)

Several lines use `vol × [2026 $ anchor] / 54` — **54 is the 2026 base volume (mtpa)**, so the 2026 dollar figure scales *linearly with volume* (e.g. maintenance runs $500M at 54mt → $694M at 75mt). Anchors are pulled from the Q3-2026 actuals.

| Line | Formula / assumption | Rationale & source |
|---|---|---|
| **Volume (mtpa)** | 54 → 57 → 58 → 61 → 65 → 69 → 72 → 75, then flat | Train schedule: Stage 3 complete (~56 operating), Midscale 8&9 H2 2028 (+5), next expansion tranche ~2030-32; capped at 75 (no credit for 40mt+ permitting backlog). **Same across all cases** — scenarios flex margin and discount rate, not volume. |
| **Fixed Fee** | `6,600 × (vol/54) × 1.015^(MIN(year, cap)−2026)`, cap = **2045 / 2050 / 2060** (bear/base/bull) | ~$6.6B contracted take-or-pay fee in 2026 (FY2025 10-K). Escalates **1.5%/yr nominal** — blends the ~15–20% CPI-indexed portion of SPAs with re-contracting uplift; *below* ~2.5% inflation, so a slight real decline (conservative). Cap = how long capacity re-signs at rising fees after SPAs roll off. *Case lever 3.* |
| **Marketed** | 4,950 / 4,400 / 4,050 (2026–28), then `coef × vol/61`, coef = **2,200 / 2,800 / 3,400** (bear/base/bull) | Spot + Cheniere Marketing margin — *volatile, at-risk, 100% wholly-owned* (the fixed fee is contracted; this isn't). Bear = premium fully unwinds (~$2,700 at 75mt); base = mid-cycle (~$3,440); bull = stays elevated (~$4,180). **Biggest operating lever.** *Case lever 2.* |
| **COGS** | `vol × 12,000/54` | Feed-gas pass-through (115% Henry Hub washes against gas cost). **Nets to zero** — revenue is grossed up by it and EBIT nets it back out, so *no valuation impact*; only there to tie revenue to the reported figure. |
| **Revenue** | Fixed + Marketed + COGS | Grossed up; ties to the reported ~$23.7B as a sanity check. Only Fixed + Marketed drive value (COGS cancels). |
| **SG&A** | `vol × 39 + 450 × 1.025^(year−2026)` | O&M + fixed G&A. **×39** = O&M per mtpa (9M-26 O&M $1,598M → annualized ~$2,130M ÷ 54). **450** = fixed G&A (9M-26 SG&A $336M → ~$448M), +2.5%/yr inflation. Ties: 54×39+450 = $2,556M vs actual ~$2,578M. |
| **D&A** | `vol × 1,500/54` | **1,500** = FY26 D&A (9M-26 $1,146M → annualized ~$1,528M); scales per mtpa with the asset base. Non-cash, added back in UFCF. |
| **Taxes** | 15% of EBIT | *Heavier* than LNG's near-term cash tax (~3%, NOLs) — deliberately conservative early, fair long-run. |
| **Maint capex** | `vol × 500/54` (inside CapEx) | **$500M vs the ~$200M FY26 guide** — deliberately above guidance as a normalized sustaining level for an aging fleet over 35yr. A *conservative choice, not an actual* (lowers value); rises to $694M at 75mt. |
| **Growth capex** | 2,800 / 3,000 / 2,800 / 2,400 / 2,000 / 1,500 / 900 / 400 / 0 | Expansion build (Midscale 8&9 + next tranche). **We charge it in UFCF** (Street values CF *before* growth capex — ~$60/sh of the gap to Street). Total CapEx = maint + growth. |
| **Change in NWC** | −1% of revenue | **Operating WC only** (receivables/inventory/margin deposits/prepaid − AP/accruals/deferred rev; *excludes* cash & current debt → those sit in net debt). 9M-26 used **+$134M** (+$452M op assets − $318M op liabs; margin deposits +$118M are the swing). ~0.76% of rev; rounded to **1%** (~$235M, conservative). |
| **UFCF** | EBIAT + D&A − CapEx + ΔNWC | Properly *unlevered* (NOPAT-based, no interest) → pairs with WACC |

### The enterprise → equity bridge

```
Sum PV of UFCF 2026–2060                          = Enterprise Value
  − Net debt (Q3-26 10-Q)                         − 21,875
  − CQP minority interest (MARKET, not book)      − 14,082
  = Implied equity value
  ÷ 204.2M diluted shares
  = Target price
```

**The CQP minority is the subtlety that matters most.** Our UFCF is 100% consolidated (it includes all of Sabine Pass), but the public owns **51.4% of CQP** (LNG owns 48.6% LP + 100% GP). So we must subtract what that public stake is *worth*, not its historical book cost. Book NCI on the balance sheet is only **$5,415M**; the economic value is **~$14,082M** (0.514 × 484.06M CQP units × $56.60 — cross-checks to ~$1.1–1.2B of annual DCF-to-NCI at CQP's ~8% yield). Using book instead of market would flatter the target by **~$45/share.** This is exactly why the Street values LNG on a sum-of-the-parts.

Two notes on the NCI. **(1) Mark-to-market** — it moves with CQP's unit price, so re-check before use. **(2) Held fixed across bear/base/bull.** This is defensible because growth accrues overwhelmingly to parent LNG: Corpus Christi and Cheniere Marketing are 100% wholly-owned, and even the Sabine/SPL-expansion portion inside CQP flows **~74% to LNG** via its 100% ownership of CQP's GP and incentive distribution rights (NCI only ~26%, not a naïve 50%). The residual distortion is the NCI's ~51% share of the WACC/fixed-fee sensitivity on Sabine's *existing* contracted base — holding NCI fixed over-credits Cheniere in the bull / under-credits in the bear by **~$5–10/sh**, far-dated and heavily discounted. Accepted rather than re-marking CQP each case. *(SPL Expansion received its final FERC approval Nov 2026; if a future version includes it in the bull volume, split its value ~74/26 rather than 100% to LNG.)*

---

**Other bridge inputs.** *Net debt* $21,875M = bonds net of cash (Q3-26 10-Q), not gross ($23,931M) or lease-inclusive ($27.7B). *Shares* 204.2M diluted (Q3-26), **held flat** — no buyback accretion modeled despite ~$1.8B repurchased in 9M-26 (conservative; the Street credits it).

---

## 3. Sanity checks that tie to the Q3 2026 release

| Our 2026E | Model | Guidance (raised Oct 29) | Verdict |
|---|---:|---|---|
| EBITDA (EBIT 7,494 + D&A 1,500) | **8,994** | Consolidated Adj. EBITDA $8.75–9.25B | ✅ dead on |
| Revenue | **23,550** | 9M actual 17,773 → FY ~23.7 | ✅ |
| UFCF + growth capex add-back | 4,570 + 2,800 = **7,370** | Consolidated DCF $7.2–7.6B | ✅ reconciles |

**Do not get spooked by GAAP net income.** FY26 guidance is only $2.1–2.5B — because of **$3.6B of non-cash IPM derivative fair-value losses** in the 9M (disclosed). It's non-cash and reverses; the DCF correctly works off EBITDA/cash flow and ignores it.

One honest footnote on the reconciliation: UFCF + growth capex ≈ Consolidated DCF is *partly coincidental* — our heavier 15% cash tax (~$1.1B) roughly offsets the interest expense (~$1.0B) we correctly exclude. The UFCF line itself is cleanly unlevered.

---

## What cuts against the thesis (the honest part)

1. **The market already prices the ramp.** At spot, LNG is valued as if it reaches 75 mtpa with most of the current margin intact. We only "win" on volume *beyond* 75 (SPL/CCL expansions past current permits) — and that value accrues far out in time, heavily discounted. There's no cheap option on the base plan; it's in the price.
2. **The conservative DCF says *rich*, not cheap.** Base is −15%, bear −36%, weighted −13%. That's the model being honest. The upside cases only exist if you relax the levers (margin durability, lower WACC, growth-capex treatment, multiple), all legitimate but all *choices*, not facts.
3. **Margin durability is an assumption.** We hold marketed margin flat at a normalized level and escalate the fixed fee — both reasonable, both not guaranteed. The spot/marketing line is genuinely volatile and mean-reverts.
4. **The edge is catalysts + floor, not valuation.** The investable angle is the near-term catalyst path (SPL Expansion FID + term-loan close, possible S&P 500 inclusion, upward estimate revisions after the guidance raise, QatarEnergy/Petrobras SPA momentum) layered on a hard contracted-cash-flow floor — not a 30% discount to intrinsic value, because there isn't one.

---

## Appendix — primary sources

- **FY2025 10-K** (`26680655 (3).pdf`) — fixed liquefaction fees, capital structure, contract book
- **Q3 2026 press release / 10-Q** (Oct 29, 2026) — raised guidance (EBITDA $8.75–9.25B, DCF $6.05–6.55B, Consolidated DCF $7.2–7.6B), balance sheet for NWC and NCI, volume/train status, SPL/CCL expansion + QatarEnergy/Petrobras SPAs
- **LSEG** — peer betas, debt, market cap (WMB, KMI, OKE, EPD, ET, TRGP); LNG 2Y adjusted weekly beta 0.476
- **CQP market data** — 484.06M units (Q2-26 10-Q), $56.60/unit, ~$27.4B market cap (mark-to-market; re-check before use)
- **Kroll** US ERP 5.0%; **Damodaran** implied US ERP 4.41% (Nov 1, 2026); **US Treasury** 10Y 5.07% / 30Y 5.41%
- **Analyst notes** — TD Cowen, BMO, BofA, Scotiabank, Barclays, Morgan Stanley, Wolfe (all in repo)

### Model tabs
- **FS** — quarterly financial database, validated to foot and tie to filings (EBITDA, net income to Cheniere $5,330M FY25)
- **WACC** — 7.44% build (above), with β 0.85 / 0.70 / 0.50 driving the three cases
- **DCF** — live engine, 2026–2060, producing the ladder above
- **Comps** — *still to build* (real peer EV/EBITDA for level 4; currently placeholder 11×)

### Open items
- [x] Live Bear/Base/Bull switch wired (`DCF!D10`, driving WACC / marketed coef / fee cap via CHOOSE → cells R16–R18)
- [x] Every line-item assumption documented (this doc + cell comments on the DCF tab)
- [ ] Build Comps tab (peers, EV/EBITDA 10–12.5×) to replace the placeholder and lock the top of the range
- [ ] Valuation Summary block + weighted PT on the DCF tab
- [ ] Report write-up / assumptions narrative
