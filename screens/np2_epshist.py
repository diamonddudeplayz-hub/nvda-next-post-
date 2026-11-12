"""Non-GAAP EPS history: for each fiscal year-end earnings release (8-K item 2.02) print the lines that carry
adjusted / non-GAAP diluted EPS so each year can be read and cross-checked against the next release's prior-year column.
Usage: python3 np2_epshist.py TICK MONTHS(e.g. 1,2,3) [regex]"""
import sys, re, os
os.environ.setdefault("SEC_CACHE", "/tmp/sec_cache")
import secutil as s
tk = sys.argv[1]; months = [int(x) for x in sys.argv[2].split(',')]
pat = re.compile(sys.argv[3] if len(sys.argv) > 3 else r'(?i)(adjusted|non-gaap)[^|]{0,40}(diluted )?(eps|earnings per (diluted )?share)')
for f in s.filings(tk, forms=("8-K",), n=900):
    if '2.02' not in (f['items'] or '') or int(f['filed'][5:7]) not in months or f['filed'] < '2015-06': continue
    t = s.exhibit99(f) or ''
    hits = []
    for l in t.split('\n'):
        if pat.search(l) and re.search(r'\d\.\d\d', l) and len(hits) < 4: hits.append(re.sub(r'\s+', ' ', l)[:230])
    print(f"## {tk} {f['filed']}"); [print('   ', h) for h in hits]
