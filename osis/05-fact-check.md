# OSIS — Data Reconciliation & What To Fact-Check

*yfinance scrape (Nov 6 close) vs LSEG consensus/CF-export vs filings. Flags = where my scraped
numbers disagree with your terminal, so you can verify on TIKR/LSEG before we commit to a model.*

---

## Reconciliation table

| Metric | yfinance scrape | LSEG / filing (authoritative) | Verdict |
|---|---|---|---|
| Price (6 Nov) | $196.36 | $196.36 (TIKR) | ✅ match |
| Market cap | $3.09B | $3.09B | ✅ |
| EV | $3.84B | $3.84B (net debt $753M) | ✅ |
| Shares out | 15.7M | 15.73M (10-Q) | ✅ |
| **"Forward" P/E** | **15.3x** | **17.2x FY27 / 15.3x FY28** | ⚠️ **yfinance's 15.3x = FY28, not NTM. It's ~17x the current forward year.** Use 17x FY27. |
| NTM P/E (TIKR) | — | 16.7x | ✅ (blend of FY27/FY28) |
| **EV/EBITDA** | **14.4x (LTM)** | **12.6x FY27E / 12.2x NTM (TIKR)** | ⚠️ yfinance uses trailing EBITDA; forward is ~12.5x. Both "true," state which. |
| Rev growth | +4.9% | FY27E +3.9%–6.5% | ✅ consistent (definition of base differs) |
| EBITDA margin | 14.8% (LTM, yf) | 16.1% (LSEG) | ⚠️ yfinance LTM margin runs low vs LSEG standardized — definitional (yf includes more below-line). Use ~16%. |
| FY26 revenue | — | **$1,786M reported** vs **$1,832M LSEG consensus** | ⚠️ **~$46M gap** — see below |
| 52-wk low | $186.50 (yf) | $186.50 (TIKR) ✅ | ✅ |

---

## The three things to actually fact-check on your terminal

1. **The FY26 revenue gap ($1,786M reported vs $1,832M LSEG consensus, ~2.6%).**
   Company external revenue FY26 = $1,786M (sum of quarterly external rev in the CF-export, and
   matches the "$1.79B" on the Q4 call). But the LSEG consensus "Revenue" measure shows $1,832M for
   FY26. **Likely an intersegment/gross-vs-net definition difference** (the segment-collection
   revenue sums to ~$1,827M including a different elimination). *Check on TIKR which revenue
   definition the consensus uses* — it matters for whether "FY27E $1,903M" is +3.9% or +6.5%. I've
   used the company-reported base for growth math; confirm which base the Street quotes.

2. **The forward P/E framing.** Confirm NTM P/E on TIKR (should be ~16.7x). My point: **don't let
   the "15x" from the first pass stick** — that was FY28. The honest number is **~17x FY27**. Cheap
   vs its own 3-yr history (traded high-20s/30s) and vs the growth, but not screaming-cheap.

3. **Segment revenue consensus is thin (2 estimates, 1 for FY28).** The segment splits in
   `04-consensus-and-segments.md` are directional, not high-conviction. If TIKR shows more
   contributors or a different segment split, tell me.

---

## What I now HAVE (don't need to re-request)
- ✅ **Consolidated consensus rev/EPS/EBITDA-margin FY24–FY29** (LSEG estimate files).
- ✅ **Segment revenue consensus FY24–FY28** (LSEG segment estimate files).
- ✅ **Historical segment operating income/margin** (CF-export actuals → I compute margins myself).
- ✅ **Backlog** from filings/releases: ~$1.8B (Jun'25, 10-K) → ~$1.9B (Jun'26) → ~$2.1B (Sep'26).

## What I still WANT (nice-to-have, model-improving)
- **Service vs product revenue estimate** forward (if LSEG has it) — else I model it.
- **Consensus FCF + buyback pace** baked into EPS (to separate operational vs engineered EPS growth).
- **Peer NTM P/E & EV/EBITDA** for the comp set: Smiths Group/Smiths Detection, Leidos, Axon,
  Mesa Labs, and ITRI (your benchmark). I'll build the relative-value table once you pull them.
- **Quarterly backlog history** if TIKR has it as a line (to chart the coverage ratio = backlog ÷
  NTM revenue; currently ~$2.1B / ~$1.9B ≈ 1.1x — rising coverage = the bull tell).

---

## Bottom line on the data
Nothing in the terminal data **breaks** the thesis — it **sharpens** it:
- Consensus **confirms the shape**: FY27 reset (+4% rev, +10% EPS, flat ~16% EBITDA margin), then
  **FY28/29 acceleration** (+7%/+10% rev, +12%/+16% EPS). The whole trade is still "do you believe
  the FY28 acceleration, and will the April Q3 FY27 print de-risk it."
- The one correction: **it's ~17x FY27, not 15x.** Fair, not cheap-cheap. The asymmetry is the
  FY28/29 re-acceleration + the de-rate already taken, not a dirt-cheap current multiple.
