import numpy as np
from scipy.optimize import brentq

X = np.array([0.0, 1/4, 15/28, 55/56], dtype=float)
R = np.array([3, 518, 2786, 135], dtype=float)

def kappa3(t):
    w = R*np.exp(-t*X)
    q = w/w.sum()
    mu = np.dot(q, X)
    return np.dot(q, (X-mu)**3)

def roots(tmin=1.0, tmax=30.0, n=20000):
    grid=np.linspace(tmin,tmax,n)
    vals=np.array([kappa3(t) for t in grid])
    out=[]
    for a,b,fa,fb in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
        if fa*fb < 0:
            rt=brentq(kappa3,a,b,xtol=1e-14)
            if not out or abs(rt-out[-1])>1e-9:
                out.append(rt)
    return out

if __name__ == "__main__":
    rs=roots()
    print("roots(t):", rs)
    print("roots(s):", [r-1 for r in rs])
    brackets=[(1.08,1.10),(6.10,6.12),(14.45,14.48),(19.63,19.66)]
    for a,b in brackets:
        print(a,kappa3(a),b,kappa3(b))
