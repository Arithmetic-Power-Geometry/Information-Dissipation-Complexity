"""Continuation from the certified five-root family.

Exact seed:
 x=(0,7/250,57/400,137/500), r=(1,103,5246,6376).

Parameterize x=a*(0,1,u,v).  Unlike all-real-zero upper-bound work, a is
retained because physical roots are restricted to t>1.

Goal: locate nearby kappa3=kappa4=0 bifurcation points and probe both sides
for >=6 physical roots. Discovery output is not theorem-grade until an exact
family is interval-certified.
"""
import numpy as np
from scipy.optimize import least_squares

X0=np.array([0.,7/250,57/400,137/500])
a0=X0[1]; u0=X0[2]/a0; v0=X0[3]/a0
lr0=np.log(np.array([103.,5246.,6376.]))

def cumulants(t,a,u,v,lr):
    x=a*np.array([0.,1.,u,v]); r=np.exp(np.r_[0.,lr])
    z=r*np.exp(-t*x); q=z/z.sum()
    mu=q@x; y=x-mu
    k2=q@(y**2); k3=q@(y**3)
    k4=q@(y**4)-3*k2*k2
    k5=q@(y**5)-10*(q@(y**3))*k2
    return k2,k3,k4,k5

def decode(z):
    a=np.exp(z[0]); u=1+np.exp(z[1]); v=u+np.exp(z[2])
    lr=z[3:6]; t=1+np.exp(z[6])
    return a,u,v,lr,t

def residual_free(z):
    a,u,v,lr,t=decode(z)
    _,k3,k4,_=cumulants(t,a,u,v,lr)
    return np.array([k3,k4])

def k3grid(a,u,v,lr,T):
    x=a*np.array([0.,1.,u,v]); r=np.exp(np.r_[0.,lr])
    z=r[:,None]*np.exp(-x[:,None]*T); q=z/z.sum(0)
    mu=(q*x[:,None]).sum(0)
    return (q*(x[:,None]-mu)**3).sum(0)

def count(a,u,v,lr):
    T=np.unique(np.r_[np.linspace(1.000001,20,5000),
                      np.geomspace(20,1000,10000)])
    y=k3grid(a,u,v,lr,T); s=np.sign(y); s[s==0]=1
    return int(np.sum(s[:-1]*s[1:]<0))

if __name__=="__main__":
    rng=np.random.default_rng(20260923)
    zseed=np.r_[np.log(a0),np.log(u0-1),np.log(v0-u0),lr0,np.log(20.)]
    best=(5,None)
    for trial in range(4000):
        # stay near the certified 5-root family but explore several scales
        z0=zseed+rng.normal(0,[.7,.5,.5,1.2,1.2,1.2,1.5])
        sol=least_squares(residual_free,z0,max_nfev=2500,
                          xtol=1e-12,ftol=1e-12,gtol=1e-12)
        if np.linalg.norm(sol.fun)>1e-10: continue
        a,u,v,lr,t=decode(sol.x)
        if not (1<t<1000 and 0<a<2 and 1<u<v<50): continue
        _,_,_,k5=cumulants(t,a,u,v,lr)
        if abs(k5)<1e-10: continue
        # transverse probes in all parameter coordinates except t
        for j in range(6):
            for eps in (-.01,.01,-.03,.03):
                zz=sol.x.copy(); zz[j]+=eps
                aa,uu,vv,ll,_=decode(zz)
                n=count(aa,uu,vv,ll)
                if n>best[0]:
                    best=(n,(aa,uu,vv,np.exp(np.r_[0.,ll]),t,k5,j,eps))
                    print("NEW BEST",best)
                    if n>=6: raise SystemExit
    print("FINAL BEST",best)
