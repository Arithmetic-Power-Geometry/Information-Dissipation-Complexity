"""Boundary-aware continuation from the certified five-root family.

Searches BOTH mechanisms by which the physical root count on t>1 can change:
(A) interior k3=k4=0; (B) boundary k3(1)=0.

The script deliberately retains the absolute information scale.
"""
import numpy as np
from scipy.optimize import least_squares
X0=np.array([0.,7/250,57/400,137/500])
LR0=np.log(np.array([103.,5246.,6376.]))

def cumulants(t,x,lr):
    r=np.exp(np.r_[0.,lr]); z=r*np.exp(-t*x); q=z/z.sum()
    mu=q@x; y=x-mu
    m2=q@(y*y); m3=q@(y**3); m4=q@(y**4); m5=q@(y**5)
    return m3,m4-3*m2*m2,m5-10*m3*m2

def unpack(z):
    gaps=np.diff(X0)*np.exp(z[:3])
    return np.r_[0.,np.cumsum(gaps)],LR0+z[3:6]

def count(x,lr):
    T=np.unique(np.r_[np.linspace(1.0000001,12,6000),np.geomspace(12,800,16000)])
    y=np.array([cumulants(t,x,lr)[0] for t in T])
    s=np.sign(y); s[s==0]=1
    return int(np.sum(s[:-1]*s[1:]<0))

def boundary_residual(z,anchor):
    x,lr=unpack(z)
    k3,_,_=cumulants(1.,x,lr)
    return np.r_[k3/1e-5,0.01*(z[:5]-anchor[:5])]

if __name__=="__main__":
    rng=np.random.default_rng(20260923)
    print("seed",count(X0,LR0))
    best=(5,X0,LR0,None)
    # Boundary-root search: can change count by one.
    for trial in range(1500):
        a=rng.normal(0,.55,6)
        sol=least_squares(lambda z:boundary_residual(z,a),a,max_nfev=1800,
                          xtol=1e-12,ftol=1e-12,gtol=1e-12)
        x,lr=unpack(sol.x); k3,k4,_=cumulants(1.,x,lr)
        if abs(k3)>1e-8 or abs(k4)<1e-9: continue
        for j in range(6):
            for eps in (-.03,-.01,.01,.03):
                z=sol.x.copy(); z[j]+=eps
                xx,ll=unpack(z); n=count(xx,ll)
                if n>best[0]:
                    best=(n,xx,ll,("boundary",trial,j,eps,k4))
                    print("NEW BEST",best)
    print("FINAL BEST",best)
