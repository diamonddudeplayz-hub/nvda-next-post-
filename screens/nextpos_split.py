"""Product vs service/recurring revenue and gross margin by quarter, from the income-statement
R-page of each 10-Q/10-K (the split is dimensional, so it is not in companyfacts).
Q4 = fiscal year minus nine months. Usage: python3 nextpos_split.py TICKER [n_filings] [--raw]
"""
import sys, re, json
import secutil as s

REC = r'service|recurring|subscription|software|maintenance|rental|consumable|aftermarket|support|leas|saas|license|parts'
def classify(label, ctx, member=''):
    l = (ctx + ' | ' + label).lower()
    kind = 'cost' if re.search(r'cost', l) else 'rev'
    if (re.search(r'total|^revenues?$|net sales$|^net revenues?$|^sales$', label.lower().strip()) and not ctx) or (label.lower().startswith('total') and not member): cat = 'total'
    elif re.search(REC, l): cat = 'svc'
    elif re.search(r'product|equipment|hardware|system|goods|device|instrument', l): cat = 'prod'
    else: cat = 'total' if re.search(r'total|revenue|sales', l) else 'other'
    return kind, cat

def parse(f):
    title, hdr, rows = s.income_statement(f)
    if not rows: return None
    out = []; member = ''; sub = ''
    stop = False; seen_member = False
    for label, vals in rows:
        if label == 'X': break
        ll = label.lower()
        if len(vals) == 5 and vals[0] is None: vals = vals[1:]
        nums = [v for v in vals if v is not None]
        if not nums:
            # header row: either a dimension member section (Itron style) or a sub-heading
            if re.search(r'^(revenues?|net sales|sales|net revenues?|cost|costs? of|operating expenses|cost of revenues?|cost of sales).*', ll) and not re.search(REC + '|product', ll.split(':')[0]) :
                sub = label
            else:
                member = label; sub = ''; seen_member = True; stop = False
            if re.search(r'operating expenses|other income|per share|weighted', ll): stop = True
            continue
        if re.search(r'gross (profit|margin)|operating expenses|total operating|research|selling|general', ll):
            stop = True
        if stop: continue
        kind, cat = classify(label, (member + ' | ' + sub).strip(' |'), member)
        out.append(dict(label=label, ctx=(member + ' | ' + sub).strip(' |'), kind=kind, cat=cat, vals=vals))
    return dict(form=f['form'], period=f['period'], filed=f['filed'], hdr=hdr, rows=out)

def series(ticker, n=14, raw=False):
    fl = s.filings(ticker, n=n)
    recs = []
    for f in fl:
        p = parse(f)
        if not p: continue
        if raw:
            print(p['form'], p['period'], p['hdr'][1:])
            for r in p['rows']: print('   ', r['kind'], r['cat'], '|', r['ctx'], '|', r['label'], r['vals'])
        ncol = max(len(r['vals']) for r in p['rows']) if p['rows'] else 0
        agg = {}
        for r in p['rows']:
            if r['cat'] in ('prod', 'svc', 'total'):
                v = r['vals']
                q = v[0]; ytd = v[2] if (p['form'] == '10-Q' and len(v) >= 4) else v[0]
                k = (r['kind'], r['cat'])
                if r['cat'] == 'total' and k in agg: continue
                a = agg.setdefault(k, [0, 0]); a[0] += abs(q or 0); a[1] += abs(ytd or 0)
        recs.append(dict(form=p['form'], period=p['period'], agg=agg))
    return recs

def quarters(recs):
    """Turn 10-Q (q, ytd) and 10-K (FY) into quarterly rows, newest first."""
    out = []
    recs = sorted(recs, key=lambda r: r['period'], reverse=True)
    for i, r in enumerate(recs):
        g = lambda k, j: r['agg'].get(k, [None, None])[j]
        row = dict(period=r['period'], form=r['form'])
        for kind in ('rev', 'cost'):
            for cat in ('prod', 'svc', 'total'):
                if r['form'] == '10-Q': row[f'{kind}_{cat}'] = g((kind, cat), 0)
                else:
                    # FY minus 9M YTD from the preceding 10-Q (next in list)
                    prev = next((x for x in recs[i + 1:] if x['form'] == '10-Q'), None)
                    fy = g((kind, cat), 0); y9 = prev['agg'].get((kind, cat), [None, None])[1] if prev else None
                    row[f'{kind}_{cat}'] = (fy - y9) if (fy is not None and y9 is not None) else None
                    row[f'fy_{kind}_{cat}'] = fy
        out.append(row)
    return out

def show(ticker, n=14):
    q = quarters(series(ticker, n))
    print(f"{ticker}: period  form   prodRev  svcRev  svc%   prodGM  svcGM   gap")
    for r in q:
        pr, sr, pc, sc = r.get('rev_prod'), r.get('rev_svc'), r.get('cost_prod'), r.get('cost_svc')
        if not pr or not sr: print(' ', r['period'], r['form'], 'no split', {k: v for k, v in r.items() if k.startswith('rev')}); continue
        pg = 1 - pc / pr if pc else float('nan'); sg = 1 - sc / sr if sc else float('nan')
        print(f"  {r['period']} {r['form']:5s} {pr:10,.0f} {sr:9,.0f} {sr/(pr+sr)*100:5.1f}% {pg*100:6.1f}% {sg*100:6.1f}% {(sg-pg)*100:5.1f}")
    return q

if __name__ == "__main__":
    tk = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 14
    if '--raw' in sys.argv: series(tk, n, raw=True)
    else: show(tk, n)
