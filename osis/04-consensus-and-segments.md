# OSIS — LSEG Consensus & Segment Data

*Source: LSEG "Estimate Details" exports (8-Nov-2026, next report 27-Jan-2027) + LSEG Company
Fundamentals segment export (CF-Export-08-11-2026). All $M unless noted. Fiscal year = June.
These are the authoritative consensus numbers — they supersede the scraped/approx anchors in
`02-financials.md`.*

---

## Consolidated consensus (LSEG mean)

| Measure | FY24A | FY25A | FY26A | **FY27E** | **FY28E** | FY29E |
|---|---|---|---|---|---|---|
| **Revenue ($M)** | 1,524 | 1,705 | 1,832* | **1,903** | **2,043** | 2,238 |
| # est | 3 | 6 | 8 | 5 | 4 | 1 |
| **EPS ($)** | 8.09 | 9.31 | 10.42 | **11.45** | **12.82** | 14.86 |
| # est | 4 | 6 | 7 | 5 | 4 | 1 |
| **EBITDA margin (%)** | — | 16.9 | 16.1 | **16.1** | **16.6** | — |

\* LSEG's consensus "Revenue" for FY26 ($1,832M) runs ~$46M **above** the company's reported
external revenue of **$1,786M** (see `05-fact-check.md` — likely a segment/intersegment definition
difference). Growth math below uses the company-reported base where it matters.

**Revenue growth:** FY27E +3.9% (vs LSEG FY26) / +6.5% (vs reported $1,786M) → **brackets the guide
($1,875–1,930M = +5–8%)**. FY28E +7.4%, FY29E +9.5% → **consensus bakes in the FY28/29 acceleration.**

**EPS growth:** FY27E +9.9%, FY28E +12.0%, FY29E +15.9% → same shape: modest FY27 (reset), then
re-acceleration. FY27E $11.45 sits dead-center of guide ($11.28–11.64).

**EBITDA margin:** essentially **flat ~16.1% in FY27**, expanding to **16.6% in FY28** — this is the
quantified version of "FY27 is a margin-reset year, expansion comes FY28." High/low dispersion:
FY27 15.7%–16.5%, FY28 16.1%–17.1%.

---

## Valuation on consensus (price $196.36, EV $3,841M)

| | FY26A | FY27E | FY28E | FY29E |
|---|---|---|---|---|
| **P/E** | 18.9x | **17.2x** | **15.3x** | 13.2x |
| **EV/EBITDA** | 13.4x | **12.6x** | 11.3x | — |

**IMPORTANT correction vs the first pass:** the "~15x forward P/E" from the yfinance scrape was
actually ~**FY28** (Jun-28) EPS. On the **current forward year (FY27) it's ~17x**, FY28 ~15x,
FY29 ~13x. Still reasonable vs its own de-rated history and vs the growth, but **it is not a
"15x" stock on the next-twelve-months — it's ~17x FY27.** State it that way.

---

## Segment revenue consensus (LSEG mean, $M)
*Thinly covered — only 2 estimates per segment, 1 for FY28. Treat as directional.*

| Segment | FY24A | FY25A | FY26A | FY27E | FY28E | FY27 gro | FY28 gro |
|---|---|---|---|---|---|---|---|
| **Security** | 1,033 | 1,176 | 1,296 | **1,331** | **1,402** | +2.8% | +5.3% |
| **Optoelectronics** | 381 | 406 | 447 | **471** | **507** | +5.4% | +7.6% |
| **Healthcare** | 170 | 176 | 159 | **167** | **176** | +4.7% (recovery) | +5.4% |
| Intersegment elim | -61 | -61 | -75 | -72 | -75 | | |
| **Sum** | 1,523 | 1,698 | 1,827 | 1,898 | 2,010 | | |

Read-through: consensus has **Security growing slowest in FY27 (+2.8%)** — the Mexico roll-off +
Middle East drag — then **re-accelerating to +5.3% FY28** as CBP/BBB + RF convert. Opto is the
steady double-plus grower. Healthcare modeled to recover off the FY26 trough.

---

## Segment OPERATING MARGINS — I can build these (good news)
Darren's note said LSEG doesn't give segment op margin. **True for the *forecast* — but the CF
Company-Fundamentals export gives segment *operating income* actuals, so I can compute HISTORICAL
segment op margins directly.** Forward segment margins aren't in consensus, so I model those off
the historical trend + management commentary.

**Historical GAAP segment op margins (from CF-export actuals):**
- **Security:** FY26 **16.7%** GAAP ($208M op inc / $1,248M); Q1 FY27 **11.7%** GAAP (non-GAAP 12.6%
  per company — the gap is amortization of acquired intangibles, mostly the RF deal). Q1 is
  seasonally the weakest; Q4 FY26 Security was ~20.7% GAAP.
- **Optoelectronics:** Q1 FY27 **12.0%** (non-GAAP 12.1%) — steadily ~12–14%, trending up.
- **Healthcare:** Q1 FY27 **−2.5%** GAAP (non-GAAP −1.8%) — the loss-making drag; swings positive
  on volume (Q4 FY26 hit ~10%).

**For the SOTP I'll model forward segment margins as:** Security ramping from ~17% GAAP toward
high-teens as service mix builds (mgmt target: recurring 30%→40%+); Opto steady ~12–13%; Healthcare
recovering from loss toward mid-single-digit by FY28. These are MY assumptions, flagged as such —
not consensus.

---

## FCF & share-count consensus (LSEG, added 9 Nov)

| Measure | FY24A | FY25A | FY26A | FY27E | FY28E |
|---|---|---|---|---|---|
| **Free cash flow ($M, mean)** | 42 | 141 | 191 | **209** | **162** |
| FCF high/low | — | 107–166 | 127–242 | **147–289** | 93–235 |
| **Shares out (M, mean)** | 17.37 | 17.09 | 17.35 | **13.6**⚠️ | 16.65 |

- **FCF:** consensus **~$209M FY27** (Mexico collections inflate it — "FCF > net income" year), easing to
  ~$162M FY28. On ~$3.09B mcap that's a **~6.8% FY27 FCF yield**, ~5.2% FY28. TIKR's NTM levered FCF
  ($173M) = **5.6% yield**. Solid cash generation — this is the "paid to wait" cushion.
- **Share count ⚠️:** the FY27 mean (13.6M) is a **garbage data point** — low estimate 5.3M, huge
  predicted-surprise — one contributor is mis-modeling the convertibles. Reality: actual diluted shares
  are ~16.25M (Q1 FY27) and **falling via buyback** (was 17.5M a year ago). Use ~16M, declining ~2-3%/yr.
  Don't trust the 13.6M.

## What's still genuinely missing (can't get from these files)
1. **Forward segment operating margin consensus** — doesn't exist in LSEG (only segment revenue).
   I'll model it; just know those SOTP margins are my estimates, not the Street's.
2. **Service vs product revenue split forward** — not in these exports. I have actuals from the
   10-Q/transcripts (service ~28% of total, growing double-digit). If TIKR/LSEG has a "service
   revenue" estimate line, pull it; otherwise I model it.
3. **Backlog history** — not in LSEG estimates. It IS in the filings/releases (see `02-financials.md`
   and below). Quarterly: ~$1.8B (Jun'25) → ~$1.9B (Jun'26) → **~$2.1B (Sep'26)**.
4. **Consensus FCF / buyback pace** — not in these files. Would help separate operational vs
   financial-engineering EPS growth. Pull if LSEG has a cash-flow estimate tab.
