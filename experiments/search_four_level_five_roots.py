"""Targeted optimizer for physical roots in four-level high-variation chambers.

Search variables:
  gaps: x=(0,1,u,v), 1<u<v
  multiplicities: positive continuous ratios (scale irrelevant)

Objective:
  maximize sign-changing zeros of kappa_3(t) on t>1.

IMPORTANT: output is exploratory. Any 5+ root candidate must be rationalized
and interval-certified before theorem use.
"""
import numpy as np
from scipy.optimize import differential_evolution

def k3(t,u,v,logr):
    x=np.array([0.,1.,u,v])
    r=np.exp(np.r_[0.,logr])
    z=r[:,None]*np.exp(-x[:,None]*t[None,:])
    q=z/z.sum(axis=0)
    mu=(q*x[:,None]).sum(axis=0)
    return (q*(x[:,None]-mu)**3).sum(axis=0)

def roots_by_sign(y):
    s=np.sign(y); s[s==0]=1
    return int(np.sum(s[:-1]*s[1:]<0))

# Dense log grid resolves early and late transitions.
T=np.unique(np.r_[np.linspace(1,8,2500),np.geomspace(8,120,3500)])

def objective(z):
    # parameterization guarantees 1<u<v
    u=1+np.exp(z[0]); v=u+np.exp(z[1])
    y=k3(T,u,v,np.array(z[2:5]))
    n=roots_by_sign(y)
    # reward robust crossings; tiny values alone do not count
    margin=np.percentile(np.abs(y),10)
    return -n-1e-3*np.log10(max(margin,1e-300))

if __name__=="__main__":
    bounds=[(-3,3),(-3,3),(-8,8),(-8,8),(-8,8)]
    for seed in range(24):
        res=differential_evolution(objective,bounds,seed=seed,popsize=20,
                                   maxiter=350,tol=1e-8,polish=True,workers=1)
        z=res.x; u=1+np.exp(z[0]); v=u+np.exp(z[1])
        y=k3(T,u,v,z[2:5]); n=roots_by_sign(y)
        print(seed,n,u,v,np.exp(np.r_[0.,z[2:5]]),res.fun)
