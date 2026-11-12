"""Latest earnings release (8-K item 2.02, ex. 99.1) for each ticker: save full text to /tmp/sec_cache/rel_TICK.txt
and print the headline lines plus lines matching mechanism keywords. Usage: python3 np2_release.py [-n LINES] TICK..."""
import sys, re, os
os.environ.setdefault("SEC_CACHE", "/tmp/sec_cache")
import secutil as s
KW = re.compile(r'(?i)backlog|book-to-bill|remaining performance|guidance|outlook|contract value|annual(ized)? recurring|\bARR\b|recurring revenue|minimum volume|repurchas|organic|net leverage|awards|record|fiscal (year )?202[78]|full[- ]year')
def run(tk, n=24, idx=0):
    rl = s.releases(tk, n=6)
    if not rl: print(f"\n=== {tk}: no 2.02 8-K"); return
    f = rl[idx]; t = s.exhibit99(f) or ''
    open(f"/tmp/sec_cache/rel_{tk}_{idx}.txt", 'w').write(t)
    lines = [l.strip() for l in t.split('\n') if len(l.strip()) > 40]
    print(f"\n=== {tk} filed {f['filed']} period {f['period']} {f['base']} ({len(t)//1000}k chars)")
    out = []; seen = set()
    for l in lines[:10]: out.append(l)
    for l in lines[10:160]:
        if KW.search(l) and '|' not in l[:60] and l[:50] not in seen: out.append(l); seen.add(l[:50])
    for l in out[:n]: print('  ' + l[:260])
if __name__ == "__main__":
    a = sys.argv[1:]; n = 24
    if a[0] == '-n': n = int(a[1]); a = a[2:]
    for tk in a:
        try: run(tk, n)
        except Exception as e: print(tk, 'ERR', e)
