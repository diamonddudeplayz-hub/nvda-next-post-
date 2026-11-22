# Independent rebuild of the GOOGL reverse-DCF, with terminal-value decomposition
price=265.29; shares=12294.0; netcash=115.0
mkt=price*shares/1000
EV=mkt-netcash
print(f"Price ${price} | Shares {shares:,.0f}M | Mkt cap ${mkt:,.0f}B | Net cash ${netcash}B | EV ${EV:,.0f}B\n")

# ---- SOURCE DATA (LSEG via TIKR, pulled 22-Nov-2026) ----
# OCF consensus (file 2)  n=28,27,22,5,4
OCF={2025:164.7,2026:196.5,2027:276.6,2028:363.6,2029:444.5,2030:525.0}
# Direct CAPEX consensus (file 11)  n=29,29,26,8,7  -> the LOW-capex / high-FCF path
CAPX_direct={2025:91.4,2026:200.8,2027:327.4,2028:375.5,2029:313.1,2030:297.9}
# LSEG FCF file (file 4) -> implies capex = OCF - FCF
FCF_file={2025:73.3,2026:-20.0,2027:-60.7,2028:-32.0,2029:64.4,2030:140.6}
CAPX_fcffile={y: OCF[y]-FCF_file[y] for y in OCF}

print("Implied capex by source, 2027-2030 ($B):")
print(f"{'Year':6}{'DirectFile':>12}{'FCFfile(OCF-FCF)':>18}{'Gap':>8}")
for y in (2027,2028,2029,2030):
    print(f"{y:<6}{CAPX_direct[y]:>12,.0f}{CAPX_fcffile[y]:>18,.0f}{CAPX_fcffile[y]-CAPX_direct[y]:>8,.0f}")
print()

def run(CAPX, label, og_term=0.06, capex_grow=0.07, disc=0.10, g=0.03,
        capx_ext_mode='flat7', verbose=False):
    """Build explicit FCF 2027-2036, TV off 2036. Return pershare + TV share."""
    ocf=dict(OCF); capx=dict(CAPX)
    # extend OCF 2031-2036 decelerating to terminal
    og=[0.13,0.11,0.10,0.09,0.08,og_term]
    o=ocf[2030]
    for i,y in enumerate(range(2031,2037)):
        o*=(1+og[i]); ocf[y]=o
    # extend capex 2031-2036
    c=capx[2030]
    for i,y in enumerate(range(2031,2037)):
        if capx_ext_mode=='flat7':
            c*=(1+capex_grow)
        elif capx_ext_mode=='track_ocf':   # capex stays a constant % of OCF (no roll-off)
            c=ocf[y]* (capx[2030]/ocf[2030])
        capx[y]=c
    FCF={y:ocf[y]-capx[y] for y in ocf}
    pv=sum(FCF[y]/(1+disc)**(i+1) for i,y in enumerate(range(2027,2037)))
    tv=FCF[2036]*(1+g)/(disc-g)
    pvtv=tv/(1+disc)**10
    val=(pv+pvtv+netcash)/shares*1000
    tv_share=pvtv/(pv+pvtv)
    if verbose:
        print(f"  [{label}] FCF path 2027-2036:", " ".join(f"{FCF[y]:.0f}" for y in range(2027,2037)))
        print(f"  explicit PV ${pv:,.0f}B | PV(TV) ${pvtv:,.0f}B | TV={tv_share*100:.0f}% of EV")
    return val, tv_share, FCF

print("="*70)
print("A) REPRODUCE author's base (direct capex, 10% WACC, 3% g):")
v,tvs,_=run(CAPX_direct,'author', disc=0.10, g=0.03, verbose=True)
print(f"  -> Fair value ${v:,.0f}/sh   (author reported $339)   TV share {tvs*100:.0f}%\n")

print("B) Same but FCF-file capex (capex stays elevated ~380B):")
v,tvs,_=run(CAPX_fcffile,'fcffile', disc=0.10, g=0.03, verbose=True)
print(f"  -> Fair value ${v:,.0f}/sh   TV share {tvs*100:.0f}%\n")

print("C) Capex NEVER rolls over (tracks OCF at 2030 ratio ~57%), 10% WACC:")
v,tvs,_=run(CAPX_direct,'noRoll', disc=0.10, g=0.03, capx_ext_mode='track_ocf', verbose=True)
print(f"  -> Fair value ${v:,.0f}/sh   TV share {tvs*100:.0f}%\n")

print("="*70)
print("D) TERMINAL-VALUE DOMINANCE across WACC (direct capex, g=3%):")
for d in (0.09,0.10,0.11,0.12):
    v,tvs,_=run(CAPX_direct, 'x', disc=d, g=0.03)
    print(f"  WACC {d*100:.0f}%: FV ${v:,.0f}  | terminal value = {tvs*100:.0f}% of EV")

print("\nE) FAIR-VALUE GRID — direct-capex path (the bull primary):")
print("WACC\\g     2.5%    3.0%    3.5%")
for d in (0.09,0.10,0.11,0.12):
    row=[run(CAPX_direct,'x',disc=d,g=gg)[0] for gg in (0.025,0.03,0.035)]
    print(f"{d*100:.0f}%    "+"  ".join(f"${x:6,.0f}" for x in row))

print("\nF) FAIR-VALUE GRID — FCF-file path (capex stays elevated):")
print("WACC\\g     2.5%    3.0%    3.5%")
for d in (0.09,0.10,0.11,0.12):
    row=[run(CAPX_fcffile,'x',disc=d,g=gg)[0] for gg in (0.025,0.03,0.035)]
    print(f"{d*100:.0f}%    "+"  ".join(f"${x:6,.0f}" for x in row))
