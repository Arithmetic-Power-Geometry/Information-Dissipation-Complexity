"""Symbolic/numerical stress test for adjacent coefficient-minor signs.

Purpose: falsify naive fixed-sign-minor hypotheses quickly. A sign flip is
enough to rule out a chamber-wide ordinary log-convexity claim; absence of a
flip is not a proof.
"""
import numpy as np

def stress_minor(A,B,C,D,ns=10000,seed=20260923):
    rng=np.random.default_rng(seed)
    signs=set()
    # Generic monomial model c0=A*r1^2*r2, c1=B*r1*r2*r3,
    # c2=C*r2^2*r3; representative of differing pair/triple exponents.
    for _ in range(ns):
        r=np.exp(rng.uniform(-8,8,4))
        c0=A*r[0]**2*r[1]
        c1=B*r[0]*r[1]*r[2]
        c2=C*r[1]**2*r[2]
        d=c0*c2-c1*c1
        if d: signs.add(int(np.sign(d)))
        if len(signs)==2:return signs
    return signs

if __name__=="__main__":
    # Positive geometry factors are placeholders after chamber signs are stripped.
    print("stress signs:",stress_minor(1.0,1.0,1.0,1.0))
    print("A two-sign result demonstrates why monomial compatibility alone does")
    print("not imply a fixed-sign adjacent-minor constraint.")
