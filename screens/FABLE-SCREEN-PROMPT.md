# Master prompt: find the next position (paste into a fresh Fable 5.2 session)

You are helping Darren find his next stock position and, later, write it up for his Substack, "Primary Source Arbitrage" (darrenleung1.substack.com). Today's job is the search and the first-pass diligence. It ends with a ranked shortlist and an exact list of analyst-estimate files for Darren to export from his LSEG terminal. Do not write a post yet.

## Who this is for and what just happened

Darren runs a small account, so each position is a large share of it (his current OSI Systems stake is about 20%). His biggest position is Itron (ITRI). He just spent a week on OSI Systems (OSIS) and an audit of that work found the stock is fairly valued with a thin edge. He wants a better home for that capital, or confirmation that none exists right now.

Read these first, in the repo at `/home/user/nvda-next-post-` on branch `claude/fervent-clarke-e23gqc`:

- `osis/16-number-audit.md`: every OSIS number re-derived, with what was wrong. This is the standard of checking expected from you.
- `osis/DRAFT-post.md`: the corrected OSIS post, for voice and for how a thesis should be caveated.
- `osis/FINAL-DECISION.md` and `osis/MASTER-review-doc.md`: how he frames a decision.
- `screens/`: the existing small-cap screen (`smallcap_screen.py`, the 9 Nov CSV) and peer regression scripts. Reuse and extend these rather than starting over.
- Invoke the skill `anthropic-skills:my-writing-style` before writing anything he will publish or send.

## The pattern he is good at

An installed hardware base that is turning into higher-margin recurring revenue, still priced as hardware, with a dated event that forces the market to look. Itron is the template. From his 28 Oct 2026 post, Itron shows:

- Service gross margin rising: 43.9% to 53.2% over two years. Product gross margin also rising: 32.6% to 38.1%.
- Service share of revenue rising: 12.5% to 18.4%.
- Earnings beats of about 20% or more in three straight quarters.
- About 14x earnings, well below the market and its own history.
- A dated catalyst: guidance in February, an investor day around March.

OSIS failed the same tests: service gross margin fell from 47.6% to 42.9%, service share is flat near 25%, the last EPS beat was 0.8%, and it trades at 17x, which is its own median. Use Itron and OSIS as the two benchmark rows in every comparison table.

## What to find

Candidates that pass most of these, judged on reported numbers and never on guidance alone:

1. Recurring or service gross margin flat or rising for at least eight quarters, and at least 10 points above product margin.
2. Recurring or service share of revenue rising over two years because that line is growing, and not because product revenue fell. Check both numerator and denominator.
3. Estimates being beaten: EPS above consensus in at least three of the last four quarters, with the size of each beat.
4. Valuation at or below the company's own ten-year median on forward earnings, and below the market.
5. Demand that is contracted or non-discretionary: backlog, remaining performance obligations, regulated or mandated spending.
6. A dated event inside twelve months that could change how the stock is classified or modeled: segment disclosure, investor day, a first recurring-revenue metric, a spin-off, an index change, a contract start.
7. Not a trap: revenue not shrinking, not loss-making, net debt under about 3x EBITDA, share count not rising.
8. Small or mid cap, roughly $1B to $15B, US-listed, with thin or lagging coverage.

Also say plainly if nothing clears the bar. "Add nothing and hold cash until OSIS reports in January" is an acceptable answer.

## Data and tools

You are in a cloud container. These hosts are already allowed: Yahoo Finance (`query1`/`query2.finance.yahoo.com`), `data.sec.gov`, `www.sec.gov`, `efts.sec.gov` (EDGAR full-text search) and `api.usaspending.gov`. If a host you need is refused by the proxy, ask Darren for permission to add it; he has said to ask.

- **Prices and screening:** `pip install yfinance`. Use it for price history, 200-week averages, drawdowns, consensus growth, analyst counts and short interest. Treat Yahoo fundamentals as a screen only and confirm anything load-bearing in filings.
- **SEC filings:** send a descriptive `User-Agent` header with a generic contact, never Darren's name or email. Use `data.sec.gov/api/xbrl/companyfacts/CIK##########.json` for the main statements and `data.sec.gov/submissions/CIK##########.json` for the filing index.
- **Product versus service split:** it is not in companyfacts because it is dimensional. Pull it from the income-statement page of each 10-Q and 10-K (`R2.htm` to `R6.htm` under the filing's Archives folder), where product and service revenue and cost of goods sold appear as separate sections. Derive Q4 as the fiscal year minus nine months.
- **Non-GAAP EPS history:** read it from the reconciliation table in each fiscal year-end earnings release (8-K, item 2.02, exhibit 99.1). Each release gives the current and prior year, so every value can be cross-checked.
- **Insiders and holders:** Forms 4 for open-market purchases (transaction code P) and sales; 13G filings for large holders.
- **Government contractors:** USAspending.gov for actual obligations against any contract a company announces. A contract ceiling is permission to buy, and only funded orders count.
- **LSEG spreadsheets in the repo:** `openpyxl` fails on their stylesheet. Read them by unzipping and parsing `xl/worksheets/*.xml` and `xl/sharedStrings.xml` directly.
- **Web search:** use it for transactions, legislation and regulator reports, and cite what you find.

## The work, in order

1. **Universe.** Start from the existing screen and widen it. Aim for a few hundred names across metering, test and measurement, detection, industrial automation, building controls, fleet and fuel systems, medical devices with consumables, and security hardware.
2. **Quantitative cut** to about 20 names using Yahoo data: valuation against own history, drawdown from high, growth, margins, leverage, coverage.
3. **Primary-source tests** on those 20, from filings: the eight tests above, with eight or more quarters of product and service margin where the company reports the split. Cut to five to eight.
4. **Valuation on the finalists.**
   - Rebuild a forward and trailing P/E band from daily prices and reported non-GAAP EPS back at least ten years. State the median and where today sits as a percentile.
   - Run a two-stage reverse DCF (five-year growth, then 3% terminal) and report the implied growth at two discount rates. Do not use a single-stage shortcut.
   - Find a private-market or transaction multiple if one exists, on the same denominator.
   - Build four scenarios with probabilities and a price each. The bear cases must assume earnings miss consensus; a de-rate on consensus earnings is not a bear case. Show the probability-weighted value against today's price.
   - State the return if the multiple never changes.
5. **Catalysts.** Each one with a date and a source. Say what number on that date would confirm or break the idea.
6. **The estimate request.** For each finalist, list the exact LSEG exports Darren should pull.

## What to ask Darren for (the LSEG list)

For each finalist, annual and interim, with actuals and the estimate history:

- Revenue, EPS, EBITDA, EBITDA margin, free cash flow, shares outstanding, FY+1 to FY+3.
- Segment revenue for every reported segment, quarterly, with actual versus mean estimate (for beat rates).
- EPS and revenue quarterly back as far as available, actual versus mean, for the beat history.
- The shareholders report with the last five quarter-end positions.
- Full daily price history.
- The three or four most recent sell-side notes, including at least one cautious one.

Then stop and wait for those files.

## Mistakes the last file made (do not repeat them)

- Dividing price by stale earnings. Use trailing four quarters or the correct fiscal year.
- Comparing a best quarter with a seasonally weak one and calling it a trend. Compare like quarters or full years.
- Treating rounded company figures as precise. Backlog reported to the nearest $0.1B carries real error.
- Using GAAP EPS that includes a one-time gain as the base for a growth calculation.
- Calling a contract ceiling "funding", or an agency appropriation "locked" for one vendor.
- Reading a rising mix percentage as growth when the other line had shrunk.
- Quoting institutional ownership from a holder list that sums past 100%.
- Stating direction wrong on a number copied from memory. Open the filing.
- Claiming analysts ignore something that is in the first paragraph of their notes. Read the notes.

Apply the symmetry test to every claim: if the data had come in the other way, would you have concluded the opposite? If good and bad outcomes both support the thesis, the claim is not evidence.

## What to hand back

1. A one-paragraph answer: the best candidate, how sure you are, and what would change your mind. Lead with this.
2. A comparison table: each finalist plus Itron and OSIS as benchmark rows, one row per name, with the eight tests, the multiple against its median, implied growth, weighted value against price, and the next dated event.
3. One page per finalist: what it does in two sentences, the reported evidence, the valuation, the bear case at full strength, the catalyst and the number to watch.
4. An audit list: every figure, its source, and whether you verified it, could not verify it, or inferred it.
5. The LSEG request list.
6. A sizing note. Darren's positions are large relative to his account, so say what weight the evidence supports for each name and what further evidence would justify more. Note any overlap with Itron, since it is already his largest holding. This is analysis for his own decision and not personal financial advice.

Save the work under `screens/` in the repo with a dated filename. Commit and push only to the branch your session is assigned, tell Darren which branch that is, and do not open a pull request unless he asks.
