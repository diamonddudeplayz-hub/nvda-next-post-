"""Ten-year annual fundamentals from SEC companyfacts (10-K 'FY' facts), compact.
python3 nextpos_facts.py TICKER..."""
import sys, json
import secutil as s
TAGS = {
 'rev': ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax'],
 'opinc': ['OperatingIncomeLoss'], 'ni': ['NetIncomeLoss'],
 'eps': ['EarningsPerShareDiluted'], 'dsh': ['WeightedAverageNumberOfDilutedSharesOutstanding'],
 'ocf': ['NetCashProvidedByUsedInOperatingActivities'],
 'capex': ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'sbc': ['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'buyback': ['PaymentsForRepurchaseOfCommonStock'],
}
def annual(tk):
    f = s.facts(tk)['facts'].get('us-gaap', {})
    out = {}
    for k, tags in TAGS.items():
        for tag in tags:
            if tag not in f: continue
            for unit, arr in f[tag]['units'].items():
                for x in arr:
                    if x.get('form') not in ('10-K', '10-K/A') or 'start' not in x: continue
                    from datetime import date
                    d0 = date.fromisoformat(x['start']); d1 = date.fromisoformat(x['end'])
                    if not 350 <= (d1 - d0).days <= 380: continue
                    out.setdefault(x['end'][:7], {}).setdefault(k, x['val'])  # first tag wins; later filings overwrite not
    return out
def show(tk):
    a = annual(tk)
    print(f"{tk}  FYend     rev    opinc     ni   epsDil  dilSh    ocf  capex    fcf    sbc  buyback  (USD m)")
    for k in sorted(a)[-11:]:
        r = a[k]; g = lambda x: (r.get(x) or 0) / 1e6
        print(f"  {k} {g('rev'):8.0f} {g('opinc'):7.0f} {g('ni'):7.0f} {r.get('eps', float('nan')):7.2f} {g('dsh'):7.1f} {g('ocf'):7.0f} {g('capex'):6.0f} {g('ocf')-g('capex'):7.0f} {g('sbc'):6.0f} {g('buyback'):7.0f}")
    return a
if __name__ == "__main__":
    for tk in sys.argv[1:]: show(tk)
