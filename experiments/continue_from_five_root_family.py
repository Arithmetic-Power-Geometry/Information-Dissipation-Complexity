"""Continuation search around the certified five-root four-level family.

Exact seed:
x=(0,7/250,57/400,137/500), r=(1,103,5246,6376).

Searches nearby parameter space for kappa3=kappa4=0 bifurcations while retaining
the absolute information-gap scale. It then probes transverse directions and
counts physical sign-changing zeros on t>1.

Discovery only: any stronger candidate requires rationalization and interval
certification.
"""
import numpy as np
from scipy.optimize import least_squares

X0=np.array([0.,7/250,57/400,137/500])
LR0=np.log(np.array([103.,5246.,6376.]))

def cumulants(t,x,lr):
    r=np.exp(np.r_[0.,lr])
    z=r*np.exp(-t*x); q=z/z.sum()
    mu=q@x; y=x-mu
    m2=q@(y**2); m3=q@(y**3); m4=q@(y**4); m5=q@(y**5)
    return m3,m4-3*m2*m2,m5-10*m3*m2

def count_roots(x,lr,T):
    y=np.array([cumulants(t,x,lr)[0] for t in T])
    s=np.sign(y); s[s==0]=1
    return int(np.sum(s[:-1]*s[1:]<0))

def unpack(z):
    # multiplicative perturbations of the three positive gaps + multiplicities
    gaps=np.diff(X0)*np.exp(z[:3])
    x=np.r_[0.,np.cumsum(gaps)]
    lr=LR0+z[3:6]
    t=1+np.exp(z[6])
    return x,lr,t

def residual(z,anchor):
    x,lr,t=unpack(z)
    k3,k4,_=cumulants(t,x,lr)
    # two exact bifurcation equations plus weak anchoring of 5 free directions
    return np.r_[k3/1e-4,k4/1e-4,0.015*(z[:5]-anchor[:5])]

if __name__=="__main__":
    rng=np.random.default_rng(20260923)
    T=np.unique(np.r_[np.linspace(1.000001,12,5000),
                      np.geomspace(12,500,10000)])
    base=count_roots(X0,LR0,T)
    print("seed physical roots",base)
    best=(base,X0,LR0,None)
    bif=0
    for trial in range(1200):
        anchor=np.r_[rng.normal(0,.45,6),rng.uniform(np.log(.02),np.log(250))]
        sol=least_squares(lambda z:residual(z,anchor),anchor,
                          max_nfev=2500,xtol=1e-12,ftol=1e-12,gtol=1e-12)
        x,lr,t=unpack(sol.x)
        k3,k4,k5=cumulants(t,x,lr)
        if t<=1 or t>500 or abs(k3)>2e-8 or abs(k4)>2e-8 or abs(k5)<1e-9:
            continue
        bif+=1
        # probe every parameter coordinate both directions
        for j in range(6):
            for eps in (-.03,-.01,.01,.03):
                zz=sol.x.copy(); zz[j]+=eps
                xx,ll,_=unpack(zz)
                n=count_roots(xx,ll,T)
                if n>best[0]:
                    best=(n,xx,ll,(trial,j,eps,t,k5))
                    print("NEW BEST",best)
    print("accepted bifurcations",bif)
    print("FINAL BEST",best)
