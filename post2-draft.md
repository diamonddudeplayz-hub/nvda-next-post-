<!-- ============================================================
DRAFT — Post 2 (Burry/NVIDIA pair). Working draft, not for publish.
Darren: items to finalize before publish (delete this block after):
  - Feynman $60B/GW: confirm exact deck + date (the "Revenue Opportunity Per GW"
    slide you pasted). Sourced below as "NVIDIA investor presentation, Sept 2026";
    verify Feynman is in that deck vs a newer one.
  - $99B equity investments: cited to the 10-Q; confirm the headline total.
  - B200 index: using $5.86 (Oct 2). Swap for the latest reading before publish.
  - Oct 8 % moves + NVDA close: from your Oct 8 note (CRWV -8, ORCL -6, MU -4.8,
    NVDA -2.9, $230.48). Confirm against the xlsx when I build the chart.
  - Anthropic 2025 numbers kept as "reported" (prospectus via Reuters).
  - CHARTS to build: [C1] token index vs rent; [C2] Oct 8 order of damage;
    [C3] $/GW by generation; [C4] three-layer rent. Marked inline.
============================================================ -->

# What Is NVIDIA Worth When the Shortage Ends?

*When chips stop being scarce, the old chip's rent can fall and NVIDIA still holds, because the scarce asset is the powered building and NVIDIA sells the upgrade that goes into it. The weak link is not what the old chips are worth. It is who pays for the tokens, and on October 8 the market showed the order it breaks in.*

---

On October 8, the AI complex sold off in a specific order. CoreWeave fell about 8%. Oracle fell 6%. Micron 4.8%. NVIDIA fell 2.9%, the least of the group, and closed at $230.48.

That order is the whole argument of my last post, playing out on a single tape. The companies most exposed to who pays for the compute took the damage first. The company that sells the chips took it last.

The trigger was not a fall in GPU rent, which is what Michael Burry is short. It was a number about an AI lab. On October 8, OpenAI told investors it had reached about $50 billion in annualized revenue at the end of September. The figure widely reported over the prior week was $68 to $70 billion.

The gap is not a demand miss. It is the difference between gross and net. The $70 billion counts the full value of OpenAI's models wherever they are sold, including through clouds like Azure that book the sale as their own. The $50 billion counts only what OpenAI keeps. Underneath, OpenAI's run-rate was still growing about 77% a quarter.

The market sold anyway. It sold a company growing 77% because a number it had been quoting turned out to be measured a different way. What moved the tape was not what OpenAI earned. It was the reminder of how much of this build rests on what the labs can pay.

This is not a niche question. NVIDIA is 7.78% of the S&P 500, the single largest weight in the index. If you own an index fund, you own this question.

Burry has given himself room to be early. In late September, according to Stocktwits, he rolled his NVIDIA short into September 2027 puts struck in the mid-$100s. A later expiry moves his clock toward the 2028 and 2029 supply wave, which is where my last post's memory argument runs out. So this post answers the rolled-forward version of his bet. The question is not whether the shortage ends. It is what NVIDIA is worth when it does.

The conventional answer is clean. Chips stop being scarce, old-chip rent falls, NVIDIA's pricing power erodes, and a bull case built on today's prices comes apart. I think that looks in the wrong place. The scarce asset was never really the chip. It is the powered building the chip sits in, and NVIDIA sells the upgrade that goes into it. The chip is the part that is supposed to get cheaper.

Steve Eisman, who is long NVIDIA himself, put it on October 2: Burry's useful-life argument is "too academic." I think that is right, and not a dismissal. What a chip is worth is its rent, rent is paid by whoever is renting the compute, and the question that decides NVIDIA is whether those renters keep paying once chips stop being scarce. That is a question about money, not about silicon. It is also where Eisman and I end up in the same place, so the rest of this post is the part he left out: the numbers, and the order the damage arrives in.

## The short version

- **What happened:** On October 8 a lab revenue reset, not a rent decline, took down the AI complex in order of who holds the financing risk. CoreWeave and Oracle first, NVIDIA last.
- **When the shortage ends:** The memory makers and NVIDIA both say supply stays tight through 2028. When it does ease, old-chip rent can fall. The last time a shortage broke, H100 rent fell 44% in five months.
- **Why NVIDIA holds anyway:** The scarce asset is the powered building, not the chip inside it. Microsoft now depreciates its data centers over 25 years and the servers inside them over as little as two to six. Neoclouds swap new chips into buildings that already have power, and NVIDIA sells every upgrade, at a price per gigawatt that keeps rising: roughly $18 billion for Hopper, $25 billion for Blackwell, $40 billion for Rubin, $60 billion for Feynman.
- **Where the real risk is:** Not the old chips' value. It is whether the AI labs, which Kress says NVIDIA expects to back with its own balance sheet at roughly a quarter of next year's business, can keep funding the token demand the whole build rests on.
- **What I hold:** NVIDIA.
- **What would prove me wrong:** Token spend flattening while capacity keeps arriving. It shows up first as the Silicon Data B200 rent index below $3.93 for three straight months (rule 6) and ACIE revenue falling quarter over quarter (rule 8), with the labs' next funding rounds shrinking or pricing wider. Not as a markdown in what the old chips are worth.

## When the shortage ends

Burry's catalyst is the bottleneck easing. My last post made the case that it does not ease before his puts expire, and I will not repeat all of it. The short version is that the people who sell the shortage and the people who buy into it agree on the timing. Micron said on September 30 it has "no line of sight" to when supply and demand return to balance. Samsung said on July 30 it is "unlikely to see any significant increase in incremental supply through 2028." NVIDIA's own CFO, Colette Kress, said on August 26 that supply stays a bottleneck "at least through the end of fiscal year '28," which ends in January 2028.

So assume Burry is right about the eventual direction, just early. When a shortage does break, old-chip rent falls, and it can fall hard. Silicon Data's H100 index went from $3.40 an hour in September 2024 to $1.90 by February 2025, down 44% in five months, as the first Hopper shortage ended and new supply arrived. That is the event the bear case needs, and it is real. The question this post asks is what it does to NVIDIA, and the answer turns on an asset that is not the chip.

## The scarce asset moved

The thing that is actually hard to get is not the GPU. It is a building with power running to it.

You can see this in the lead times. A gas turbine ordered today is quoted for delivery around 2031. Large transformers run three to five years. Power interconnection and permitting take years more. Against that, the chip inside the building is the fast-moving, swappable part, replaced every few years. When people say "data center shortage," the binding constraint is the powered shell, and the GPU is what you slot into it once it is built.

NVIDIA says this in its own filings, in the plainest possible terms. Its latest 10-Q books a category called "Land, Power, and Shell Guarantees for AI Clouds," backstopping partners' data-center lease obligations if they default. NVIDIA is willing to guarantee the land, the power and the shell. It is not guaranteeing the chips. The company knows which part is scarce.

The buyers of these assets are now saying the same thing with their accounting. On its Q4 fiscal 2026 earnings call on July 29, Microsoft's CFO, Amy Hood, said:

> "Effective at the start of FY '27, we are extending the estimated useful life of our data centers and office buildings from 15 to 25 years, reflecting our operating history and expected use of these assets."

Microsoft's own 10-K depreciates the servers and network equipment inside those buildings over two to six years. So the same company now writes the building off over 25 years and the chips inside it over as few as six. It stretched the building's life in the exact quarter the memory shortage was at its worst. That is management putting its depreciation schedule exactly where the economics are: the shell is the long-lived asset, the silicon is the consumable.

This is the hinge of Burry's own analogy, turned around. In 1968 the computer-leasing companies were killed when IBM's next machine made the old one hard to re-rent. The equivalent risk today is that NVIDIA's next chip makes the last one worthless. But a neocloud is not only a bet on a chip. It is a bet on a building. Jensen Huang said as much at Goldman Sachs on September 10: the neoclouds "secure land power and shell for us that the CSPs have already exhausted." And he was blunt about the fate of old chips in a world where the building outlives them: "You can still rent Voltas. Voltas is 10 years old. All the Ampere in the world are all rented out."

Kress put the economics on NVIDIA's August 26 call, describing a 20-year site:

> "The LPS commitment secures a long-lived AI factory site, while the NVIDIA compute within the data center can be upgraded repeatedly."

**That sentence is the difference between Burry's story and this one.** The lessor's durable asset is the powered site. The chip is the part it refreshes, and every refresh is a sale for NVIDIA. CoreWeave made the same point from the lender's side on August 11, saying it has "built a business whose economics do not rely on recontracting after initial customer term." The old chip does not need to hold its rent for the building to keep earning. It needs to be replaced.

And NVIDIA prices each replacement higher. Its revenue opportunity per gigawatt of deployed power has gone from about $18 billion with Hopper to $25 billion with Blackwell to $40 billion with Rubin, and the roadmap slide carries it to $60 billion with Feynman [NVIDIA investor presentation, Sept 2026 — confirm deck/date]. That is what NVIDIA sells per gigawatt, which means it is what a neocloud spends per gigawatt to upgrade. The building persists; the bill for filling it goes up every generation.

[C3: $/GW by generation — Hopper $18B, Blackwell $25B, Rubin $40B, Feynman $60B, with NVIDIA's rising capex share of the top-5 CSPs on a second axis.]

## But only if the money keeps coming

Here is where the building thesis stops being a complete answer and hands off.

A neocloud can only swap a new chip into its building if it can pay for the chip, either out of its own cash or with a new loan. Paying out of cash requires the renters to keep paying it. Raising a new loan requires a lender to believe the renters will keep paying. Either way the upgrade cycle, the thing that keeps NVIDIA selling after the shortage, runs on the same fuel as everything else: money coming in from whoever is renting the compute. The durable building does not break the chain. It just moves the question one link down, to who pays.

The clouds have built real machinery for this, and it mostly works. Nebius says its customers prepay 50% to 60% of the capital cost, and it expects more than $9 billion of prepayments in 2026. CoreWeave funds most of its fleet through per-contract loans that are repaid inside the customer's own contract, so that, in its CFO's words, "when an initial contract ends, the cluster no longer has any leverage." Re-renting the old chip is upside, not survival. That is the strong version of the structure, and it is why the neoclouds were not the ones that blew up in the July selloff.

The weak version is the part Burry is describing, and it exists. CoreWeave's DDTL 5.5, a $2.6 billion loan it closed on August 10, runs about five years against customer contracts that average about three. For the last two years, the lenders get paid only if CoreWeave finds new tenants for those GPUs at a decent rent. It priced at SOFR plus 5.50%, about 10.4% all in, a full point wider than the same loan three months earlier at the same credit ratings. The cost of carrying renewal risk is rising, and CoreWeave's five-year credit default swap sat at 8.2% on October 2, about two and a half times a year earlier. The credit market is not hiding this risk. It is charging for it. But the charge is landing at the company level, not inside the contract-backed loans, which is a very different thing from 2006.

So the upgrade cycle is financeable today, at a rising price. Whether it stays financeable is a question about the renters, and the renters are the labs.

## Who pays for the tokens

Start with who buys NVIDIA's chips, because it is more concentrated than the headline suggests. In its latest 10-Q, NVIDIA discloses that five direct customers made up 22%, 14%, 13%, 11% and 10% of its receivables, which is 70% from five accounts. A quarter earlier, three customers were 56%. The buyers are concentrating, not diversifying.

Those direct customers are mostly the clouds. The clouds' own revenue is concentrated one layer further, in the labs. Eisman's claim, which I could not source to a filing, is that about 70% of the hyperscalers' AI revenue comes from OpenAI and Anthropic. What I can source points the same way: CoreWeave's S-1 shows 62% of its 2024 revenue came from Microsoft, and Oracle's cloud backlog is reportedly about half OpenAI. Stack the two layers and you get the real picture. NVIDIA sells to a handful of clouds, and those clouds sell to a handful of labs. The demand narrows as you follow the money down.

Kress named the exposure on the August 26 call. The AI labs "for which we expect to leverage our balance sheet" are, she said, roughly a quarter of NVIDIA's business next year. That is the layer NVIDIA is backing directly, through equity stakes, through the $105 billion Ohio lease it guarantees for OpenAI, and through the land, power and shell guarantees in the 10-Q. A quarter of the business leans on companies that do not yet make money.

How much money the labs make depends on something the bulls and bears both misread: tokens. The usual bull argument is that token volume is exploding, so demand is safe. Google reported 1,300 trillion tokens a month across its surfaces; OpenRouter traffic is up many times over. The usual bear argument is that token prices are collapsing, so revenue must be collapsing too. Silicon Data's token-price index more than halved, from about $2.06 in late May to $0.97 on October 1, while GPU rent held roughly flat.

[C1: token-price index vs H100/B200 rent — the halving while rent held.]

Both arguments measure the wrong thing. Revenue is price times volume, and neither side times the other. Two things break the clean arithmetic. First, each model generation cuts the price of a given capability by about five times. OpenAI's own pricing page puts GPT-6.1 Sol at $2 per million input tokens and $10 output, against GPT-6 Astra at $10 and $50, and describes it as "near-Astra intelligence for a fifth of the price." On that number alone, usage would have to grow five times per generation just to hold revenue. But the second thing cuts the other way: the newer models are reasoning models, and they burn far more tokens to do the same job. So a chunk of the volume growth is mechanical, the same task costing more tokens, not new paying demand. And a large share of the tokens, over 85% of agent tokens by one count, are cached and priced about 95% below standard. Token counts are inflated from both ends.

The honest conclusion is that you cannot read demand off either the price or the count. You have to look at what the labs actually take in against what they have promised to spend. That is why October 8 moved the tape and a trillion tokens a month did not. OpenAI keeps about $50 billion a year today, against projected cash burn above $600 billion through 2030 and a funding round it is still trying to close, reportedly about $30 billion at a $1.4 trillion valuation. Anthropic, on the prospectus Reuters has seen, did $4.6 billion of revenue in 2025 against an operating loss above $8 billion. The spend is real and contracted years out. The revenue that has to service it is a fraction of it, and it belongs to two companies.

**This is where Eisman and I agree, and where I part from him.** He is right that the whole build rests on a couple of labs that do not make money. But "the labs" and "compute demand" are not the same risk. The thing that threatens the labs, no moats and a drift to open-weight models, hurts the labs' economics. It does not make the compute go away, because open models still run on GPUs and cheaper models pull in more use. The risk to NVIDIA does not run through tokens disappearing. It runs through financing: whether the companies that sign the multi-year contracts can keep paying them. That is a narrower claim than Eisman's, and it is testable.

There is a circular version of this that NVIDIA funds the labs that buy its compute. The 10-Q shows NVIDIA has committed to equity investments in "AI model makers, infrastructure financiers, and other private companies," on top of roughly $99 billion of equity investments on its books [confirm total]. Huang's answer at Goldman Sachs was that "the circular part of it doesn't make much sense to me because the number shows it doesn't." I would hold him to the number. The circularity is a real exposure, sized in the ledger below, not a reason the whole thing is a fraud.

One risk sits outside this post entirely. The labs could be forced to slow down, not by economics but by a catastrophic AI event and the regulation that would follow it. Both OpenAI and Anthropic are now openly gaming out that scenario. I cannot put a number on it, so it is not in my ledger, and it is the subject of a separate post. Here I am pricing the money, not the politics.

## What the multiple is already pricing

The strange part of this trade is that the stock is not priced for the bull case. NVIDIA trades at about 14.81x next-twelve-months EV/EBITDA, down from 32.44x a year ago, even as the business accelerated to 106% revenue growth and guided to a first-ever full-year number. Microsoft, growing far slower, trades at 16.81x. The de-rating has already happened.

That matters because Burry's puts do not strictly need rent to fall. If the market decides to price the end of the shortage early, the multiple can compress on its own. You can watch the mechanism live in memory. Samsung guided to a record quarterly operating profit near $80 billion on October 8, its fourth straight record, and the stock is down more than 25% from its June high. Micron trades at 6.1x forward earnings and Samsung at 4.2x, the way markets price a business they think is near its peak. The market is not waiting for earnings to fall. It is selling the slowdown in growth.

Two different forces could pull NVIDIA's multiple down, and they are worth separating. One is the discount rate: the 10-year Treasury yield was 5.23% on October 8, and a higher rate lowers the value of distant earnings. But at about 16.5x forward earnings, NVIDIA is not priced as a 2035 story. Most of its value is near-term earnings, so rising rates should hit it less than a 40x software name. The other force is the cycle: whether this decade's earnings hold after the shortage. That is the real question for NVIDIA, and it is the who-pays question in a different hat. Micron at 6.1x is the market pricing the cycle at its extreme. NVIDIA at 14.81x is the market pricing some of it already.

## Break conditions

Rules 1 to 5 carry forward from my August 28 earnings post. Rules 6 to 9 are from my October 5 post. I grade each as written, not as reinterpreted after the data arrives.

| # | Rule | Threshold | Action | Status (Oct 11) |
|---|------|-----------|--------|-----------------|
| 1 | Non-GAAP gross margin below 72%, two consecutive quarters, Vera Rubin ramp | <72% x2 | Exit review | Not triggered. Q2 75.0%; Q4 guided 71–72%; one quarter below is guided, so Q1 FY28 is the test. |
| 2 | ACIE/Hyperscale split reversing | Hyperscale reaccelerates while ACIE decelerates | Exit review | Not triggered. ACIE +25% q/q vs Hyperscale +13%. |
| 3 | Hyperscaler frames custom silicon as primary training compute, two calls, plus sequential Hyperscale decline | As stated | Exit review | Not triggered. |
| 4 | Vera CPU shipments delayed beyond Q1 FY2028 | As stated | Exit review | Not triggered. Shipping to lead partners. |
| 5 | FY2028 revenue guide walked back below 60% growth | <60% | Exit review | Not triggered. Guided 70%. |
| 6 | GPU rent: Silicon Data B200 index, three consecutive monthly readings before Sep 2027 | <$3.93 review; <$2.85 exit | Review / exit | Not triggered. ~$5.86 on Oct 2. |
| 7 | Memory supply: Micron, Samsung or SK hynix says supply and demand balance in CY2027 | As stated | Exit review | Not triggered. All three say tighter in 2027. |
| 8 | Lessor stress reaches the order book: ACIE revenue declines q/q | q/q decline | Exit review | Not triggered. +25% q/q in Q2. |
| 9 | NVIDIA records a payment or loss under AI cloud, land/power/shell, SB Energy or residual-value support | Any | Review and resize | Not triggered. |

Three candidate rules I am weighing for this post, and want reader input on before I set them:

- **Lab revenue.** OpenAI net annualized revenue below $70 billion at the end of 2026, the figure it has guided to during its raise. A clean "who pays" test. The objection is that it is a private number I cannot audit.
- **Token spend.** The Silicon Data token-price index below a set level for three months, paired with a decline in disclosed lab or inference revenue. The objection is that price alone is the wrong measure, for the reasons above.
- **Lab share.** NVIDIA's AI-lab share of the business, which Kress put at roughly a quarter, falling on two consecutive calls. The objection is that a fall could be good news, if the hyperscalers are growing faster.

## The close

Burry rolled his puts to September 2027, toward the supply wave where the memory argument runs out. When supply does catch up, what decides NVIDIA is not what the old chips are worth. It is whether the renters can keep paying for the new ones, and on October 8 the market showed the order it checks that in: the labs first, the clouds next, NVIDIA last.

I am still holding NVIDIA. The thing that would change that is not a fall in GPU rent. It is a fall in what the AI labs can spend. So the question I would put to you is the one I am watching myself: which of those two do you think moves first?

---

*Disclosure: I hold a position in NVIDIA. This material is for informational purposes only and does not constitute investment advice. Sources: [to compile — NVIDIA Q2 FY27 10-Q (Notes 7, 10); NVIDIA Q2 FY27 earnings call, Aug 26, 2026; NVIDIA investor presentation, Sept 2026; Microsoft Q4 FY26 earnings call, Jul 29, 2026, and FY26 10-K; Silicon Data indices, accessed Oct 2026; Micron Q4 FY26 call, Sep 30; Samsung prelim Q3, Oct 8; CoreWeave Q2 call and 8-K, Aug 2026; Nebius Q2 call, Aug 12; Huang at Goldman Sachs, Sep 10; Eisman, Oct 2; OpenAI pricing page; prospectus figures via Reuters.]*
