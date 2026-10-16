<!-- ============================================================
DRAFT v3 — Post 2 (Burry/NVIDIA pair). Updated to Oct 16, 2026. Not for publish.
Darren: remaining items to finalize before publish (delete this block after):
  - B200 index: using ~$5.86 (Oct 2). Swap for latest reading.
  - $99B equity investments: cited to 10-Q; confirm headline total.
  - NVDA EV/EBITDA: "about 14x" scales 14.81x (Aug 27 $227.98) to $215.20; likely lower
    since FY28 EBITDA est rose. Confirm current TIKR/LSEG reading before publish.
  - Anthropic Q3 numbers are IPO-roadshow figures (adjusted); label as such.
  - CXMT 4F² and Acer quote: want primary sourcing before quoting hard.
  - CHARTS: [C1] token index vs rent; [C2] order of damage Oct 7->16 (BUILT: charts/);
    [C3] $/GW charged vs ~$/GW earned; [C4] three-layer rent.
  Primary-sourced: MSFT 25yr (Amy Hood Q4 FY26 call); NVDA 70% receivables (10-Q Note 7);
  Nebius/IREN earns per MW (Q2/FY26 calls); OpenAI $856B/$278B (FT Sep 21);
  Feynman $60B (NDR deck Sep 2026 p.11); Anthropic Q3 (FT Oct 14); CRWV CDS (Oct 15).
============================================================ -->

# What Is NVIDIA Worth When the Shortage Ends?

*The shortage ending is not NVIDIA's risk. On the contracts the neoclouds are signing now, a gigawatt of compute pays back its chips in about two years and runs for six, so rent can fall a long way before NVIDIA loses the upgrade sale. The risk is whether the AI labs can keep paying for the tokens. Over the past week the market has started pricing that risk in the credit of the companies around NVIDIA, and the order it is doing it in is the whole argument.*

---

On October 8, the AI complex sold off in a specific order. CoreWeave fell about 8%. Oracle fell 6%. Micron 4.8%. NVIDIA fell 2.9%, the least of the group, and closed at $230.48.

That order is the whole argument of my last post, playing out on a single tape. The companies most exposed to who pays for the compute took the damage first. The company that sells the chips took it last.

In the week since, it got louder. By October 16, NVIDIA was $215.20, down about 9% from its October 7 high. CoreWeave was down about 30% over the same stretch, and Nebius about 29%. On October 15, the cost of insuring CoreWeave's debt hit a record, with its five-year credit default swap pricing a better-than-even chance of default, and some of its bonds yielding 16%. Jensen Huang went out of his way that day to say CoreWeave is getting stronger and NVIDIA has no need to bail it out, and the stock closed up almost 6%. The same ordering held all week. The lessors took the damage. NVIDIA took a third of it.

[C2: NVDA, CoreWeave and Nebius indexed to October 7, showing the lessors falling three times as far as NVIDIA through October 16.]

None of this was triggered by a fall in GPU rent, which is what Michael Burry is short. It was triggered by a question about whether the companies renting compute can pay for it. That question has a cleaner shape than the headlines, and answering it is the point of this post.

Start with where it began, on October 8, when OpenAI told investors it had reached about $50 billion in annualized revenue at the end of September. The figure widely reported over the prior week was $68 to $70 billion. The gap is not a demand miss. It is the difference between gross and net: the $70 billion counts the full value of OpenAI's models wherever they are sold, including through clouds like Azure that book the sale as their own, and the $50 billion counts only what OpenAI keeps. Underneath, OpenAI's run rate was still growing about 77% a quarter. The market sold a company growing 77% because a number it had been quoting turned out to be measured a different way, and then it kept selling, into the credit of everyone downstream of the labs. What moved the tape was the reminder of how much of this build rests on what the labs can pay.

This is not a niche question. NVIDIA is the single largest weight in the S&P 500. If you own an index fund, you own this question.

Burry has given himself room to be early. In late September, according to Stocktwits, he rolled his NVIDIA short into September 2027 puts struck in the mid-$100s. A later expiry moves his clock toward the 2028 and 2029 supply wave, which is where my last post's memory argument runs out. So this post answers the rolled-forward version of his bet. The question is not whether the shortage ends. It is what NVIDIA is worth when it does.

The conventional answer is clean. Chips stop being scarce, old-chip rent falls, NVIDIA's pricing power erodes, and a bull case built on today's prices comes apart. **My answer is that the shortage ending barely touches NVIDIA, and the thing that actually threatens it is a different event with a different clock: the AI labs running out of money to pay for compute.** Those are two separate bets. Only the second one reaches the stock, and even now, with the credit market getting nervous, I do not think it lands before Burry's puts expire. The rest of this post is why, with the arithmetic that decides it.

Steve Eisman, who is long NVIDIA himself, put the reason the depreciation fight misses the point on October 2: Burry's useful-life argument is "too academic." I think that is right, and not a dismissal. What a chip is worth is its rent, rent is paid by whoever is renting the compute, and the question that decides NVIDIA is whether those renters keep paying once chips stop being scarce. Eisman and I end up in the same place. The difference is that he says it on television without numbers, and the numbers are the entire argument.

## The short version

- **What happened:** Since October 8 the AI complex has sold off in order of who holds the financing risk. CoreWeave and Nebius fell about 30%, and CoreWeave's default insurance hit a record, while NVIDIA fell about 9%. The trigger was lab and lessor financing, not a fall in GPU rent.
- **When the shortage ends:** Memory and power stay short through 2028 on the makers' own guidance, though the timing is now contested. When supply does ease, old-chip rent can fall, as H100 rent fell 44% the last time a shortage broke.
- **Why that barely touches NVIDIA:** The scarce asset is the powered building, not the chip. On the multi-year deals Nebius and IREN are signing now, a gigawatt of compute brings in roughly $20 to $25 million per megawatt a year and pays back its chips in about two years, against a six-year life. Rent would have to fall by half before a chip stops covering its cost, and right now rent is rising. The cloud swaps new chips into the building it already powered, and NVIDIA sells every upgrade at a rising price per gigawatt ($18 billion for Hopper, $25 billion for Blackwell, $40 billion for Rubin, $60 billion for Feynman).
- **Where the real risk is:** Not the old chips' value. It is whether the AI labs, which Kress says NVIDIA expects to back with its own balance sheet at roughly a quarter of next year's business, can keep funding the demand the whole build rests on. The news this week cut both ways: Anthropic told investors it is now profitable and makes $1.70 of revenue for every $1 of compute, while the credit market put CoreWeave's default odds above even.
- **What I hold:** NVIDIA.
- **What would prove me wrong:** The labs' money drying up while capacity keeps arriving. It shows up as a neocloud that cannot refinance, ACIE revenue falling quarter over quarter (rule 8), and the labs' funding rounds shrinking or pricing wider, not as a markdown in what the old chips are worth.

## When the shortage ends

Burry's catalyst is the bottleneck easing. My last post made the case that it does not ease before his puts expire, and I will not repeat all of it. The short version is that the people who sell the shortage and the people who buy into it agree on the timing. Micron said on September 30 it has "no line of sight" to when supply and demand return to balance. Samsung said on July 30 it is "unlikely to see any significant increase in incremental supply through 2028." NVIDIA's own CFO, Colette Kress, said on August 26 that supply stays a bottleneck "at least through the end of fiscal year '28," which ends in January 2028.

One point worth being precise about, because it runs through the whole argument: the thing in short supply is memory and power, not NVIDIA's chips. NVIDIA can make plenty of GPUs. What it cannot conjure is high-bandwidth memory and a building with power running to it. That is what holds rent up, and it is why the shortage lasts.

The timing is now contested, and I would rather say so than lean on one side of it. A Chinese maker, CXMT, said in October it has a denser next-generation DRAM design with server product by year-end, Acer's CEO said shortages "have completely disappeared" and prices peak around mid-2027, and Samsung and SK hynix ended a record buyback early as their stocks rolled over. That is the first real cluster of "sooner" signals. But the memory inside NVIDIA's chips is HBM, a tighter market that is sold out for 2027 and priced higher again, not the commodity DRAM CXMT is targeting, and a density breakthrough with unproven volume is not the same as supply that moves the global balance. So I read it as a reason to watch rule 7, not to change the clock.

And here is the part that matters for NVIDIA: the exact timing barely changes the answer. When a shortage does break, old-chip rent falls, and it can fall hard. Silicon Data's H100 index went from $3.40 an hour in September 2024 to $1.90 by February 2025, down 44% in five months. The question is what a 44% fall does to NVIDIA, and the answer turns on an asset that is not the chip.

## The scarce asset moved

The thing that is actually hard to get is not the GPU. It is a building with power running to it.

You can see this in the lead times. A gas turbine ordered today is quoted for delivery around 2031, and large transformers run three to five years (a16z, citing TrendForce, September). Power interconnection and permitting take years more. Against that, the chip inside the building is the fast part, swapped every few years. IREN's co-CEO, Daniel Roberts, put the whole thesis in one line on the company's August 27 call: "The digital world scales almost instantly, the physical world does not. Power, land, data centers, these things take years to permit, finance and build."

NVIDIA says the same in its own filings, in the plainest possible terms. Its latest 10-Q books a category called "Land, Power, and Shell Guarantees for AI Clouds," where it backs partners' data-center lease obligations if they default. A guarantee here means NVIDIA agrees to pay the building's lease if the cloud renting it cannot. NVIDIA is willing to put its balance sheet behind the land, the power and the shell. It is not doing that for the chips. That tells you which part it thinks is scarce, and it is also a real exposure, which is why it sits in the ledger at the end.

The buyers are now saying the same thing with their accounting. On its fourth-quarter call on July 29, Microsoft's CFO, Amy Hood, said:

> "Effective at the start of FY '27, we are extending the estimated useful life of our data centers and office buildings from 15 to 25 years, reflecting our operating history and expected use of these assets."

Microsoft's own 10-K depreciates the servers and network equipment inside those buildings over two to six years. So the same company now writes the building off over 25 years and the chips inside it over as little as two, and it stretched the building's life in the same year memory prices were setting records. Management is putting its depreciation schedule where the economics are. The shell is the long-lived asset. The silicon is the consumable.

This is the hinge of Burry's own analogy, turned around. In 1968 the computer-leasing companies were killed when IBM's next machine made the old one hard to re-rent. The equivalent risk today is that NVIDIA's next chip makes the last one worthless. But a neocloud is not only a bet on a chip. It is a bet on a building. Jensen Huang said as much at Goldman Sachs on September 10: the neoclouds "secure land power and shell for us that the CSPs have already exhausted," meaning the cloud service providers have used up the power and land they can easily reach, so the neoclouds go find more. And he was blunt about the fate of old chips once the building outlives them: "You can still rent Voltas. Voltas is 10 years old. All the Ampere in the world are all rented out."

Kress put the economics on the August 26 call, describing a 20-year site, where LPS is that same land, power and shell:

> "The LPS commitment secures a long-lived AI factory site, while the NVIDIA compute within the data center can be upgraded repeatedly."

**That sentence is the difference between Burry's story and this one.** The lessor's durable asset is the powered site. The chip is the part it refreshes, and every refresh is a sale for NVIDIA. And NVIDIA prices each refresh higher: its revenue opportunity per gigawatt has gone from about $18 billion with Hopper to $25 billion with Blackwell to $40 billion with Rubin, and the roadmap carries it to $60 billion with Feynman (Non-Deal Roadshow deck, September 2026, p.11). The building persists. The bill for filling it goes up every generation.

[C3: $/GW charged by generation ($18/$25/$40/$60B) against ~$/GW earned, below.]

## Does the upgrade pay?

Here is the question that actually answers the post, and until recently I could not close it, because the number you need is what a gigawatt of tokens earns, and the only public figure was Huang's claim that a 1 GW site "is being rented out for" about $50 billion a year. That is the seller's number, and it is the retail, fully-utilized, newest-chip top end.

The neoclouds' own books give the real figure. On its August 12 call, Nebius said its core one-to-three-year deals carry "a yield of $20 million to $25 million per megawatt," with customers prepaying 50% to 60% of the cost and a payback "less than 2 years." IREN, on August 27, said its recent three-year contracts price "in excess of $20 million per megawatt of IT load, paying back the compute investment in around 2 years," with active talks near $25 million. Two independent operators, the same number: **about $20 to $25 million per megawatt of IT load per year, which is $20 to $25 billion per gigawatt, paying back the chips in roughly two years.** Huang's $50 billion is the short-term premium end; Nebius confirms it, quoting $40 to $50 million per megawatt for six-month capacity. The durable, multi-year number is half that, and it is audited.

Now the math closes. NVIDIA's hardware for a gigawatt of Rubin is about $40 billion, and the full build, where GPUs are roughly two-thirds of the cost, is about $60 billion. A gigawatt earning $20 to $25 billion a year pays the chips back in about two years and the whole build in under three, against a chip life of six. After it has paid for itself, it earns for three or four more years. For the upgrade to stop making sense, rent has to fall far enough that a chip no longer covers its cost over those six years, and my last post put that break-even at roughly a 50% to 65% fall in the B200 index.

**Rent is going the other way.** IREN said its three-year contract pricing is up about 125% since November, and Nebius said its first capacity auction cleared 15% above the highest price it had ever charged for Blackwell. A 44% fall, the worst the H100 has ever shown, lands in the middle of that cushion, not through it. And because memory and power stay short through 2028, the scarcity premium comes out slowly, not at once.

The demand side of the same trade just reported, and it points the same way. On October 14, Anthropic told investors it made **$1.70 of revenue for every $1 it spent on computing power** in the third quarter, that it was profitable on an adjusted basis for the second quarter running, and that it was cash flow positive. Read the two numbers together. The cloud earns $20 to $25 million per megawatt and pays back its chips in two years. The lab makes $1.70 for every dollar of compute it buys. At the unit level, both sides of the compute trade are making money right now. That is what has to stay true for the upgrade cycle to keep turning, and this week it got more true, not less.

So the answer to what happens to NVIDIA after the shortage is that the chip economics have years of room. The thing that closes that room is not oversupply, which the shortage prevents. It is the earns side collapsing, rent falling by half because the demand for tokens fell, and that happens only if the people renting the compute stop paying. Which brings the whole post to one question.

## But only if the money keeps coming

The upgrade cycle, the thing that keeps NVIDIA selling after the shortage, runs on one input: a cloud that can pay for the next chip, out of its own cash or a new loan. Both depend on its customers paying. So the durable building does not break the chain. It moves the question one link down, to who pays.

The machinery for this is real and mostly works. Nebius says customers prepay 50% to 60% of the capital cost and will put up more than $9 billion of prepayments this year, and it has about $40 billion of contracted backlog to borrow against. IREN has turned this into a flywheel: prepayments cover about half the GPU cost, GPU-backed loans cover up to 90% of the rest, and it keeps its data centers unencumbered to finance later. These are companies funding the next building before it is built, which is the opposite of a business that needs old chips to hold their rent.

The weak version is the part Burry is describing, and this week it stopped being hypothetical. CoreWeave's DDTL 5.5, a $2.6 billion loan it closed on August 10, runs about five years against customer contracts that average about three. For the last two years, the lenders get paid only if CoreWeave re-rents those GPUs at a decent price. On October 15, the cost of insuring CoreWeave's debt hit a record, its five-year credit default swap implying a better-than-even chance of default over five years, up from about 30% a year ago, and some of its bonds traded to yield 16%. That is the renewal risk being repriced in the open. Jensen Huang said the same day that CoreWeave's capital costs are "actually declining" and that NVIDIA, which owns about 10% of the company, has no need to bail it out, and the stock reversed to close up almost 6%.

Two things are true about that at once, and the post has to hold both. The credit market is charging hard for CoreWeave's renewal risk, which is exactly the risk Burry is pointing at, and it is charging at the company level rather than inside the individual loans backed by a named customer's contract, which lenders still treat as safe. That is the opposite of 2006, when the risk was hidden behind investment-grade ratings and cheap insurance. Here it is priced in daylight. But priced is not the same as realized. A record CDS is stress, not default. CoreWeave can still refinance, at a price, and its co-founder told the Financial Times it is working toward an investment-grade rating that would reopen cheaper capital. The question is whether stress becomes failure, and so far it has not.

It is worth being clear about what blew up earlier, in July, because it was not this. A hedge fund running as much as 400% leverage on AI infrastructure stocks got margin-called, and its biggest holdings, Nebius, Micron, Sandisk and CoreWeave, each fell more than 35% as it was forced to sell into Citadel. The leverage that failed sat in stock positions, not in the GPU-backed loans. Twelve days later CoreWeave closed DDTL 5.5 anyway. The pattern this October is different, because the stress is in the credit itself. That makes it the more important one to watch.

So the upgrade is still financeable today, at a rising price. Whether it stays financeable is a question about the renters, and the renters are the labs.

## Who pays for the tokens

Start with who buys NVIDIA's chips, because it is more concentrated than the headline suggests. In its latest 10-Q, NVIDIA discloses that five direct customers made up 22%, 14%, 13%, 11% and 10% of its receivables, which is 70% from five accounts. At the fiscal 2026 year-end in January, three customers were 56%. The buyers are concentrating, not diversifying. NVIDIA does not name them, and given its customer categories they are the large cloud providers, system integrators and manufacturers that build for the hyperscalers and neoclouds, not the labs directly.

Those buyers' own revenue is concentrated one layer further, in the labs. I could not source Eisman's claim that about 70% of the hyperscalers' AI cloud revenue comes from OpenAI and Anthropic, so I flag it as his, but what I can source points the same way: CoreWeave's S-1 shows 62% of its 2024 revenue came from Microsoft, and Oracle's cloud backlog is reportedly about half OpenAI. NVIDIA sells to a handful of clouds, and those clouds sell to a handful of labs. The demand narrows as you follow the money down.

Kress named the exposure on the August 26 call. The AI labs "for which we expect to leverage our balance sheet" are, she said, roughly a quarter of NVIDIA's business next year. That is the layer NVIDIA backs directly, through equity stakes, through the $105 billion Ohio lease it guarantees for OpenAI, and through the land, power and shell guarantees. A quarter of the business leans on the two labs that anchor the whole chain, and this week those two labs told opposite halves of the same story.

Anthropic is the half that is working. Its revenue went from $4.7 billion in the first quarter to $11.6 billion in the second to $16.8 billion in the third, and on October 14 it told investors it was profitable on an adjusted basis and cash flow positive, the $1.70 per dollar of compute from the section above. Its growth is slowing, which cooled its expected IPO valuation from about $2 trillion toward $1.5 trillion, and its annualized revenue is tracking below $100 billion. But a lab that was losing more than $8 billion a year in 2025 is now, on its own account, paying its way. So the line I would have written a month ago, that the build rests on two labs that both lose money, is no longer true. The labs are diverging.

OpenAI is the half that still burns. Its own investor projection, reported by the Financial Times on September 21, plans about $856 billion of compute spending between 2026 and 2030 against a cumulative $278 billion of negative free cash flow. It keeps about $50 billion a year today and is raising again, reportedly about $30 billion at a $1.4 trillion valuation. So the risk concentrates: it is less "the labs cannot pay" and more "OpenAI depends on a capital market that is, this week, getting more expensive," with the IPO window itself wobbling as SB Energy, the developer behind the Ohio campus NVIDIA guarantees, delayed its own listing.

**This is where Eisman and I agree, and where I part from him.** He is right that the whole build leans on a small number of labs. But "the labs" and "compute demand" are not the same risk. What threatens the labs, no moats and a drift to cheaper open-weight and Chinese models, hurts the labs' economics. It does not make the compute go away, because those models still run on GPUs and cheaper models pull in more use. The risk to NVIDIA runs through financing, whether the companies that sign the multi-year contracts can keep paying them, not through tokens disappearing. That is a narrower claim than his, and it is testable.

There is a circular version of this, that NVIDIA funds the labs and the lessors that buy its compute, and it stopped being abstract on October 15, when NVIDIA's CEO personally talked up a company NVIDIA owns 10% of and sells chips to. The 10-Q shows NVIDIA has committed to equity investments in "AI model makers, infrastructure financiers, and other private companies," on top of roughly $99 billion of equity investments on its books. Huang's answer at Goldman Sachs was that "the circular part of it doesn't make much sense to me because the number shows it doesn't." I would hold him to the number. It is a real exposure, sized in the ledger, not proof of a fraud, but it is the exposure the market is now poking at.

One risk sits outside this post, and I want to be honest that I am leaving it out rather than pretend it is small. The labs could be forced to stop, not by economics but by a catastrophic AI event and whatever follows it. Both OpenAI and Anthropic are now openly planning for that scenario. I cannot put a number on it, so it is not in my ledger and it does not belong in a valuation. It is the subject of a separate post. Here I am pricing the money.

## What the multiple is already pricing

The strange part of this trade is that the stock is not priced for the bull case. Before this week NVIDIA traded at about 14.81x next-twelve-months EV/EBITDA, down from 32.44x a year ago, on a business that just grew 106% and guided to its first-ever full-year number. This week's selloff took it lower still, toward 14x and under. Microsoft, growing far slower, trades richer. The de-rating has already happened, and it is deepening.

That matters because Burry's puts do not strictly need rent to fall. The market can simply decide to price the end of the shortage early, assigning NVIDIA a lower multiple now because it expects growth to slow later, and the stock falls on the multiple alone, with earnings intact. You are watching that mechanism live, and not only in NVIDIA. Samsung guided to a record quarterly profit near $80 billion on October 8 and its stock is down more than 25% from its June high. Micron is near a technical bear market, about 20% off its June high, even as a peer, Nanya, just reported revenue up more than 600% year over year at an 85% gross margin. On October 14 Korea's KOSPI fell 7% in a single session on a chip rout. The market is not waiting for memory earnings to fall. It is selling the slowdown in growth, and this week it started doing the same to the AI infrastructure names, helped along by hotter-than-expected US inflation and a 10-year yield above 5%.

But here is the thing the multiple tells you, and it is the heart of my position. That is the multiple of a business the market expects to slow down, not one it expects to break. If the market genuinely thought a lab failure was coming, the kind that takes a quarter of next year's business with it, NVIDIA would trade where Micron does, at a single-digit multiple. It does not, even after this week. So the lab-failure risk, the only one that actually reaches NVIDIA, is still not fully in the price. That cuts both ways. If it happens, the stock falls hard, and Burry wins on the multiple rather than on rent. If it does not, the stock is cheap for what it earns. I am on the second side of that, because the demand under the stock improved this week even as the price fell: Anthropic turned profitable, OpenAI neared $70 billion, rent kept rising, and the only thing that broke was the price of insurance on the most levered lessor's debt.

A bear would point to Gartner, which said on October 14 that more than $3.5 trillion of AI infrastructure spending could face write-down by 2030 and that 80% of neoclouds will cease to operate independently. I take the warning seriously and read the second half carefully. "Cease to operate independently" is consolidation, not demand destruction. When a neocloud fails, its contracts and its powered buildings do not vanish, they get absorbed by a stronger operator or a hyperscaler, and the compute inside still gets bought from NVIDIA. That is the building thesis again, from the bankruptcy side. The risk it names is real for the neoclouds' equity and debt, which is what this week is about. It is a smaller risk for the company that sells the chips into whoever owns the building next.

## Break conditions

Rules 1 to 5 carry forward from my August 28 earnings post. Rules 6 to 9 are from my October 5 post. I grade each as written, not as reinterpreted after the data arrives. The one I want to flag is rule 6: a falling B200 index can mean the next chip arrived and pushed it down the ladder, which is the normal cascade, so I read it alongside rule 8, ACIE revenue, which is the cleaner signal of the labs' money reaching the order book.

| # | Rule | Threshold | Action | Status (Oct 16) |
|---|------|-----------|--------|-----------------|
| 1 | Non-GAAP gross margin below 72%, two consecutive quarters, Vera Rubin ramp | <72% x2 | Exit review | Not triggered. Q2 75.0%; Q4 guided 71–72%; one guided quarter below, so Q1 FY28 is the test. |
| 2 | ACIE/Hyperscale split reversing | Hyperscale reaccelerates while ACIE decelerates | Exit review | Not triggered. ACIE +25% q/q vs Hyperscale +13%. |
| 3 | Hyperscaler frames custom silicon as primary training compute, two calls, plus sequential Hyperscale decline | As stated | Exit review | Not triggered. |
| 4 | Vera CPU shipments delayed beyond Q1 FY2028 | As stated | Exit review | Not triggered. Shipping to lead partners. |
| 5 | FY2028 revenue guide walked back below 60% growth | <60% | Exit review | Not triggered. Guided 70%. |
| 6 | GPU rent: Silicon Data B200 index, three consecutive monthly readings before Sep 2027 | <$3.93 review; <$2.85 exit | Review / exit | Not triggered. ~$5.86 on Oct 2; read with rule 8. |
| 7 | Memory supply: Micron, Samsung or SK hynix says supply and demand balance in CY2027 | As stated | Exit review | Not triggered, but watch: CXMT's denser DRAM and Acer's "shortage gone" are the first sooner signals. All three makers still say tighter in 2027. |
| 8 | Lessor stress reaches the order book: ACIE revenue declines q/q | q/q decline | Exit review | Not triggered. +25% q/q in Q2. The Q3 print in November is the live test. |
| 9 | NVIDIA records a payment or loss under AI cloud, land/power/shell, SB Energy or residual-value support | Any | Review and resize | Not triggered. Watch: SB Energy delayed its IPO this week. |

Three candidate rules I am weighing, and want reader input on before I set them:

- **Neocloud refinancing.** A CoreWeave or peer refinancing that fails, or prices at a yield that makes the contract-backed model unworkable (CoreWeave bonds are near 16% as I write). The objection: "unworkable" needs a number.
- **Lab revenue.** OpenAI net annualized revenue below $70 billion at the end of 2026, the figure it has guided to during its raise. The objection: it is a private number I cannot audit.
- **Lab share.** NVIDIA's AI-lab share of the business, which Kress put at roughly a quarter, falling on two consecutive calls. The objection: a fall could be good news if the hyperscalers are growing faster.

## The close

Burry rolled his puts to September 2027, toward the supply wave where the memory argument runs out. When supply does catch up, what decides NVIDIA is not what the old chips are worth. A gigawatt pays back its chips in two years and earns for six, rent is rising, Anthropic is now making money on its compute, and memory stays short, so the shortage ending leaves years of room before it reaches the company that sells the chips. What decides NVIDIA is whether the labs renting the compute can keep paying, and this week the market started testing exactly that, in the one place the test shows up first: the credit of the most levered lessor, not the rent on the oldest chip. The order held. CoreWeave's insurance went to a record and NVIDIA fell a third as much.

I am still holding NVIDIA. This week is the risk I wrote down arriving on schedule, in the channel I said it would, and so far it is stress, not failure. The thing that would change my mind is not a fall in GPU rent. It is a neocloud that cannot refinance or a lab whose money runs short, and I am watching the credit tape for it, not the rent index. So the one question I would put to you is the one I am watching myself: which moves first, the price of insuring CoreWeave's debt, or the rent on an H100?

---

*Disclosure: I hold a position in NVIDIA. This material is for informational purposes only and does not constitute investment advice. Sources: NVIDIA Q2 FY27 10-Q (Notes 7, 10) and Q2 FY27 earnings call, August 26, 2026; NVIDIA Non-Deal Roadshow presentation, September 2026 (p.11); NVIDIA at Goldman Sachs Communacopia, September 10, 2026; Microsoft Q4 FY26 earnings call, July 29, 2026, and FY26 10-K; Silicon Data indices, accessed October 2026; Micron Q4 FY26 call, September 30; Samsung preliminary Q3, October 8; Nanya and KOSPI coverage, October 2026; CoreWeave Q2 call and 8-K, August 2026, CDS and bond pricing via ICE/LSEG/Bloomberg/Reuters, October 15, 2026; Nebius Q2 call, August 12, 2026; IREN FY26 call, August 27, 2026; a16z State of Markets, September 2026; Gartner press release, October 14, 2026; OpenAI projections via Financial Times, September 21, 2026; Anthropic Q3 figures via Financial Times and Reuters, October 14–16, 2026; OpenAI pricing page; Stocktwits and Benzinga coverage of Burry, late September 2026; Steve Eisman interview, October 2, 2026; LSEG and TIKR valuation data.*
