"""Finite certificate for the generic four-level chamber arrangement.

Enumerates all 2^10 wall-sign vectors. Each feasible set is convex, hence a
feasible sign vector is one chamber. The representative point is then moved
strictly into the chamber by maximizing a common signed-wall margin, avoiding
numerical representatives that lie effectively on a coefficient-sign wall.
"""
import itertools
import numpy as np
from scipy.optimize import linprog

LINES=[
 (0,2,-1),(1,-2,1),(1,1,-1),(1,2,-2),(1,2,-1),
 (2,-2,1),(2,-1,0),(2,0,-1),(2,1,-2),(2,1,-1)
]

def interior_point(sig):
    # variables (u,v,m), maximize m subject to wedge and signed walls >= m
    # with m <= 1 to make the LP bounded.
    A=[]; b=[]
    # u >= 1+m -> -u + m <= -1
    A.append([-1,0,1]); b.append(-1)
    # v-u >= m -> u-v+m <= 0
    A.append([1,-1,1]); b.append(0)
    for sg,(a,bu,bv) in zip(sig,LINES):
        # sg*(a+bu*u+bv*v) >= m
        A.append([-sg*bu,-sg*bv,1])
        b.append(sg*a)
    A.append([0,0,1]); b.append(1)
    r=linprog([0,0,-1],A_ub=A,b_ub=b,
              bounds=[(None,None),(None,None),(0,None)],method="highs")
    return r

def triple(a,b,c):
    return (a-2*b+c)*(a+b-2*c)*(2*a-b-c)

def atoms(u,v):
    x=[0.,1.,u,v]
    out=[]
    for i in range(4):
        for j in range(4):
            if i!=j:
                out.append((2*x[i]+x[j], np.sign((x[j]-x[i])**3),
                            f"P{i+1}{j+1}"))
    for I in itertools.combinations(range(4),3):
        a,b,c=[x[i] for i in I]
        out.append((a+b+c,np.sign(triple(a,b,c)),
                    "T"+''.join(str(i+1) for i in I)))
    return sorted(out)

def variation(u,v):
    aa=atoms(u,v)
    signs=[z[1] for z in aa]
    assert all(s != 0 for s in signs), "representative is not strictly generic"
    return sum(a!=b for a,b in zip(signs,signs[1:])),aa

if __name__=="__main__":
    chambers=[]
    for sig in itertools.product((-1,1),repeat=10):
        r=interior_point(sig)
        if r.success and r.x[2] > 1e-9:
            u,v,_=r.x
            C,aa=variation(u,v)
            chambers.append((sig,u,v,C))
    hist={}
    for *_,C in chambers:
        hist[C]=hist.get(C,0)+1
    print("feasible generic chambers =",len(chambers))
    print("variation histogram =",dict(sorted(hist.items())))
    print("max generic variation =",max(hist))
    assert len(chambers)==24
    assert hist=={5:12,7:6,9:2,11:4}
