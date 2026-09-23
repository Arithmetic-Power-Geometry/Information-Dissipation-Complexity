import itertools
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction

LINES=[(0,2,-1),(1,-2,1),(1,1,-1),(1,2,-2),(1,2,-1),
       (2,-2,1),(2,-1,0),(2,0,-1),(2,1,-2),(2,1,-1)]

def feasible(sig,eps=1e-5):
    A=[[-1,0],[1,-1]]; b=[-1-eps,-eps]
    for sg,(a,bu,bv) in zip(sig,LINES):
        A.append([-sg*bu,-sg*bv]); b.append(sg*a-eps)
    return linprog([0,0],A_ub=A,b_ub=b,bounds=[(None,None),(None,None)],method="highs")

def triple(a,b,c):
    return (a-2*b+c)*(a+b-2*c)*(2*a-b-c)

def atoms(u,v):
    x=[0.,1.,u,v]; out=[]
    for i in range(4):
        for j in range(4):
            if i!=j: out.append((2*x[i]+x[j],np.sign((x[j]-x[i])**3),f"P{i+1}{j+1}"))
    for I in itertools.combinations(range(4),3):
        z=[x[i] for i in I]
        out.append((sum(z),np.sign(triple(*z)),"T"+''.join(str(i+1) for i in I)))
    return sorted(out)

def variation(aa):
    z=[a[1] for a in aa]
    return sum(x!=y for x,y in zip(z,z[1:]))

rows=[]
for sig in itertools.product((-1,1),repeat=10):
    r=feasible(sig)
    if r.success:
        u,v=r.x; aa=atoms(u,v)
        rows.append((variation(aa),u,v,sig,aa))
rows.sort(key=lambda z:(-z[0],z[1],z[2]))
print("id,C,u,v,wall_signature,ordered_atom_signs")
for k,(C,u,v,sig,aa) in enumerate(rows,1):
    uf=Fraction(u).limit_denominator(10000); vf=Fraction(v).limit_denominator(10000)
    signs=' '.join(('+' if s>0 else '-')+name for _,s,name in aa)
    ws=''.join('+' if z>0 else '-' for z in sig)
    print(f"C{k:02d},{C},{uf},{vf},{ws},{signs}")
