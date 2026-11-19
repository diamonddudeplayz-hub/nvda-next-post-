# Cheniere (NYSE: LNG) — DCF Model Assumptions & Build Notes

Date: Nov 19, 2026. Context: full valuation build for the Vertige equity research report, done cell-by-cell in the house workbook (`LNG_Quarterly_FS_Template vJM`). This captures every assumption, where each number comes from, *why* it's set the way it is, the valuation range it produces, and — most importantly — the honest tensions the model exposes. All figures tie to the live DCF tab unless marked otherwise.

---

## The one-line view

On a strict, standalone, conservative DCF — growth capex charged, 15% cash tax, economic (not book) CQP minority, fixed fee capped at the contract horizon — **Cheniere is worth ~$247, about 17% *below* spot ($296).** It is not cheap on the fundamentals. The market is already pricing the full ramp to 75 mtpa and most of the war-era margin premium. The honest conclusion is **"roughly fairly valued, modest upside in the blend, real edge in the catalyst path and the floor underneath"** — not a pound-the-table buy. That's a harder story to tell and a more defensible one to walk in with.

The whole bull/bear spread ($247 → $350) reduces to **two judgment calls**: (1) do you charge growth capex or add it back like the Street does (~$60/share swing), and (2) what EV/EBITDA multiple do you put on the comps (~$100/share swing across 10–12.5x). Name your two levers and you can defend any point on the field.

---

## Headline valuation range (all tied to the live engine)

| Level | The one lever that moves it | Target | vs spot $296 |
|---|---|---:|---:|
| **1. Conservative DCF** (live model) | fee capped '45 + growth capex charged + econ NCI | **$247** | −17% |
| **2. Base DCF** | let fixed fee escalate to 2050 (it's contracted) | **$258** | −13% |
| **3. Growth-adjusted DCF** | add back growth capex (Street's treatment) | **$319** | +8% |
| **4. EV/EBITDA comps** | 10× / 11× / 12.5× on 2027E EBITDA (~$8.8B) | **$250 / $293 / $358** | −16% / −1% / +21% |
| **Blended PT** | 50% growth-adj DCF + 50% comps | **~$305** | +3% |

Spot sits in the middle of every bar. That *is* the thesis.

**Analyst cross-check (Street $322–352):** TD Cowen $352 (50/50 10× EBITDA + DCF @8%), BMO $350 (50/50 DCF + SOTP), BofA $350 (split-rate DCF to 2060), Scotia $327 (12.5× 2028 EBITDA), Barclays $328, Morgan Stanley $322, Wolfe *downgrade* to Peer Perform ("fully valued"). The Street gets to $350 by (a) *not* charging growth capex and (b) blending in comps — exactly the two levers above. Wolfe's downgrade corroborates our conservative read.

---

## 1. WACC — 7.33% base (WACC tab)

| Input | Value | Source / reasoning |
|---|---:|---|
| Net debt | $21,875M | Bonds net of cash, Q3 2026 10-Q (not gross debt $23,931M, not Yahoo's lease-inclusive $27.7B) |
| Market cap | $60,543M | 204.2M diluted shares × ~$296 |
| Debt / Equity weight | 26.5% / 73.5% | from the above |
| Tax rate | 15% | blended long-run; below the 21% statutory because of NOLs / structure |
| **Beta** | **0.70** | see note below |
| Risk-free | 5.1% | 10Y UST ~5.07% (rates are high right now — do *not* use a stale 4.2%) |
| Equity risk premium | 5.0% | Kroll recommended US ERP (Damodaran's Nov-1 implied is 4.41%; we took the more conservative Kroll number) |
| Cost of equity | 8.6% | = 5.1% + 0.70 × 5.0% (CAPM) |
| Total debt / interest exp | $23,931M / $1,073M (TTM) | Q3 2026 filings |
| Cost of debt | 4.5% | = 1,073 / 23,931 |
| **WACC** | **7.33%** | = 0.735 × 8.6% + 0.265 × 4.5% × (1 − 0.15) |

**Beta — the one that needed real work.** LNG's *raw* market beta is near-zero (0.04 on 5Y monthly) because the stock has structurally decoupled from the index — a contracted toll-road cash flow that doesn't move with the market. That raw number is an artifact, not a risk measure. So:
- Unlevered the peer set (WMB, KMI, OKE, EPD, ET, TRGP) via Hamada (βu = βL / (1 + (1−t)·D/E)), re-levered to LNG's capital structure → **≈0.51**.
- Cross-check: LNG's own **2-year adjusted weekly beta = 0.476.** The two agree.
- We then bumped to **0.70** to price commodity and execution risk that CAPM misses given LNG's low realized correlation. This is the one deliberately subjective input, and it's conservative (pushes WACC up, value down).

**WACC cases:** Conservative 7.8% / Base 7.33% / Optimistic 6.6%.

---

## 2. DCF structure — full contracted life, no perpetuity

- **Forecast window: 2026–2060 explicit.** For a contracted LNG toll road you can *see* the cash flows out to the SPA expiries (~2045–2053), so we model them directly rather than guessing them through a short-forecast-plus-perpetuity. This is arguably *better* than the Street's 10yr + terminal.
- **Terminal value = 0.** Because the explicit window already spans the full economic/contract life, there is no growing perpetuity on top. Stacking a Gordon Growth perpetuity on 2060's (already escalated) ~$12B UFCF produced a nonsense $390–409 — *above every bull* — by assuming the toll road grows forever, past the point its contracts exist. Zeroing it is the honest call. Cross-checked three ways (35yr + zero TV; to-2045 + 8× exit; 10yr + GG(1%) + 8× blend) — all land ~$320 before the conservative levers.

### Line-item drivers (Base Case)

| Line | Formula / assumption | Rationale |
|---|---|---|
| **Volume (mtpa)** | 54 → 57 → 58 → 61 → 65 → 69 → 72 → 75, then flat | Maps to the actual train schedule: Stage 3 complete (~56 in operation), Midscale 8&9 online H2 2028 (+5), SPL Expansion ~2030, CCL Expansion later; capped at 75 |
| **Fixed Fee** | `6,600 × (vol/54) × 1.015^(year−2026)` | ~$6.6B contracted liquefaction fee in 2026 (FY2025 10-K); 1.5%/yr real escalator. *Conservative case caps the escalator at 2045* via `MIN(year,2045)` — stops assuming customers re-sign at ever-higher real fees after contracts roll off |
| **Marketed** | 4,950 / 4,400 / 4,050 (2026–28), then `2,800 × vol/61` | Spot + Cheniere Marketing margin; steps *down* as the war-era premium normalizes, then grows with volume at a normalized level |
| **COGS** | `vol × 12,000/54` | Feed gas, ~1:1 pass-through with variable revenue (115% Henry Hub washes against gas cost). Cancels in the margin — only Fixed + Marketed drives value |
| **Revenue** | Fixed + Marketed + COGS | Grossed up so Revenue − COGS = real margin |
| **SG&A** | `vol × 39 + 450 × 1.025^(year−2026)` | O&M (scales with volume) + fixed G&A (2.5%/yr inflation) |
| **D&A** | `vol × 1,500/54` | scales with asset base |
| **Taxes** | 15% of EBIT | *Heavier* than LNG's near-term cash tax (~3%, they barely pay cash tax due to NOLs) — deliberately conservative early, fair long-run |
| **Maint capex** | `vol × 500/54` | sustaining |
| **Growth capex** | 2,800 / 3,000 / 2,800 / 2,400 / 2,000 / 1,500 / 900 / 400 / 0 | SPL + CCL expansion build-out. **We charge this** (Street values distributable CF *before* it) |
| **Change in NWC** | −1% of revenue | **Real, verified drag.** 9M-2026 balance sheet shows operating NWC consumed ~$134M (receivables/inventory/margin deposits scale with volume). Not neutral — leaving it at 0 would be mildly *generous* |
| **UFCF** | EBIAT + D&A − CapEx + ΔNWC | Properly *unlevered* (NOPAT-based, no interest) → pairs with WACC |

### The enterprise → equity bridge

```
Sum PV of UFCF 2026–2060                          = Enterprise Value
  − Net debt (Q3-26 10-Q)                         − 21,875
  − CQP minority interest (MARKET, not book)      − 14,866
  = Implied equity value
  ÷ 204.2M diluted shares
  = Target price
```

**The CQP minority is the subtlety that matters most.** Our UFCF is 100% consolidated (it includes all of Sabine Pass), but the public owns **51.4% of CQP** (LNG owns 48.6% LP + 100% GP). So we must subtract what that public stake is *worth*, not its historical book cost. Book NCI on the balance sheet is only **$5,415M**; the economic value is **~$14,866M** (0.514 × 484.06M CQP units × $59.75, Nov-18 close — cross-checks to ~$1.1–1.2B of annual DCF-to-NCI at CQP's ~8% yield). Using book instead of market would flatter the target by **~$50/share.** This is exactly why the Street values LNG on a sum-of-the-parts.

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
2. **The conservative DCF says *rich*, not cheap.** $247 is −17%. That's the model being honest. The upside cases only exist if you relax the two levers (growth capex, multiple), both of which are legitimate but are *choices*, not facts.
3. **Margin durability is an assumption.** We hold marketed margin flat at a normalized level and escalate the fixed fee — both reasonable, both not guaranteed. The spot/marketing line is genuinely volatile and mean-reverts.
4. **The edge is catalysts + floor, not valuation.** The investable angle is the near-term catalyst path (SPL Expansion FID + term-loan close, possible S&P 500 inclusion, upward estimate revisions after the guidance raise, QatarEnergy/Petrobras SPA momentum) layered on a hard contracted-cash-flow floor — not a 30% discount to intrinsic value, because there isn't one.

---

## Appendix — primary sources

- **FY2025 10-K** (`26680655 (3).pdf`) — fixed liquefaction fees, capital structure, contract book
- **Q3 2026 press release / 10-Q** (Oct 29, 2026) — raised guidance (EBITDA $8.75–9.25B, DCF $6.05–6.55B, Consolidated DCF $7.2–7.6B), balance sheet for NWC and NCI, volume/train status, SPL/CCL expansion + QatarEnergy/Petrobras SPAs
- **LSEG** — peer betas, debt, market cap (WMB, KMI, OKE, EPD, ET, TRGP); LNG 2Y adjusted weekly beta 0.476
- **CQP market data** — 484.06M units (Q2-26 10-Q), $59.75/unit (Nov-18 close), ~$28.9B market cap
- **Kroll** US ERP 5.0%; **Damodaran** implied US ERP 4.41% (Nov 1, 2026); **US Treasury** 10Y 5.07% / 30Y 5.41%
- **Analyst notes** — TD Cowen, BMO, BofA, Scotiabank, Barclays, Morgan Stanley, Wolfe (all in repo)

### Model tabs
- **FS** — quarterly financial database, validated to foot and tie to filings (EBITDA, net income to Cheniere $5,330M FY25)
- **WACC** — 7.33% build (above)
- **DCF** — live engine, 2026–2060, producing the ladder above
- **Comps** — *still to build* (real peer EV/EBITDA for level 4; currently placeholder 11×)

### Open items
- [ ] Build Comps tab (peers, EV/EBITDA 10–12.5×) to replace the placeholder and lock the top of the range
- [ ] Wire the Conservative/Base/Optimistic CHOOSE switches for live case toggling
- [ ] Valuation Summary block (blended PT) on the DCF tab
- [ ] Report write-up / assumptions narrative
