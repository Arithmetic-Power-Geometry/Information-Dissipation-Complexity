"""Direct six-zero feasibility search for four information levels.

Unknowns include scale-aware geometry, multiplicity ratios, and six ordered
physical times. Objective is simultaneous kappa3(t_j)=0.

IMPORTANT: failure to solve is not an impossibility proof.
"""
import numpy as np
from scipy.optimize import least_squares

def unpack(z):
    a=np.exp(z[0]); u=1+np.exp(z[1]); v=u+np.exp(z[2])
    x=a*np.array([0.,1.,u,v])
    lr=z[3:6]
    # ordered times via positive increments from 1
    inc=np.exp(z[6:12])
    t=1+np.cumsum(inc)
    return x,lr,t

def k3(t,x,lr):
    r=np.exp(np.r_[0.,lr])
    q=r*np.exp(-t*x); q/=q.sum()
    mu=q@x
    return q@((x-mu)**3)

def residual(z):
    x,lr,t=unpack(z)
    vals=np.array([k3(tt,x,lr) for tt in t])
    # scale-free normalization prevents tiny x from making all cumulants tiny
    span=x[-1]-x[0]
    return vals/(span**3+1e-300)

if __name__=="__main__":
    rng=np.random.default_rng(20260923)
    best=(np.inf,None)
    for trial in range(4000):
        z0=np.r_[rng.uniform(-5,2),rng.uniform(-3,3,2),
                 rng.uniform(-10,10,3),rng.uniform(-3,4,6)]
        sol=least_squares(residual,z0,max_nfev=5000,
            xtol=1e-13,ftol=1e-13,gtol=1e-13)
        norm=np.linalg.norm(residual(sol.x),np.inf)
        if norm<best[0]:
            best=(norm,sol.x.copy())
            x,lr,t=unpack(sol.x)
            print("NEW BEST",norm,"x",x,"r",np.exp(np.r_[0.,lr]),"t",t)
    print("FINAL",best[0])
    if best[1] is not None:
        print(unpack(best[1]))
