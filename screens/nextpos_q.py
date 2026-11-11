"""Robust quarterly product/service table for finalists.
Uses only 3-month columns of 10-Qs and FY columns of 10-Ks; Q4 = FY - (Q1+Q2+Q3).
python3 nextpos_q.py TICKER [n_filings]"""
import sys, re, json
import secutil as s, nextpos_split as ns
KEYS = [('rev','prod'),('rev','svc'),('cost','prod'),('cost','svc')]
def collect(tk, n=20):
    Q = {}; FY = {}
    for f in s.filings(tk, n=n):
        p = ns.parse(f)
        if not p: continue
        hdr = [h for h in p['hdr'][1:] if re.search(r'\d{4}', h)]
        for col in range(0, 2 if f['form']=='10-Q' else min(3, len(hdr))):
            a = {}
            for r in p['rows']:
                if r['cat'] in ('prod','svc') and col < len(r['vals']) and r['vals'][col] is not None:
                    a[(r['kind'], r['cat'])] = a.get((r['kind'], r['cat']), 0) + abs(r['vals'][col])
            if not all(k in a for k in KEYS): continue
            if col >= len(hdr): continue
            m = re.search(r'([A-Z][a-z]{2})\. (\d+), (\d{4})', hdr[col]) or re.search(r'([A-Z][a-z]{2})[a-z]* (\d+), (\d{4})', hdr[col])
            if not m: continue
            key = f"{m.group(3)}-{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(m.group(1))+1:02d}"
            (Q if f['form']=='10-Q' else FY).setdefault(key, [a[k] for k in KEYS])
    # derive Q4
    for k, v in FY.items():
        y, mth = int(k[:4]), int(k[5:])
        prev = []
        for back in (3, 6, 9):
            mm = mth - back; yy = y
            while mm <= 0: mm += 12; yy -= 1
            # tolerate 52/53-week drift of one month
            cand = [f"{yy}-{mm:02d}"] + [f"{yy + (1 if mm+d>12 else (-1 if mm+d<1 else 0))}-{((mm+d-1)%12)+1:02d}" for d in (-1, 1)]
            hit = next((Q[c] for c in cand if c in Q), None)
            if hit is None: break
            prev.append(hit)
        if len(prev) == 3 and k not in Q:
            Q[k] = [v[i] - sum(p[i] for p in prev) for i in range(4)]
            Q[k].append('derived')
    return Q, FY
def table(tk, n=20):
    Q, FY = collect(tk, n)
    print(f"{tk}  quarter   prodRev    svcRev  svc%  prodGM  svcGM  gap")
    for k in sorted(Q, reverse=True):
        pr, sr, pc, sc = Q[k][:4]
        print(f"  {k} {pr:10,.0f} {sr:9,.0f} {sr/(pr+sr)*100:5.1f} {100*(1-pc/pr):6.1f} {100*(1-sc/sr):6.1f} {100*((1-sc/sr)-(1-pc/pr)):5.1f} {'(FY-9M)' if len(Q[k])>4 else ''}")
    print("  fiscal years:")
    for k in sorted(FY, reverse=True):
        pr, sr, pc, sc = FY[k]
        print(f"  FY {k} {pr:10,.0f} {sr:9,.0f} {sr/(pr+sr)*100:5.1f} {100*(1-pc/pr):6.1f} {100*(1-sc/sr):6.1f}")
    return Q, FY
if __name__ == "__main__":
    table(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 20)
