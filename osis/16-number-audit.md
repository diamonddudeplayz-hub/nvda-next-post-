# OSIS — Number Audit (11 Nov 2026)

Every figure in `DRAFT-post.md` re-derived from primary data: SEC XBRL + filings (CIK 1039065), the
18 fiscal year-end earnings releases, Yahoo price history and consensus (10 Nov close), USAspending.gov,
LSEG sheets in the repo (8 Nov), and web checks. "Was" = what the file or brief said.

## Wrong or stale (fixed in the draft)
| Item | Was | Re-derived | Source |
|---|---|---|---|
| Backlog "new high every quarter" | rose every quarter | $1.9B Sep-25, **$1.8B Dec-25**, $1.9B Mar-26, $1.9B Jun-26 (book-to-bill 0.98), $2.1B Sep-26 | earnings releases |
| Q1 FY27 GAAP operating income | down, $33.6M to $33.1M | **up**, $33.07M to $33.57M (+1.5%) | 10-Q / release |
| Q1 FY26 adjusted operating income | $39.6M | $39.78M (to $38.28M; margin 10.3% to 9.5% is right) | release reconciliation |
| Trailing P/E today | ~21x | **18.6x** on TTM non-GAAP EPS $10.59 (19.0x on FY26 $10.35). 21x used FY25 EPS | releases + price |
| FY25 non-GAAP EPS | $9.34 | $9.36 | Aug 2025/2026 releases |
| Forward P/E median | "12-yr ~18x" | 10-yr 16.7x, 12-yr 17.6x, since-2010 18.1x | rebuilt band |
| Reverse DCF | market prices ~4% growth | 2-stage: **6.1% (8.8% WACC) to 6.9% (9.0%)** for 5 yrs, 3% terminal. 4% is the single-stage Gordon figure | own calc |
| FCF yield | 5.6% NTM | FY27 consensus $209M = 6.7% of market cap, 5.4% of EV; $190M normalized = 6.1%; FY26 actual $245M = 7.9% | 10-K, LSEG |
| Gross margin history | "36% in 2017, declining since" | FY16 33.4%, FY17 33.7%, **FY18 36.0%**, FY25 34.3%, FY26 33.2%: a 33-36% range | XBRL |
| $200M CBP IDIQ | no task order | **$7.2M delivery order**, signed 28 Jul 2026 (70B03C26F00000506) | USAspending |
| "GAO flagged OSI scanners in storage" | GAO, OSI-specific | **DHS OIG, June 2025**: of 150 large-scale systems bought 2020-24, 50 installed, 43 in storage. Not vendor-specific. GAO separately: 52 of 153 operational, Feb 2025 | web |
| "$3.45B CBP NII" | all NII | one line covering NII plus surveillance towers, counter-drug, biometric entry-exit | Act summaries |
| Buyback funding | "one-time Mexico cash harvest" | FY26 buybacks $272M > FCF $245M; **$575M 0.50% convert issued Nov 2025** (converts at $353.82) | 10-Q Note 8 |
| Analyst coverage | "only 2 analysts" | 5-7 EPS estimates (LSEG, Yahoo); 2 publish segment detail | LSEG |
| Chart "reclaiming" | OSIS reclaiming | lowest close of the decline was **$191.61 on 5 Nov 2026**; never within ~8% of the 200-week | Yahoo |
| Itron lag | "a few months" | peak Jul-25 vs Apr-26; crash 30 Oct 2025 vs 5 May 2026 = about six months | Yahoo |

## Confirmed
- Price path: peak close $309.68 (17 Apr), intraday $311.72 (21 Apr); $282.87 to $234.74 on 5 May (-17.0%, 4.7x volume); $186.50 intraday 21 Aug (1.29M shares, about 5x); close $197.00 on 10 Nov. Peak to closing low -38.1%, intraday -40.2%.
- De-rate: 27.6x NTM at the April peak to 16.5x NTM / 17.2x FY27 now; trailing 33.1x to 18.6x.
- 200-week averages: OSIS $178.02, ITRI $92.05. ITRI: $138.42 to $78.02 (-43.6%), -21.1% on 30 Oct 2025, +26.2% on 28 Jul 2026, traded 9% below its 200-week.
- OSIS vs ITRI two-year average consensus growth: revenue 6.8% vs 3.2%, EPS 11.4% vs -1.3%; P/E 17.2x vs 14.7x.
- Coverage (backlog / LTM revenue): 1.05, 1.08, 1.00, 1.05, 1.06, 1.16x. Backlog is rounded to $0.1B, so about ±0.03x each.
- RPO about $2.0B, 64% within 12 months (10-Q). Bookings $583M, book-to-bill 1.4.
- FY26: revenue $1,786.0M (+4.3%), non-GAAP EPS $10.35 (+10.6%), OCF $275.9M, capex $30.6M. Revenue was $39M below the low end of the $1.825-1.867B guide. Q4 FY26 revenue -4.1% YoY.
- Q1 FY27: revenue $403.5M (+4.9%), non-GAAP EPS $1.66 (+17%), GAAP EPS $1.51, GM 30.7% vs 32.0%. Pre-tax income +$4.6M, of which interest -$4.1M. Service GM 42.0% vs 45.4%; product GM 26.2% vs 26.7%. Diluted shares 17.47M to 16.25M.
- Guidance: revenue $1.875-1.930B unchanged; EPS $11.28-11.64, raised from $11.13-11.49.
- Consensus: EPS FY27 $11.45 / FY28 $12.82-12.85 / FY29 $14.86 (one estimate); revenue $1.90-1.91B / $2.04B / $2.24B; EBITDA margin 16.1% / 16.1% / 16.6%. Q3 FY27 revenue estimate $497-498M vs $453.2M = +9.6 to +9.9%.
- EV/EBITDA: 12.2x (converts-only EV $3.72B) to 12.6x (Yahoo EV $3.85B) on FY27 consensus EBITDA of about $306M.
- CVC / Smiths Detection: £2.0B EV, 12.5x headline EBITDA of £160M, completed 30 Jun 2026.
- Secure America Act (S. 2) signed 10 Jun 2026; about $26B to CBP, available to 30 Sep 2029.
- CBP IDIQs: $200M and $85M ceilings, both single-award, four offers each; $21.2M order on the $85M.
- Scenario math: 0.13×134 + 0.25×172 + 0.37×218 + 0.25×270 = $208.6. Base $218 = 17x × $12.82.
- 2029 notes convert at $191.98 (1.82M shares; about 3.3% dilution at $270). No capped call in the 10-Q.
- Insiders: 46 Forms 4 since 20 Apr 2026; zero open-market purchases.
- Mexico award day: $91.14 to $98.23 on 20 Mar 2023 (+7.8%).

## New from USAspending (not in any prior doc)
- CBP obligations to Rapiscan under the 2026 IDIQs: $28.4M of $285M (10%).
- New federal awards to all OSI entities since 1 Oct 2025: about $56M.
- CBP detection-equipment obligations (product code 6665): FY21-26 Rapiscan $405M of about $1.06B among listed vendors (38%); FY26 Rapiscan $66.5M of about $229M (29%); FY25 about $201M total.
- 2021 precedent: $186.9M delivery order on 28 Sep 2021 (period of performance to Sep 2028), then almost nothing until 2026.

## Second pass (after the LSEG files were added, 11 Nov)
- **Security beat rate: confirmed.** 11 of 13 quarters beat the mean estimate (Q1 FY24 to Q1 FY27); misses were Q3 FY26 (-1.8%) and Q4 FY26 (-12.3%). Only two estimates per quarter. Consolidated revenue *beat* in Q3 FY26 (+0.9%) and missed only in Q4 FY26 (-8.6%), so "the ramp slipped twice" is one real miss plus one small segment miss.
- **Q1 FY27 revenue consensus was $396.1M** (LSEG mean), not $393M. EPS beat was $1.66 vs $1.647.
- **FCF consensus confirmed:** FY27 mean $209.5M (range $147-289M), FY28 $162.2M (range $93-235M). FY26 actual $245.3M matches the filings.
- **April bar:** Q3 FY27 revenue $497.7M (+9.8%), Security $355M (+11.2%), EPS $3.18 (+22%), EBITDA $85.2M vs $69.9M (margin 17.1% vs 15.4%). Q4 FY27 revenue $549M would be a record quarter by 9%.
- **FY28 EBITDA consensus $345M (+11.7%)**, margin 16.9%.
- **Ownership:** holder percentages sum to 137% (double counting; several managers appear as multiple entities), so "~90% institutional" is not derivable. September 13Fs were not in the file; "most recent" is June for most holders. March to June: BlackRock +3%, Janus +17%, **Fidelity -13%**. CFO 1.8% + founder 1.6% = 3.3%.
- **Doc 15 raw numbers confirmed** from the income statements: service share 25.0% (FY23), 21.5% (FY24), 22.8% (FY25), 24.7% (FY26 and TTM); service GM 41-49%, product GM 26-35%; DSO 178 to 151; net working capital $605M, $1,197M, $1,100M.
- **Doc 15 interpretation not supported:**
  - Service GM is not intact. FY22 47.6%, FY23 46.5%, FY24 43.8%, FY25 44.3%, FY26 43.8%, TTM 42.9%; the last two quarters were 41.4% and 42.0%.
  - Product GM is flat, not collapsing: 29.4%, 31.9%, 31.3%, 29.7% by fiscal year. "35.4% to 26.2%" compares the best quarter with a seasonally weak Q1; year over year Q1 product GM moved 26.7% to 26.2%.
  - Service share recovered because product revenue stalled (+1.1%, -4.9%, +5.1%), not because service grew (+5.0%, -1.4%, +4.4%).
  - Working capital rose $32M in Q1 FY27 (inventory +$48M). The unwind so far is essentially one quarter and one customer's payment.
- **Doc 14 decomposition:** the GAAP arithmetic is right (1.36x EPS, 2.69x multiple) but FY22 GAAP EPS of $6.45 sat above non-GAAP $5.81, so it included a gain. On non-GAAP trailing EPS the split is 1.70x EPS and 2.15x multiple (about 60% re-rate); on forward EPS it is 1.81x and 2.01x (about 54%). "Re-rate did 75%" overstates it.
- **"$177 buys back the 13x start"** is wrong: $177 is 15.5x FY27 EPS and 16.7x trailing. It is 13.8x only on FY28 EPS, two years out. The like-for-like 13x level is about $140-150.
- **Target matrix bear** ($179-192) assumes FY28 consensus EPS is hit, so it is a de-rate case, not an earnings miss. The "2-3:1 skew" comes from that.

## Could not verify (left as cited, or softened)
- "~90% institutional" ownership: Yahoo shows 127%, which is double counting. Draft now says "most of the float."
- "#1 in cargo, >50% share": company and trade-press claim. Draft says "by its own account."
- Itron's 26% day on 28 Jul 2026 being an earnings report: inferred from 9.8x volume and the date.
- Short interest: Yahoo shows 2.0M shares (about 13% of shares outstanding). With $925M of converts outstanding much of this is probably arbitrage hedging. Not used in the draft.
