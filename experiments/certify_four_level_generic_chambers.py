"""Finite certificate for the generic four-level chamber arrangement.

Enumerates all 2^10 wall-sign vectors.  Each feasible set is convex, hence a
feasible sign vector is one chamber.  Also computes the coefficient-sign
variation in each chamber.

A separate boundary audit is required for points on one or more walls.
"""
import itertools, math
import numpy as np
from scipy.optimize import linprog

LINES=[
 (0,2,-1),(1,-2,1),(1,1,-1),(1,2,-2),(1,2,-1),
 (2,-2,1),(2,-1,0),(2,0,-1),(2,1,-2),(2,1,-1)
]

def feasible(sig, eps=1e-7):
    A=[[-1,0],[1,-1]]
    b=[-1-eps,-eps]
    for sg,(a,bu,bv) in zip(sig,LINES):
        A.append([-sg*bu,-sg*bv])
        b.append(sg*a-eps)
    return linprog([0,0],A_ub=A,b_ub=b,bounds=[(None,None),(None,None)],
                   method="highs")

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
    return sum(a!=b for a,b in zip(signs,signs[1:])),aa

if __name__=="__main__":
    chambers=[]
    for sig in itertools.product((-1,1),repeat=10):
        r=feasible(sig)
        if r.success:
            u,v=r.x
            C,aa=variation(u,v)
            chambers.append((sig,u,v,C))
    hist={}
    for *_,C in chambers: hist[C]=hist.get(C,0)+1
    print("feasible generic chambers =",len(chambers))
    print("variation histogram =",dict(sorted(hist.items())))
    print("max generic variation =",max(hist))
    assert len(chambers)==24
    assert hist=={5:12,7:6,9:2,11:4}
