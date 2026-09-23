"""Constrained high-complexity search in the four C=11 chambers.

Discovers the four C=11 chamber signatures from the 10-wall arrangement, then
samples/optimizes only inside those chambers. Objective = actual physical
sign-changing zeros of kappa3, not coefficient variation.

Exploratory until a candidate is rationalized + interval certified.
"""
import itertools, numpy as np
from scipy.optimize import linprog, differential_evolution

LINES=np.array([(0,2,-1),(1,-2,1),(1,1,-1),(1,2,-2),(1,2,-1),
 (2,-2,1),(2,-1,0),(2,0,-1),(2,1,-2),(2,1,-1)],float)

def wall_sig(u,v):
    z=LINES[:,0]+LINES[:,1]*u+LINES[:,2]*v
    return tuple(np.sign(z).astype(int))

def triple(a,b,c): return (a-2*b+c)*(a+b-2*c)*(2*a-b-c)
def atoms(u,v):
    x=[0.,1.,u,v]; out=[]
    for i in range(4):
      for j in range(4):
       if i!=j: out.append((2*x[i]+x[j],np.sign((x[j]-x[i])**3)))
    for I in itertools.combinations(range(4),3):
      z=[x[i] for i in I]; out.append((sum(z),np.sign(triple(*z))))
    return sorted(out)
def variation(u,v):
    a=atoms(u,v); s=[q[1] for q in a]
    return sum(x!=y for x,y in zip(s,s[1:]))

def feasible(sig,eps=1e-5):
    A=[[-1,0],[1,-1]]; b=[-1-eps,-eps]
    for sg,(a,bu,bv) in zip(sig,LINES):
      A.append([-sg*bu,-sg*bv]); b.append(sg*a-eps)
    return linprog([0,0],A_ub=A,b_ub=b,bounds=[(None,None),(None,None)],method="highs")

C11=[]
for sig in itertools.product((-1,1),repeat=10):
    r=feasible(sig)
    if r.success and variation(*r.x)==11: C11.append((sig,r.x))
assert len(C11)==4

T=np.unique(np.r_[np.linspace(1.000001,10,3500),np.geomspace(10,250,5000)])
def k3grid(u,v,lr):
    x=np.array([0.,1.,u,v]); r=np.exp(np.r_[0.,lr])
    z=r[:,None]*np.exp(-x[:,None]*T); q=z/z.sum(0)
    mu=(q*x[:,None]).sum(0)
    return (q*(x[:,None]-mu)**3).sum(0)
def count(u,v,lr):
    y=k3grid(u,v,lr); s=np.sign(y); s[s==0]=1
    return int(np.sum(s[:-1]*s[1:]<0))

# penalty keeps geometry in requested chamber
def obj(z,sig):
    u=1+np.exp(z[0]); v=u+np.exp(z[1])
    if wall_sig(u,v)!=sig: return 100.0
    return -count(u,v,z[2:5])

if __name__=="__main__":
  print("C11 chambers",len(C11))
  for ci,(sig,wit) in enumerate(C11,1):
    print("CHAMBER",ci,"signature",sig,"LP witness",wit)
    best=(-1,None)
    for seed in range(12):
      res=differential_evolution(lambda z:obj(z,sig),
        [(-3,3),(-3,3),(-9,9),(-9,9),(-9,9)],
        seed=1000*ci+seed,popsize=18,maxiter=220,polish=False)
      z=res.x; u=1+np.exp(z[0]); v=u+np.exp(z[1])
      n=count(u,v,z[2:5]) if wall_sig(u,v)==sig else -1
      if n>best[0]: best=(n,(u,v,np.exp(np.r_[0.,z[2:5]])))
    print("BEST",best)
