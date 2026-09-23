"""Outward-rounded interval certificate for four physical roots."""
import mpmath as mp
iv=mp.iv
X=[iv.mpf([0,0]),iv.mpf([1,1])/4,iv.mpf([15,15])/28,iv.mpf([55,55])/56]
R=[iv.mpf([3,3]),iv.mpf([518,518]),iv.mpf([2786,2786]),iv.mpf([135,135])]
def kappa3_at(s):
    t=iv.mpf([s,s])
    w=[R[i]*iv.exp(-t*X[i]) for i in range(4)]
    Z=sum(w); q=[z/Z for z in w]
    mu=sum(q[i]*X[i] for i in range(4))
    return sum(q[i]*(X[i]-mu)**3 for i in range(4))
BRACKETS=[("1.08","1.10"),("6.10","6.12"),("14.45","14.48"),("19.63","19.66")]
if __name__=="__main__":
    for a,b in BRACKETS:
        print(a,kappa3_at(a),b,kappa3_at(b))
