"""Enumerate rate-order signatures for four information levels.

Normalization: x=(0,1,u,v), 1<u<v.
This script constructs all 16 pair/triple rates, finds feasible equality
lines, samples the admissible wedge, and records rate-order/sign signatures.

It is exploratory enumeration. A manuscript theorem requires exact cell
enumeration/certification.
"""
import itertools, math
import numpy as np
from scipy.optimize import linprog

XCOEF=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]

def add(A,B,mA=1,mB=1):
    return tuple(mA*A[k]+mB*B[k] for k in range(3))

RATES=[]
for i in range(4):
    for j in range(4):
        if i!=j:
            RATES.append((f"P{i+1}{j+1}",add(XCOEF[i],XCOEF[j],2,1)))
for C in itertools.combinations(range(4),3):
    RATES.append(("T"+''.join(str(i+1) for i in C),
                  tuple(sum(XCOEF[i][k] for i in C) for k in range(3))))

def normalize_line(d):
    g=0
    for z in d: g=math.gcd(g,abs(z))
    d=tuple(z//g for z in d)
    for z in d:
        if z:
            return tuple(-q for q in d) if z<0 else d

def feasible_lines():
    lines=set()
    for (_,r1),(_,r2) in itertools.combinations(RATES,2):
        d=tuple(r1[k]-r2[k] for k in range(3))
        if d!=(0,0,0): lines.add(normalize_line(d))
    valid=[]
    for A,B,C in lines:
        res=linprog([0,0],A_ub=[[-1,0],[1,-1]],
                    b_ub=[-1.000001,-0.000001],
                    A_eq=[[B,C]],b_eq=[-A],
                    bounds=[(None,None),(None,None)],method="highs")
        if res.success: valid.append((A,B,C))
    return sorted(valid)

def rate_value(r,u,v):
    a,b,c=r
    return a+b*u+c*v

def triple_c(a,b,c):
    return (a-2*b+c)*(a+b-2*c)*(2*a-b-c)

def coefficient_signs(u,v):
    x=[0,1,u,v]; out=[]
    for name,_ in RATES:
        if name.startswith("P"):
            i,j=int(name[1])-1,int(name[2])-1
            val=(x[j]-x[i])**3
        else:
            inds=[int(z)-1 for z in name[1:]]
            val=triple_c(*[x[i] for i in inds])
        out.append(np.sign(val))
    return out

def signature(u,v):
    vals=[rate_value(r,u,v) for _,r in RATES]
    order=tuple(np.argsort(vals))
    signs=coefficient_signs(u,v)
    seq=[signs[i] for i in order]
    changes=sum(a!=b for a,b in zip(seq,seq[1:]))
    return order,changes,''.join('+' if z>0 else '-' for z in seq)

if __name__=="__main__":
    print("16 rates:")
    for item in RATES: print(item)
    print("\nFeasible equality lines A+B*u+C*v=0:")
    for line in feasible_lines(): print(line)

    rng=np.random.default_rng(2)
    found={}
    for _ in range(200000):
        u=1+10**rng.uniform(-3,1)
        v=u+10**rng.uniform(-3,1.3)
        order,changes,seq=signature(u,v)
        found[order]=(u,v,changes,seq)

    hist={}
    for _,(_,_,c,_) in found.items(): hist[c]=hist.get(c,0)+1
    print("\nSampled generic rate-order chambers:",len(found))
    print("Variation histogram:",dict(sorted(hist.items())))
    print("Maximum sampled variation:",max(hist))
