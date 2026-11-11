# Next position: search and first-pass diligence (11 Nov 2026)

Prices are the 10 Nov 2026 close. Working notes for Darren's own decision, not a post and not personal financial advice.

## 1. The answer

Nothing clears the bar the way Itron did, and I would not move the OSIS capital at full size into any of these today. The closest fit to the pattern is **Napco Security (NSSC, $31.34, $1.1B)**: recurring revenue at a 90% gross margin for twelve straight quarters, 52% of sales and up from 41.5% two years ago, net cash, falling share count, at a 52-week low after an 18% drop on 2 November, on 19.4x forward earnings against a ten-year median of 27.6x. The cheapest against its own history is **Trimble (TRMB, $54.75, $12.6B)** at 13.7x against a 20.1x median, the 2nd percentile of ten years, after a 17% drop on 4 November. Both are missing the thing that made Itron work, which was a recurring line that was accelerating while estimates were being beaten by 20%. Napco's recurring growth has slowed every year (26%, 14%, 13%, now 11.5%) and its last print was a miss. Trimble just cut its 2026 organic ARR growth outlook from 12-14% to about 10%. My probability-weighted values come out 8% above price for Napco and 11% for Trimble, against 6% for OSIS in the audit. That gap is inside the error of my own probabilities, so I'd call it about 60/40 that the right move now is no switch, with at most a starter (3-5% of the account) in Napco or Trimble if you want exposure before February. What would change my mind: Napco's fiscal Q2 on or about 1 February 2027 showing equipment revenue at or above $24.3M (flat year over year) with recurring growth still at or above 11%; or Trimble's February call guiding 2027 organic ARR growth at 10% or better with Q4 net new ARR at or above last year's. Either print failing would take the name off the list.

One uncomfortable finding: on the same reverse DCF, Itron is cheaper than every finalist (8.4% trailing free cash flow yield, priced for roughly zero growth). The screen did not find a better Itron. It found that Itron is still the cheapest one.

## 2. Comparison table

Tests: 1 service/recurring gross margin flat or rising 8+ quarters and 10+ points above product; 2 recurring share rising because recurring grew; 3 EPS beats in 3 of last 4; 4 forward P/E at or below own median and below market; 5 contracted or non-discretionary demand; 6 dated event inside 12 months; 7 not a trap; 8 $1-15B with thin coverage. P = pass, ~ = partial, F = fail, n/d = not disclosed.

| Name | 1 | 2 | 3 (last four beats, oldest first) | 4 | 5 | 6 | 7 | 8 | Fwd P/E vs 10-yr median | Implied 5-yr FCF growth (8.5% / 10%) | Weighted value vs price | Next dated event |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ITRI** (benchmark) | P: 43.9% to 53.2%, gap 15 pts | ~: 12.5% to 18.4%; service +43%, but product -9% and 2026 goodwill +$345M | P: +12%, +20%, +24%, +25% | P | P | P | P | P | 14.4x vs 20.0x (16th pct) | -3.5% / 1.8% | not re-derived here | Q4 and 2027 guide, Feb 2027 |
| **OSIS** (benchmark) | F: 47.6% to 42.9% | F: flat near 25% | ~: +2.4%, +2.3%, +0.1%, +0.8% | ~: at median | P | P | ~ | P | 17.2x vs 16.7x | 6.1% / 6.9% (at 8.8% / 9.0%, from audit) | $208.6 vs $197.00 (+6%) | Q2 FY27, 28 Jan 2027 |
| **NSSC** | P: 89.8% to 90.1%, gap 62-68 pts | P: 41.5% to 52.3%; recurring +51%, equipment -2% | ~: +19%, +15%, +32% (of which $0.09 tariff refund), then a miss | ~: below own median, about level with market | ~ | F | P | P | 19.4x vs 27.6x (14th pct) | 4.3% / 10.1% | $33.7 vs $31.34 (+8%) | FQ2, about 1 Feb 2027 |
| **TRMB** | P: 75.9% to 81.6% over 3 yrs, gap 30-35 pts | F: flat at 66% for two years, both lines +7% | ~: +4%, +10%, +7%, -0.2% | P | P | ~: dated, direction uncertain | P | F: 13 analysts | 13.7x vs 20.1x (2nd pct) | 1.3% / 6.9% (6.2% / 12.2% after SBC) | $60.7 vs $54.75 (+11%) | Q4 and 2027 guide, Feb 2027 |
| **ARLO** | ~: 76.7% to 81.0% over 2 yrs, but down from 84.5% a year ago | ~: 45% to 64%; services +55%, product -30%, two acquisitions in 2026 | P: +34%, +46%, +43%, +22% | F on GAAP; non-GAAP 11.1x | F | ~ | ~: shares 83M to 110M, FCF after SBC negative | P | 11.1x non-GAAP vs 16.7x (3 yrs only) | -0.5% / 5.0% on reported FCF; not solvable after SBC | $13.0 vs $12.32 (+6%) | Q4, late Feb 2027 |
| **DGII** | P: 78.3% to 80.8%, gap 23 pts | ~: 27% to 36%, mostly acquired (Jolt, Particle) | P: +10%, +2%, +7%, +13% | F | P | P | P | P | 20.8x vs 14.1x (6 yrs only) | 3.1% / 8.9% | $58.8 vs $65.05 (-10%) | FQ4 and FY27 guide, mid Nov 2026 |
| **VNT** | n/d | n/d | P: +1%, +0.3%, +11%, +9% | ~: below market, above own median | ~ | F | ~: reported sales -2% | ~ | 11.2x vs 10.3x (5 yrs only) | 1.8% / 7.5% | $42.4 vs $43.13 (-2%) | Q4, Feb 2027 |

Reference: S&P 500 trailing P/E 23.9x (SPY, Yahoo). I could not get a clean forward market multiple, so "below the market" is judged against that.

## 3. How the search ran

1. **Universe.** 880 tickers from the Yahoo screener across 27 industries plus a hand list; 519 are US-listed and between $1B and $15B (`nextpos_universe.py`).
2. **Yahoo cut.** Forward P/E under 21x, revenue not shrinking, positive trailing EPS, net debt under 3.2x EBITDA, three or more beats in four, gross margin over 28%: 119 names.
3. **Filing scan.** I parsed the latest 10-Q income statement of all 519 for a product and service split with separate costs (`nextpos_splitscan.py`). Only 36 report one. That is the real bottleneck for this pattern: most hardware companies do not disclose service margin at all.
4. **Twenty names tested on filings**, five kept:

| Cut | Why (latest quarter, year over year, from the 10-Q) |
|---|---|
| ALRM | SaaS share flat at 68.4%; SaaS gross margin fell 86.2% to 84.6%; 21x |
| MIR | Service margin up 48.9% to 56.0% but share fell 25.5% to 23.1%; 29x; net debt 3.5x |
| ADT | Service revenue -1.3%; share fell 84.6% to 80.3% |
| EXTR | Service share 37.5% to 36.0%; margin gap only 12 pts and flat |
| OMCL | Service margin 46.7% vs product 43.2%, gap under 10 pts; service growth 1.3% |
| DBD | Service margin 26.9%, 5 pts above product |
| NATL | Service margin 26.5% vs product 23%; net debt 2.5x |
| NTCT | Product margin (87.6%) is above service margin (74.0%) |
| BRKR | Gap 2 pts; 25x; net debt 2.9x |
| ZBRA | Service share fell 18.1% to 15.1%; service margin 46.3% vs product 45.6%; above $15B |
| VYX | Share rose only because product revenue fell 82%; net debt 3.7x |
| VMI | Service 11% of revenue and flat |
| AZTA | 59x; two beats in four |
| BMI | 31.6x; two beats in four; no split |
| MWA | No service line; revenue -1% |

Benchmarks reproduce: the parser returns Itron service margin 43.9% (Sep 2024) and 53.2% (Sep 2026), and OSIS 47.6% (Jun 2025 quarter) and 42.0% (Sep 2026), matching the audit.

## 4. One page per finalist

### Napco Security (NSSC), $31.34, $1.12B market cap, $0.99B EV

**What it does.** Makes alarm panels, locks and cellular alarm communicators sold through distributors to security dealers, then bills a monthly fee for each connected radio. The fee line ("recurring service revenue") is now larger than equipment.

**Reported evidence (10-Qs and 10-Ks, fiscal year ends June).**

| Quarter | Equipment $K | Recurring $K | Recurring share | Equipment GM | Recurring GM |
|---|---|---|---|---|---|
| Sep 2026 | 23,850 | 26,130 | 52.3% | 24.3% | 90.1% |
| Jun 2026 (FY less 9M) | 30,488 | 25,321 | 45.4% | 37.4% | 90.1% |
| Mar 2026 | 24,238 | 24,929 | 50.7% | 28.7% | 90.4% |
| Dec 2025 | 24,323 | 23,849 | 49.5% | 27.6% | 90.2% |
| Sep 2025 | 25,739 | 23,429 | 47.7% | 26.0% | 90.3% |
| Jun 2025 (FY less 9M) | 28,298 | 22,426 | 44.2% | 22.9% | 90.6% |
| Mar 2025 | 22,351 | 21,610 | 49.2% | 24.6% | 90.8% |
| Dec 2024 | 21,725 | 21,208 | 49.4% | 23.6% | 91.3% |
| Sep 2024 | 22,917 | 21,086 | 47.9% | 23.6% | 91.1% |
| Jun 2024 (FY less 9M) | 29,938 | 20,392 | 40.5% | 31.4% | 90.4% |
| Mar 2024 | 29,735 | 19,532 | 39.6% | 28.8% | 91.8% |
| Dec 2023 | 29,007 | 18,540 | 39.0% | 28.8% | 89.9% |
| Sep 2023 | 24,391 | 17,285 | 41.5% | 28.3% | 89.8% |

- Recurring revenue by fiscal year: $46.0M, $59.9M, $75.7M, $86.3M, $97.5M (FY22 to FY26). Growth 30%, 26%, 14%, 13%, then 11.5% in the September quarter. The line is growing and the growth rate has fallen every year.
- Like for like, September 2023 to September 2026: recurring +51%, equipment -2%. The share gain is the numerator.
- Fiscal Q1 FY27 (release, 2 Nov 2026): revenue $50.0M (+1.7%), equipment -7.3%, diluted EPS $0.36 against a consensus near $0.375. Yahoo records the actual as $0.34; I can't reconcile that and the release is the source. Operating income included a $1.0M litigation benefit (10-Q). Run rate of recurring revenue about $106M on October billings, up $3M from July.
- The fiscal Q4 FY26 "beat" ($0.50 against $0.38) included about $0.09 of tariff refunds (release, 24 Aug 2026). Excluding it the beat was about 8%.
- FY26: GAAP EPS $1.20, non-GAAP $1.60 after adding back $0.40 of litigation settlement. A $15M settlement payment took fiscal Q1 free cash flow to $2.3M from $11.4M.
- Balance sheet: $135M cash, $5M debt. Shares outstanding 35.77M, down from 37.1M diluted in FY24. Dividend $0.17 a quarter (2.2%).
- Insiders, last 12 months: 8 sales totalling $33.7M, no open-market purchases (Forms 4).

**Valuation.** 19.4x next-twelve-month EPS against a ten-year median of 27.6x (14th percentile); 19.9x trailing against 34.4x (2nd percentile). FY27 consensus EPS is $1.53, below FY26's $1.60, so the Street already has a down year. Reverse DCF on $50M trailing free cash flow: 4.3% growth for five years at an 8.5% discount rate, 10.1% at 10%. No transaction multiple found on the same denominator. If the multiple never changes and FY28 consensus of $1.76 is met, the price a year out is about $36 (+15%) plus the dividend.

| Scenario | Prob. | Assumption | Price |
|---|---|---|---|
| Deep bear | 15% | Equipment keeps falling 10%, recurring growth slows to 7%; FY27 EPS $1.35, 16x | $21.6 |
| Bear | 25% | FY27 EPS $1.45, FY28 $1.55, 18x | $28 |
| Base | 40% | Consensus met ($1.53, $1.76), 20x FY28 | $35 |
| Bull | 20% | Equipment recovers, recurring 12%+, FY28 $1.90, 25x | $47.5 |
| **Weighted** | | | **$33.7 (+8%)** |

**Bear case at full strength.** Recurring growth has halved in three years and every new radio comes from an equipment sale, so a falling equipment line is next year's recurring growth problem. Management's explanation for the September quarter is that two locking distributors cut inventory while sell-through grew; that is management's claim and nothing in the filings lets me check it. The same company restated fiscal 2023 quarters and has just paid to settle the resulting class action. Insiders sold $33.7M in a year and bought nothing. The stock de-rated from 33x to 19x while recurring revenue kept growing, which is what a market does when it stops believing the growth rate. And the monthly fees are not contracted backlog: they are sticky because fire monitoring is required by code, but a dealer can swap the radio.

**Symmetry check.** If equipment had grown 7% instead of falling 7%, would I like this less? No, I'd like it more. So the equipment decline is evidence against, and I'm counting it that way.

**Catalyst and the number to watch.** Fiscal Q2 results, about 1 February 2027 (Yahoo calendar; the company has not confirmed). Confirms: equipment revenue at or above $24.3M and recurring growth at or above 11%. Breaks: equipment below $22M for a second down quarter, or recurring growth below 9%.

### Trimble (TRMB), $54.75, $12.55B market cap, $13.9B EV

**What it does.** Positioning hardware and software for construction, surveying and trucking. About two thirds of revenue is now subscription and services, and it reports $2.56B of annualized recurring revenue.

**Reported evidence.**

| Quarter | Product $M | Subscription and services $M | Share | Product GM | Service GM |
|---|---|---|---|---|---|
| Oct 2026 | 324.3 | 642.5 | 66.5% | 46.8% | 81.6% |
| Jul 2026 | 331.4 | 640.6 | 65.9% | 51.7% | 81.3% |
| Apr 2026 | 311.2 | 628.7 | 66.9% | 49.2% | 81.0% |
| Jan 2026 (FY less 9M) | 268.3 | 701.5 | 72.3% | 48.0% | 83.5% |
| Oct 2025 | 302.5 | 598.7 | 66.4% | 50.8% | 80.8% |
| Jul 2025 | 292.8 | 582.9 | 66.6% | 50.7% | 79.9% |
| Apr 2025 | 271.6 | 569.0 | 67.7% | 47.1% | 79.0% |
| Jan 2025 (FY less 9M) | 288.9 | 694.5 | 70.6% | 46.8% | 81.3% |
| Sep 2024 | 307.6 | 568.2 | 64.9% | 47.8% | 78.8% |
| Sep 2023 | 444.0 | 513.3 | 53.6% | 51.4% | 75.9% |

- Service margin has risen about two points a year for three years. That test passes cleanly.
- The mix shift from 54% to 66% happened in 2024 and came mostly from selling hardware businesses (product revenue fell from $1.77B in 2023 to $1.14B in 2025). For the last two years the share has been flat because both lines grow about 7%. I'm scoring test 2 as a fail for that reason.
- Q3 2026 (release, 4 Nov 2026): revenue $966.8M (+7% organic), ARR $2.56B (+11%, +10% organic), non-GAAP EPS $0.86 against a consensus of $0.861. Full-year EPS guide $3.63-3.69.
- The same day it cut the 2026 organic ARR growth outlook to about 10% from 12-14%, citing its field systems and transportation businesses (press coverage of the call; I could not open the transcript). The stock fell 17.3%, from $65.61 to $54.25, on 2.5 times normal volume.
- $562M goodwill impairment in transportation and logistics in Q2 2026 (10-Q), which is why 2026 GAAP EPS is guided to a loss.
- Buybacks: 8.7M shares for $548.6M in three quarters at an average of $63.40; $768M of authorization left. Diluted shares 254M (2021) to about 232M.
- Net debt about $1.3B, roughly 1.5x EBITDA (Yahoo).
- Insiders: 15 sales, $5.3M, no purchases.

**Valuation.** 13.7x forward against a ten-year median of 20.1x and a 10th percentile of 16.9x. It has not been this cheap on this measure in the ten years I rebuilt. Trailing 15.2x against 22.4x. Reverse DCF on $798M trailing free cash flow: 1.3% growth at 8.5%, 6.9% at 10%. Stock compensation is $154M a year; after it the figures are 6.2% and 12.2%. Trailing free cash flow is more than double fiscal 2025's $361M, so I'd treat the lower pair as flattering until the 10-K shows a clean year. Transaction reference: Nemetschek's purchase of HCSS from Thoma Bravo was reported at more than 28x 2025 EBITDA. Trimble is at roughly 12x my estimate of 2026 adjusted EBITDA (about $1.14B, inferred from guidance and the Q3 margin). HCSS is pure construction software and Trimble is not, so that is a ceiling for one segment and not a comparable for the whole. If the multiple never changes and EPS grows 10% in 2028, the price in early 2028 is about $60.5 (+10%).

| Scenario | Prob. | Assumption | Price |
|---|---|---|---|
| Deep bear | 15% | ARR growth slides to 6-7%, hardware turns down; 2027 EPS $3.60 against $4.03 consensus, 11x | $40 |
| Bear | 25% | 2027 EPS $3.85, 13x | $50 |
| Base | 40% | Consensus met, 2028 EPS about $4.45, 14.4x | $64 |
| Bull | 20% | ARR back to 12%+, 2028 EPS $4.60, 18x | $83 |
| **Weighted** | | | **$60.7 (+11%)** |

**Bear case at full strength.** Net new ARR in Q3 was about half of last year's (third-party tally, unverified). The 2027 targets from the December 2024 investor day were $3B of ARR, $4B of revenue and a 30% EBITDA margin. ARR ends 2026 near $2.63B if the 10% guide holds, and 10% again gets to about $2.9B, so the ARR target is likely to be missed and February is probably when management says so. The whole software sector has de-rated on the fear that AI compresses seat-based pricing, and a company that just cut its recurring growth outlook is not the place to argue the fear is wrong. Thirteen analysts cover it. I have no information the market lacks.

**Symmetry check.** The discount to its own history is real, but a low multiple after a guidance cut is what a correct market looks like too. The multiple alone is not evidence.

**Catalyst and the number to watch.** Q4 results and 2027 guidance, February 2027 (last year's was 10 February). Confirms: 2027 organic ARR growth guided at 10% or better and Q4 net new ARR at or above Q4 2025's. Breaks: a guide below 9%, or year-end ARR below $2.60B.

### Arlo Technologies (ARLO), $12.32, $1.32B market cap, $1.19B EV

**What it does.** Sells home security cameras at or below cost and earns its profit on monthly subscriptions. 6.6M paid accounts and $370M of ARR.

**Reported evidence.** Services revenue by year: $103.5M, $136.5M, $201.2M, $243.0M, $316.4M (2021-2025), at gross margins of 59.7%, 66.5%, 73.7%, 77.5% and 83.5%. Product revenue went the other way: $331.6M to $212.9M, at a gross margin that fell from 14.0% to -14.6%.

| Quarter | Product $K | Services $K | Share | Product GM | Services GM |
|---|---|---|---|---|---|
| Sep 2026 | 53,145 | 96,032 | 64.4% | -15.9% | 81.0% |
| Jun 2026 | 62,890 | 93,047 | 59.7% | -0.4% | 81.1% |
| Mar 2026 | 60,283 | 90,099 | 59.9% | -4.6% | 83.7% |
| Dec 2025 (FY less 9M) | 51,907 | 89,390 | 63.3% | -16.3% | 82.8% |
| Sep 2025 | 59,587 | 79,942 | 57.3% | -18.5% | 84.5% |
| Jun 2025 | 51,230 | 78,175 | 60.4% | -15.4% | 84.3% |
| Mar 2025 | 50,217 | 68,849 | 57.8% | -7.7% | 82.2% |
| Dec 2024 (FY less 9M) | 57,425 | 64,147 | 52.8% | -12.6% | 81.2% |
| Sep 2024 | 75,784 | 61,883 | 45.0% | 1.3% | 76.7% |

- Beats are the largest of any name here: 34%, 46%, 43%, 22%.
- Q3 2026 (release, 5 Nov): services +20.1%, ARR +14.5%, paid accounts +23.1%. Accounts growing faster than ARR means revenue per account is falling at the margin. Services gross margin is down 3.5 points from a year ago.
- Two acquisitions in 2026, including Aloe Care on 16 April for $48.9M of consideration (10-Q), so some of the services growth is bought. I have not separated organic from acquired.
- Q4 guide: revenue $137-147M against $141.3M a year ago, non-GAAP EPS $0.17-0.23. The stock fell 16.8% the next day.
- Stock compensation was $80.4M over the trailing twelve months against free cash flow of $74.2M. After paying staff in stock there is no free cash flow. GAAP EPS for nine months is $0.17 against $0.80 non-GAAP.
- Diluted shares: 82.7M (2021) to 110.2M (2025). Buybacks ($63M trailing) have not yet stopped that. New $100M authorization through 2028.
- Remaining performance obligations are $51.5M. This is consumer month-to-month revenue.
- Insiders: 34 sales for $22.0M; one purchase of about $0.1M by a director on 10 November.

**Valuation.** 11.1x non-GAAP forward earnings, and about 56x trailing GAAP (Yahoo). There is no ten-year band because it lost money until 2023. EV is 3.2x ARR. Reverse DCF on reported free cash flow: -0.5% at 8.5%, 5.0% at 10%; after stock compensation it can't be solved because the base is negative. No same-denominator transaction found. If the non-GAAP multiple never changes and 2027 consensus of $1.13 is met, about $13.6 (+10%).

| Scenario | Prob. | Assumption | Price |
|---|---|---|---|
| Deep bear | 20% | ARR growth to high single digits; 2027 EPS $0.90, 9x | $8.1 |
| Bear | 25% | 2027 EPS $1.00, 10x | $10.0 |
| Base | 35% | Consensus $1.13, 12x | $13.6 |
| Bull | 20% | ARR +30% in 2027 as management targets, EPS $1.30, 16x | $20.8 |
| **Weighted** | | | **$13.0 (+6%)** |

**Bear case at full strength.** The cheapness is an artefact of adding back stock pay. Management is reported to be targeting about 30% ARR growth in 2027 on partner launches (press summary of the call, unverified); that is guidance, ARR growth is 14.5% today, and the gap between them is the whole bull case. The hardware is sold at a loss into a market where Ring and Google set prices.

**Catalyst and the number to watch.** Q4 results, late February 2027. Confirms: ARR growth above 15% and services gross margin back above 83%. Breaks: ARR growth below 12%.

### Digi International (DGII), $65.05, $2.47B

**What it does.** Industrial routers and IoT modules, plus subscription monitoring for things like restaurant temperature logs and tank levels. ARR was $191M at 30 June 2026.

**Evidence.** Service share 27.2% to 35.6% in two years at a service margin of 78% to 81%; product margin also rose, 50% to 58%. ARR +52%, but the release says most of it came from buying Jolt (August 2025) and Particle (January 2026). Four beats (10%, 2%, 7%, 13%). Net debt $81M.

**Valuation.** 20.8x fiscal 2027 consensus against a 14.1x median since 2020 (I could only build six years on a consistent definition of adjusted EPS). The stock is up about 70% in a year. Reverse DCF 3.1% / 8.9%. Scenarios: $39 (15%), $47 (30%), $66 (40%), $83 (15%); weighted $58.8, 10% below price. If the multiple holds and EPS grows 10%, about +10%.

**Why it's here.** It passes six tests and fails the one that matters, which is price. The fiscal Q4 report and FY27 guidance are due this week or next. It becomes interesting near $50, which is 16x.

### Vontier (VNT), $43.13, $5.73B

**What it does.** Fuel dispensers and payment systems for convenience stores (Gilbarco), plus tools for mechanics (Matco).

**Evidence.** No product and service split, and no recurring-revenue metric in the release, so tests 1 and 2 can't be run. Q3 2026: reported sales -2.1% after selling Teletrac Navman, core sales +5.7%, adjusted EPS $0.92, guide raised to $3.60-3.64. Net leverage 2.3x. 8.8M shares bought back this year.

**Valuation.** 11.2x against a 10.3x median since 2022, up 15% in the week since the print. Trailing free cash flow yield 7.3%. Scenarios: $29 (15%), $36.5 (25%), $45.7 (45%), $56 (15%); weighted $42.4, 2% below price.

**Why it's here.** It is the cheapest finalist on cash flow and a useful control. It is cheap because it has always been cheap, and nothing dated would change that.

## 5. Audit list

V = verified in a primary source this session. S = secondary source only. I = inferred or my estimate. U = could not verify.

| Figure | Source | Status |
|---|---|---|
| All product/service revenue, cost and margin tables | Income-statement R pages of each 10-Q and 10-K; Q4 = fiscal year less three quarters | V (parser checked against Itron and OSIS audit values) |
| Latest-quarter headline figures for NSSC, TRMB, ARLO, DGII, VNT | Earnings releases, 8-K ex. 99.1 | V |
| NSSC $0.09 tariff refund in Q4 FY26 EPS; $0.40 litigation; non-GAAP $1.60 | Release, 24 Aug 2026 | V |
| NSSC Q1 FY27 EPS $0.36; consensus $0.375 | Release; Yahoo | V; consensus S. Yahoo "actual" of $0.34 unexplained |
| NSSC two distributors destocking, sell-through up | Release and 10-Q MD&A (management statement) | U as a fact |
| NSSC shares 35,768,437; $1.0M litigation benefit | 10-Q | V |
| TRMB ARR $2.56B, +11%, +10% organic; guide $3.63-3.69 | Release and 10-Q | V |
| TRMB ARR outlook cut from 12-14% to about 10%; 2027 "consistent with exit rate"; February guidance | Press coverage of the call | S |
| TRMB net new ARR half of prior year | Third-party tally | U |
| TRMB $562M T&L impairment; buyback figures; $768.3M remaining | 10-Q | V |
| TRMB 2027 targets ($3B, $4B, 30%) from December 2024 investor day | Press coverage | S |
| TRMB 2026 adjusted EBITDA about $1.14B, 12x | My estimate | I |
| ARLO ARR $369.9M, +14.5%; accounts 6.6M, +23.1%; guide | Release | V |
| ARLO Aloe Care $48.9M; RPO $51.5M; Verisure largest customer | 10-Q | V |
| ARLO 30% ARR growth target for 2027; Comcast mid-2027 | Press summary of the call | S |
| ARLO organic vs acquired services growth | Not separated | U |
| DGII ARR $191M, +52%, acquisitions named | Release, 5 Aug 2026 | V |
| VNT Q3 figures, 2.3x leverage, buybacks | Release, 5 Nov 2026 | V |
| Non-GAAP EPS history: TRMB 2013-25, ITRI 2013-25, VNT 2021-25, DGII FY20-25, ARLO 2023-25 | Year-end releases, each cross-checked against the next year's prior-year column where shown | V, except VNT 2022 and 2024 and DGII FY20-22 read from one release only |
| NSSC EPS history FY14-25 | XBRL GAAP diluted, halved before the January 2022 split | V for FY16-26; FY14-15 from memory of filings, I |
| P/E bands and percentiles | My calculation; forward uses later-reported EPS as a stand-in for consensus then | I (method stated) |
| Consensus EPS and revenue, analyst counts, beat sizes | Yahoo, 10 Nov 2026 | S, to be replaced by LSEG |
| Trailing free cash flow and stock compensation | XBRL companyfacts (fiscal year plus year to date less prior year to date) | V arithmetic; TRMB level looks high, see text |
| Net debt, market cap, EV | Yahoo; cash checked against releases for ARLO, DGII, VNT | S |
| Reverse DCF | Two-stage, five years then 3%, at 8.5% and 10% (`nextpos_valuation.py`) | I. OSIS row uses the audit's 8.8% and 9.0% |
| Scenario probabilities and multiples | Mine | I |
| Insider transactions | Forms 4, codes P and S, 11 Nov 2025 onward | V |
| Price moves and volume | Yahoo daily history | V |
| Itron 2026 goodwill increase of $345M | 10-Q balance sheet ($1,345M to $1,690M) | V; share of service growth that is acquired not checked |
| HCSS at more than 28x EBITDA | M&A news summary | S |
| S&P 500 trailing P/E 23.9x | Yahoo (SPY) | S |
| Earnings dates for February 2027 | Yahoo calendar or last year's date | I |

Not done: I could not read any call transcript (the transcript sites are outside this environment's network allowlist, as is Yahoo's earnings-history page), any sell-side note, or any 13G. USAspending was not relevant to these five.

## 6. LSEG request list

Priority order: NSSC.OQ, TRMB.OQ, ARLO.N, then DGII.OQ and VNT.N if you have time. For each:

1. **Estimate Details, annual**, FY+1 to FY+3, with actuals and the estimate history: revenue, EPS, EBITDA, EBITDA margin, free cash flow, shares outstanding.
2. **Estimate Details, interim (quarterly)**, same measures, as far back as available, actual against mean, for the beat history. This replaces the Yahoo beat sizes above.
3. **Segment and KPI estimates, quarterly, actual against mean:**
   - NSSC: equipment revenue, recurring service revenue, gross margin by line if carried.
   - TRMB: AECO, Field Systems, Transportation and Logistics revenue and operating income; ARR; subscription and services revenue.
   - ARLO: product revenue, subscriptions and services revenue, ARR, paid accounts, services gross margin.
   - DGII: IoT Products and Services, IoT Solutions, ARR.
   - VNT: Environmental and Fueling, Mobility Technologies, Repair Solutions.
4. **Shareholders Report** with the last five quarter-end positions.
5. **Full daily price history** (max range), with volume.
6. **Three or four recent sell-side notes each, at least one cautious.** For NSSC I'd most like whichever note followed the 2 November miss; for TRMB one from 4-5 November that discusses the ARR cut and the 2027 targets; for ARLO one that models stock compensation.
7. **Transcripts** of the latest call for NSSC (2 Nov), TRMB (4 Nov) and ARLO (5 Nov), since I couldn't open them here.

## 7. Sizing note

- **Itron overlap.** Low. Two-year daily return correlation with Itron: Trimble 0.38, Arlo 0.29, Digi 0.25, Napco 0.22, Vontier 0.47; after removing the small-cap index the figures are 0.15, 0.11, -0.06, -0.02 and 0.24. None of these doubles the Itron bet. The overlap that matters is in the idea: all are hardware-to-recurring stories, and they would de-rate together if the market decided recurring revenue deserves less.
- **Napco.** The evidence supports a starter of about 3-5% of the account, and nothing above that before the February print. It is a $1.1B company trading about $13M a day, so size is not constrained by liquidity. A clean February (equipment flat or better, recurring 11%+) would justify moving toward 8-10%.
- **Trimble.** Up to about 5%. It is the most liquid and the least likely to be a permanent loss, and also the one where I have the least edge. A 2027 guide at 10%+ ARR growth would justify more.
- **Arlo.** Zero to 3%. The beats are real and so is the stock compensation. I would want the LSEG notes and an organic services growth figure first.
- **Digi and Vontier.** Zero at these prices.
- **OSIS.** The audit put its weighted value 6% above price. Napco at 8% and Trimble at 11% are not different enough to pay the spread and reset the clock. If you hold OSIS into 28 January, the two February prints above arrive within two weeks of it, and all three decisions can be made on reported numbers.

## Files

- `nextpos_universe.py`, `data/nextpos_universe_raw_2026-11-11.csv`, `data/nextpos_universe_inrange_2026-11-11.csv`: universe and Yahoo metrics.
- `nextpos_splitscan.py`, `data/nextpos_splitscan_2026-11-11.csv`: product/service scan of the latest 10-Q for every in-range name.
- `secutil.py`, `nextpos_split.py`, `nextpos_q.py`, `data/split_*.txt`: filing parser and quarterly tables.
- `nextpos_facts.py`, `data/facts_annual.txt`: ten-year XBRL fundamentals.
- `nextpos_valuation.py`, `data/nextpos_valuation_2026-11-11.json`: P/E bands, trailing cash flow, reverse DCF.
- `nextpos_insiders.py`, `data/insiders.txt`: Form 4 scan.

Sources: SEC EDGAR filings for each company (10-Q, 10-K, 8-K ex. 99.1, Forms 4); Yahoo Finance prices and consensus, 10 Nov 2026; [Trimble Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0000864749/000086474926000119/a2026q3-8kex991.htm); [Investing.com on the Trimble growth outlook cut](https://www.investing.com/news/company-news/trimble-q3-2026-slides-margins-ahead-of-plan-growth-outlook-cut-93CH-5000267); [Napco fiscal Q1 2027 release](https://www.sec.gov/Archives/edgar/data/0000069633/000110465926121107/nssc-ex99d1.htm); [SecurityInfoWatch on Napco](https://www.securityinfowatch.com/alarms-monitoring/article/55416151/napco-security-technologies-napco-recurring-revenue-growth-offsets-softer-equipment-sales-in-fiscal-q1); [MarketBeat on the Arlo Q3 call](https://marketbeat.com/instant-alerts/transcript-arlo-technologies-q3-earnings-call-highlights-2026-11-06/?amp=); [Seeking Alpha on Trimble's 2027 targets](https://seekingalpha.com/news/4515985-trimble-outlines-3b-arr-and-4b-revenue-targets-for-2027-as-ai-and-recurring-revenue-drive); [Mainsights on HCSS](https://www.mainsights.io/ma-news/germany-based-nemetschek039s-publ-construction-software-division-is-set-to-acquire-us-based-hcss-from-thoma-bravo-valuing-the-asset-at-more-than-eur-2bn).
