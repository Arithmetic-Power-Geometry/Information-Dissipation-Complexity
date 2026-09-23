"""Scale-aware global search in the four maximal C=11 chambers.

Corrects the earlier chamber search by retaining x=a(0,1,u,v), a>0.
The chamber is determined by (u,v); a controls placement of zeros relative
to the physical boundary t=1.

Objective: actual sign-changing zeros of kappa3(t) on t>1.
Discovery only until rational/integer simplification and interval certification.
"""
import itertools, numpy as np
from scipy.optimize import linprog, differential_evolution

LINES=np.array([(0,2,-1),(1,-2,1),(1,1,-1),(1,2,-2),(1,2,-1),
 (2,-2,1),(2,-1,0),(2,0,-1),(2,1,-2),(2,1,-1)],float)

def sig(u,v):
 z=LINES[:,0]+LINES[:,1]*u+LINES[:,2]*v
 return tuple(np.sign(z).astype(int))

def tri(a,b,c): return (a-2*b+c)*(a+b-2*c)*(2*a-b-c)
def variation(u,v):
 x=[0.,1.,u,v]; A=[]
 for i in range(4):
  for j in range(4):
   if i!=j:A.append((2*x[i]+x[j],np.sign((x[j]-x[i])**3)))
 for I in itertools.combinations(range(4),3):
  z=[x[i] for i in I];A.append((sum(z),np.sign(tri(*z))))
 A.sort(); s=[z[1] for z in A]
 return sum(a!=b for a,b in zip(s,s[1:]))

def feasible(S,e=1e-6):
 A=[[-1,0],[1,-1]];b=[-1-e,-e]
 for q,(c,du,dv) in zip(S,LINES):
  A.append([-q*du,-q*dv]);b.append(q*c-e)
 return linprog([0,0],A_ub=A,b_ub=b,bounds=[(None,None),(None,None)],method="highs")

C11=[]
for S in itertools.product((-1,1),repeat=10):
 r=feasible(S)
 if r.success and variation(*r.x)==11:C11.append(S)
assert len(C11)==4

T=np.unique(np.r_[np.linspace(1.000001,12,4000),np.geomspace(12,1500,12000)])
def count(a,u,v,lr):
 x=a*np.array([0.,1.,u,v]); r=np.exp(np.r_[0.,lr])
 z=r[:,None]*np.exp(-x[:,None]*T); q=z/z.sum(0)
 mu=(q*x[:,None]).sum(0)
 y=(q*(x[:,None]-mu)**3).sum(0)
 s=np.sign(y);s[s==0]=1
 return int(np.sum(s[:-1]*s[1:]<0))

def objective(z,S):
 a=np.exp(z[0]);u=1+np.exp(z[1]);v=u+np.exp(z[2])
 if sig(u,v)!=S:return 100.
 return -count(a,u,v,z[3:6])

if __name__=="__main__":
 for ci,S in enumerate(C11,1):
  best=(-1,None)
  for seed in range(20):
   R=differential_evolution(lambda z:objective(z,S),
      [(-5,2),(-3,3),(-3,3),(-10,10),(-10,10),(-10,10)],
      seed=10000*ci+seed,popsize=22,maxiter=300,polish=False)
   z=R.x;a=np.exp(z[0]);u=1+np.exp(z[1]);v=u+np.exp(z[2])
   n=count(a,u,v,z[3:6]) if sig(u,v)==S else -1
   if n>best[0]:
    best=(n,(a,u,v,np.exp(np.r_[0.,z[3:6]])))
    print("CHAMBER",ci,"NEW BEST",best)
  print("CHAMBER",ci,"FINAL",best)
