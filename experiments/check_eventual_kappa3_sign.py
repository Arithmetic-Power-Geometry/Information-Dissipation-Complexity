"""High-precision sanity check for the eventual-sign asymptotic.

For a chosen finite information spectrum, compare
exp(t*Delta)*kappa3(t) with (r2/r1)*Delta**3.
This is a verification aid, not part of the proof.
"""
import mpmath as mp

mp.mp.dps=80

def kappa3(t,x,r):
    z=[mp.mpf(rr)*mp.e**(-t*mp.mpf(xx)) for xx,rr in zip(x,r)]
    Z=sum(z); q=[a/Z for a in z]
    mu=sum(qi*mp.mpf(xx) for qi,xx in zip(q,x))
    return sum(qi*(mp.mpf(xx)-mu)**3 for qi,xx in zip(q,x))

if __name__=="__main__":
    x=[0, mp.mpf("0.37"), mp.mpf("0.91"), mp.mpf("1.8")]
    r=[3,17,5,11]
    D=x[1]-x[0]
    target=mp.mpf(r[1])/r[0]*D**3
    print("target =",mp.nstr(target,30))
    for t in [10,20,40,80,160]:
        scaled=mp.e**(t*D)*kappa3(mp.mpf(t),x,r)
        print(t,mp.nstr(scaled,30))
