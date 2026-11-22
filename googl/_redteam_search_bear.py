# Does "falling TPU cost-to-serve" actually defend the Search margin vs an RPM decline?
# The thesis's central claim. Test the revenue-vs-cost asymmetry.

# ---- Structure (public Alphabet figures, FY2025, labeled) ----
search_ad_pool = 220.0     # "Google Search & other" ad revenue, FY25 (~$198B in '24 +~11%)
# Economics of a Search ad dollar:
tac_rate = 0.21            # traffic acquisition cost (paid to Apple/partners) ~21% of gross ad rev
# Non-TAC cash cost of actually SERVING search (datacenters/compute/people allocated to Search),
# i.e. the thing "cost-to-serve / TPU efficiency" can bend. Deliberately GENEROUS (high) so the
# cost-defense gets its best shot:
serve_cost = 18.0          # $B/yr of Search serving+infra cost (generous upper end)
# => incremental margin on a lost ad dollar (you still save TAC on a click that doesn't happen,
#    but the serving cost is mostly fixed/won't fall with lost revenue):
incr_margin = 1 - tac_rate # ~0.79 drops to operating income when an ad dollar is lost

print("SEARCH-RPM BEAR — revenue-vs-cost asymmetry")
print(f"Search ad pool (FY25): ${search_ad_pool:.0f}B | serving/compute cost (generous): ${serve_cost:.0f}B")
print(f"Revenue-per-query is ~{search_ad_pool/serve_cost:.0f}x the serve-cost-per-query.")
print(f"=> A 1% RPM decline costs ~${search_ad_pool*0.01:.1f}B rev; offsetting it needs a "
      f"{search_ad_pool*0.01/serve_cost*100:.0f}% cut in ALL Search serving cost.\n")

print("The 'TPU defends margin' lever, best case:")
for cut in (0.25,0.50,0.75):
    print(f"  Cut Search serving cost by {cut*100:.0f}% -> saves ${serve_cost*cut:.1f}B of operating income")
print()

# Group anchors for EPS translation (FY27 consensus)
group_OI_fy27 = 180.0      # ~group operating income FY27 (33% margin on ~$545B rev, consistent w/ 10-Q run-rate)
shares = 12294.0
eps_fy27 = 14.88
tax = 0.16
def eps_hit(oi_delta_B):
    ni = oi_delta_B*(1-tax)*1000  # $M
    return ni/shares

print("SCENARIO GRID: share of commercial queries shifting to AI answers (X) x RPM haircut (r)")
print("OI impact ($B, after best-case $9B cost offset) and FY27 EPS / % impact\n")
cost_offset = serve_cost*0.50   # give the bull a GENEROUS 50% serve-cost cut as the 'defense'
print(f"{'':14}" + "".join(f"r={r*100:.0f}%".rjust(16) for r in (0.15,0.30,0.45)))
for X in (0.30,0.50,0.70):
    cells=[]
    for r in (0.15,0.30,0.45):
        rev_hit = search_ad_pool*X*r
        oi_hit  = rev_hit*incr_margin - cost_offset
        oi_hit  = max(oi_hit, -999)
        e = eps_hit(oi_hit)
        pct = oi_hit/group_OI_fy27*100
        cells.append(f"-${oi_hit:4.0f}B {e:+.2f}/{ -pct:+.0f}%")
    print(f"X={X*100:.0f}% comm   " + "".join(c.rjust(16) for c in cells))

print("\nRead: cost offset (${:.0f}B even at a 50% TPU-driven cut) is a rounding error".format(cost_offset))
print("against the revenue hit once RPM falls on a meaningful share of commercial queries.")
print("The margin is defended on the SMALL side (cost) against a risk on the BIG side (revenue).")

# What RPM/volume combo does the market's ~19% FY27 EPS haircut already imply?
print("\nCross-check: the de-rate already prices a ~19% FY27 EPS cut (~$2.8/sh, ~$34B NI, ~$40B OI).")
print("That OI hit corresponds to e.g. X=50% commercial queries at r~45%, or X=70% at r~30% +")
print("some Cloud-margin softness. So a STRUCTURAL RPM break is roughly what $265 already embeds -")
print("i.e. the bear case is not 'unpriced', it's approximately IN the price. The upside needs RPM")
print("to HOLD, which is the one thing nobody can prove today.")
