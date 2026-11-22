price=265.29; shares=12294.0; netcash=115.0
mkt=price*shares/1000
print(f"Mkt cap ${mkt:,.0f}B | net cash ${netcash}B\n")
# OCF consensus (LSEG, reliable n=22-28)
OCF={2026:196,2027:277,2028:364,2029:444,2030:525}
# DIRECT capex consensus (LSEG, from the uploaded file)
CAPX={2026:201,2027:327,2028:375,2029:313,2030:298}
# extend: OCF 14->7%, capex resumes modest ~7%/yr from 2030 base
og=[0.14,0.12,0.10,0.09,0.08,0.07]; cg=[0.07,0.07,0.07,0.07,0.07,0.07]
o=OCF[2030]; c=CAPX[2030]
for i,y in enumerate(range(2031,2037)):
    o*= (1+og[i]); c*=(1+cg[i]); OCF[y]=o; CAPX[y]=c
FCF={y:OCF[y]-CAPX[y] for y in OCF}
print("Yr    OCF  Capex   FCF   (FCF = OCF - direct capex)")
for y in range(2027,2037): print(f"{y} {OCF[y]:6.0f} {CAPX[y]:6.0f} {FCF[y]:7.0f}")
print("  [memo: LSEG 'FCF' file had 2027 -61 / 2029 +64 — lower, because it also nets finance leases;")
print("   OCF-minus-capex is the textbook FCF and the cleaner number. Truth ~ in between.]")

def dcf(disc,g):
    pv=sum(FCF[y]/(1+disc)**(i+1) for i,y in enumerate(range(2027,2037)))
    tv=FCF[2036]*(1+g)/(disc-g); pv+=tv/(1+disc)**10
    return (pv+netcash)/shares*1000
print("\n== Fair value per share (direct-capex path) ==")
print("WACC\\g    2.5%    3.0%    3.5%")
for d in [0.09,0.10,0.11]:
    print(f"{d*100:.0f}%   "+"  ".join(f"${dcf(d,g):6.0f}" for g in [0.025,0.03,0.035]))
print("\n== Reverse: terminal g implied by $265.29 ==")
for d in [0.09,0.10,0.11]:
    lo,hi=-0.08,0.08
    for _ in range(60):
        mid=(lo+hi)/2
        if dcf(d,mid)<price: lo=mid
        else: hi=mid
    print(f"  WACC {d*100:.0f}%: implied terminal growth = {mid*100:.1f}%")
