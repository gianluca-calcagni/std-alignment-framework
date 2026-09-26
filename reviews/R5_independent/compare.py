import sys; sys.path.insert(0,'/home/claude/SEALED/t1'); sys.path.insert(0,'/home/claude/blind')
from routing_data import R as RP
from my_routing_FROZEN import R as RM
from collections import Counter
prev={t[0]:t for t in RP}; assert len(prev)==221 and set(prev)==set(RM)
ids=sorted(RM,key=lambda s:(s[0],int(s[1:])))
def kappa(a,b):
    n=len(a); po=sum(x==y for x,y in zip(a,b))/n
    ca,cb=Counter(a),Counter(b); pe=sum(ca[k]*cb[k] for k in set(ca)|set(cb))/n/n
    return po,(po-pe)/(1-pe)
pe=[prev[i][2] for i in ids]
len_=[{'Pt':'P'}.get(RM[i][1],RM[i][1]) for i in ids]
strict=[{'Pt':'N'}.get(RM[i][1],RM[i][1]) for i in ids]
print('prev counts',Counter(pe))
for name,m in [('lenient',len_),('strict',strict)]:
    po,k=kappa(pe,m); print(f'expr {name}: agree {po:.3f} kappa {k:.3f}')
    cm=Counter(zip(pe,m)); print('  prev->mine', {f'{a}->{b}':cm[(a,b)] for a in 'FPN' for b in 'FPN'})
pl=[prev[i][3] for i in ids]; ml=[RM[i][2] for i in ids]
po,k=kappa(pl,ml); print(f'layer: agree {po:.3f} kappa {k:.3f}')
po,k=kappa([prev[i][1] for i in ids],[RM[i][0] for i in ids]); print(f'locus: agree {po:.3f} kappa {k:.3f}')
import random; random.seed(20260924); S=set(random.sample(ids,40))
sub=[i for i in ids if i in S]
for name,m in [('lenient',len_),('strict',strict)]:
    a=[prev[i][2] for i in sub]; b=[m[ids.index(i)] for i in sub]; po,k=kappa(a,b); print(f'T1b-40 expr {name}: {po:.3f} k={k:.3f}')
po,k=kappa([prev[i][3] for i in sub],[RM[i][2] for i in sub]); print(f'T1b-40 layer: {po:.3f} k={k:.3f}')
print('\nprev layer',Counter(pl))
print('\n--- expr disagreements (lenient) ---')
for i in ids:
    a=prev[i][2]; b=len_[ids.index(i)]
    if a!=b: print(f'{i:4} prev {a}/{prev[i][3]:11} mine {RM[i][1]}/{RM[i][2]:11} | prev: {prev[i][4][:95]}')
