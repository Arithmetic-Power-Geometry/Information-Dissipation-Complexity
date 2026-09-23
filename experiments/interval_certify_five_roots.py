"""Outward-rounded interval certificate for five physical roots."""
import mpmath as mp
iv=mp.iv
X=[iv.mpf([0,0]),iv.mpf([7,7])/250,iv.mpf([57,57])/400,iv.mpf([137,137])/500]
R=[iv.mpf([1,1]),iv.mpf([103,103]),iv.mpf([5246,5246]),iv.mpf([6376,6376])]
def kappa3(s):
    t=iv.mpf([str(s),str(s)])
    w=[R[i]*iv.exp(-t*X[i]) for i in range(4)]
    Z=sum(w); q=[z/Z for z in w]
    mu=sum(q[i]*X[i] for i in range(4))
    return sum(q[i]*(X[i]-mu)**3 for i in range(4))
BRACKETS=[("2.5","3"),("19","21"),("31","34"),("90","96"),("160","175")]
if __name__=="__main__":
    for a,b in BRACKETS:
        ka,kb=kappa3(a),kappa3(b)
        print(a,ka,b,kb)
