"""Form 4 open-market purchases (code P) and sales (code S) over the last 12 months. python3 nextpos_insiders.py TICKER..."""
import sys, re, json
import secutil as s
def scan(tk, since='2025-11-11'):
    fl = [f for f in s.filings(tk, forms=('4',), n=400) if f['filed'] >= since]
    P = S = 0.0; nP = nS = 0; buyers = set()
    for f in fl:
        idx = s.get(f['base'] + 'index.json')
        if not idx: continue
        x = next((i['name'] for i in json.loads(idx)['directory']['item'] if i['name'].endswith('.xml')), None)
        if not x: continue
        t = s.get(f['base'] + x) or ''
        name = re.search(r'<rptOwnerName>(.*?)</rptOwnerName>', t)
        for tr in re.findall(r'<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>', t, re.S):
            code = re.search(r'<transactionCode>(\w)</transactionCode>', tr)
            sh = re.search(r'<transactionShares>\s*<value>([\d.]+)', tr); px = re.search(r'<transactionPricePerShare>\s*<value>([\d.]+)', tr)
            if not (code and sh and px): continue
            v = float(sh.group(1)) * float(px.group(1))
            if code.group(1) == 'P': P += v; nP += 1; buyers.add((name.group(1) if name else '?', f['filed']))
            if code.group(1) == 'S': S += v; nS += 1
    print(f"{tk}: Forms 4 since {since}: {len(fl)}; open-market buys {nP} (${P/1e6:.2f}M) {sorted(buyers)[:6]}; sales {nS} (${S/1e6:.1f}M)")
if __name__ == "__main__":
    for tk in sys.argv[1:]: scan(tk)
