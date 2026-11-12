"""Summarize the KBR LSEG Estimate Details exports (12 Nov 2026): per measure, period, # estimates, mean, actual, surprise.
Run from the repo root: python3 kbr/kbr_lseg.py > kbr/lseg_summary.txt"""
import sys, glob, re; sys.path.insert(0, 'screens'); import lseg_read as L
def num(x):
    try: return float(x.replace(',', ''))
    except Exception: return None
def table(f):
    rows = L.read(f)[0][1]
    meas = next(r[2] for r in rows if len(r) > 2 and r[1] == 'Measure'); seg = next((r[2] for r in rows if len(r) > 2 and r[1] == 'Segment'), 'Consolidated')
    hdr = next(r for r in rows if any(re.match(r'(Q\d|FY) \w{3}-\d\d', c) for c in r))
    lab = {r[2]: r for r in rows[:22] if len(r) > 2 and r[2] in ('# Estimates', 'Mean', 'High', 'Low', 'Actual', 'Guidance')}
    out = []
    for j, p in enumerate(hdr):
        if not re.match(r'(Q\d|FY) \w{3}-\d\d', p): continue
        g = lambda k: (lab[k][j] if k in lab and j < len(lab[k]) else '-')
        out.append((p, g('# Estimates'), num(g('Mean')), num(g('Actual')), num(g('High')), num(g('Low')), g('Guidance')))
    brokers = [(r[1], r[2]) for r in rows if len(r) > 3 and r[2] not in ('-', '', 'Current Analyst') and r[1] not in ('', 'Contributor', 'Measure', 'Segment', 'Periodicity', 'Basis Indicator', 'Next Earning Report') and 'Estimate Details' not in r[1]]
    return meas, seg, out, brokers
if __name__ == "__main__":
    for f in sorted(glob.glob('Estimate Details KBR*.xlsx')):
        meas, seg, out, brokers = table(f)
        print(f"\n=== {meas} | {seg} | {f}")
        print("current contributors:", '; '.join(f"{a} ({b})" for a, b in brokers))
        yr = lambda p: int(p[-2:])
        for p, n, m, a, hi, lo, gd in out:
            if yr(p) < 23 and not p.startswith('FY'): continue
            if yr(p) < 19: continue
            s = f"{(a/m-1)*100:+.1f}%" if (a is not None and m) else ''
            print(f"{p:10s} n={n:>3s} mean={m if m is not None else '-':>9} actual={a if a is not None else '-':>9} {s:>7s} hi={hi} lo={lo} {'' if gd in ('-','') else 'guide='+gd}")
