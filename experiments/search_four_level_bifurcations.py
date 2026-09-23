"""Four-level double-root / bifurcation search.

Finds solutions of kappa_3(t)=kappa_4(t)=0 for x=(0,1,u,v), t>1.
At such a point kappa_3 has a multiple zero because d kappa_3/dt=-kappa_4.

This is a discovery tool. A root-count improvement must be rationalized and
interval-certified separately.
"""
import numpy as np
from scipy.optimize import least_squares

def cumulants(t,u,v,logr):
    x=np.array([0.,1.,u,v],float)
    r=np.exp(np.r_[0.,logr])
    z=r*np.exp(-t*x); q=z/z.sum()
    mu=np.dot(q,x); y=x-mu
    k2=np.dot(q,y**2); k3=np.dot(q,y**3)
    k4=np.dot(q,y**4)-3*k2*k2
    k5=np.dot(q,y**5)-10*np.dot(q,y**3)*k2
    return k2,k3,k4,k5

def residual(z):
    # z=(log(u-1),log(v-u),log r2,log r3,log r4,log(t-1))
    u=1+np.exp(z[0]); v=u+np.exp(z[1]); t=1+np.exp(z[5])
    _,k3,k4,_=cumulants(t,u,v,z[2:5])
    return np.array([k3,k4])

def count_crossings(u,v,logr,T):
    vals=np.array([cumulants(t,u,v,logr)[1] for t in T])
    sg=np.sign(vals); sg[sg==0]=1
    return int(np.sum(sg[:-1]*sg[1:]<0))

if __name__=="__main__":
    rng=np.random.default_rng(20260923)
    T=np.unique(np.r_[np.linspace(1.000001,10,3000),np.geomspace(10,200,4000)])
    sols=[]
    for trial in range(5000):
        z0=np.r_[rng.uniform(-2.5,2.5,2),rng.uniform(-8,8,3),rng.uniform(-3,4)]
        sol=least_squares(residual,z0,max_nfev=3000,xtol=1e-13,ftol=1e-13,gtol=1e-13)
        if np.linalg.norm(sol.fun)>1e-9: continue
        z=sol.x; u=1+np.exp(z[0]); v=u+np.exp(z[1]); t=1+np.exp(z[5])
        if not (1<u<v and 1<t<200): continue
        _,k3,k4,k5=cumulants(t,u,v,z[2:5])
        # probe both sides of one multiplicity parameter
        counts=[]
        for eps in (-2e-3,2e-3):
            lr=z[2:5].copy(); lr[0]+=eps
            counts.append(count_crossings(u,v,lr,T))
        key=tuple(np.round([u,v,t,*np.exp(np.r_[0.,z[2:5]])],6))
        if all(np.linalg.norm(np.array(key)-np.array(q[0]))>1e-4 for q in sols):
            sols.append((key,counts,k5))
            print("solution",key,"side-counts",counts,"k5",k5)
    print("distinct double-root candidates",len(sols))
