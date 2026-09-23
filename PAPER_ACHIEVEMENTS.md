# Paper Achievement Ledger

## Unconditional power-sum / entropy spine

For (W=(w_i)),
[
F_W(s)=sum_i w_i^{1+s}=e^{-sH_{1+s}(W)},qquad D_W(s)=1-F_W(s).
]
The original APG first-order law is retained:
[
delta_{K_P}=rac{H(W)}2|K_P|+O(K_P^2).
]
The second-order expansion is
[
D_W(s)=Hs-rac{V+H^2}{2}s^2+O(s^3).
]

## Escort-information dynamics

With
[
q_i(s)=rac{w_i^{1+s}}{F_W(s)},qquad I_i=-log w_i,qquad L=-log F,
]
[
L'=E_q[I],qquad L''=-V_s,qquad V_s'=-kappa_{3,s},
]
and generally
[
kappa'_{r,s}=-kappa_{r+1,s}.
]

Exact integrated remainder:
[
sH-L(s)=int_0^s(s-u)V_u,du=s(H-H_{1+s}).
]

Sum rules:
[
int_0^infty V(s),ds=H-H_infty,
]
[
int_0^infty sV(s),ds=H_infty-log r_1.
]

Tail theory recovers the leading probability-level ratio from exponential varentropy decay.

## Dissipation-transition complexity

Define
[
N_V(W)=#{s>0:V'_W(s)=0}.
]

Established low-level results:
[
N_{max}(1)=0,qquad N_{max}(2)=1,qquad N_{max}(3)=3.
]

For two distinct probability levels the dynamics reduce exactly to a logistic variance and transient amplification occurs iff the initial combined escort mass of the lower-probability group exceeds (1/2). An ordinary two-coordinate probability vector cannot amplify; three coordinates are the minimum dimension that can.

For three geometric probability levels (M,Mr,Mr^2), with multiplicities (A,B,C),
[
lambda=rac{B}{sqrt{AC}},qquad R=rsqrt{C/A},
]
and
[
kappa_3propto(1-y^2)left[y^2+left(rac8lambda-lambdaight)y+1ight].
]
The exact bifurcation is
[
lambda=4.
]
For (lambda>4), the physical trajectory can exhibit three stationary points in max-min-max order. This construction proves sharpness of (N_{max}(3)=3).

## General third-cumulant decomposition

For distinct information levels (x_i) and unnormalized tilted masses (u_i),
[
Z^3kappa_3=
sum_{i
e j}(x_j-x_i)^3u_i^2u_j+
sum_{i<j<k}C_{ijk}u_iu_ju_k,
]
where
[
C_{ijk}=(x_i-2x_j+x_k)(x_i+x_j-2x_k)(2x_i-x_j-x_k).
]
Geometric spacing annihilates the genuine triple interaction:
[
C_{ijk}=0iff x_i+x_k=2x_jiff M_j^2=M_iM_k.
]

## Four-level theorem

After normalization (x=(0,1,u,v)), ten affine walls control all relevant rate collisions and triple-sign changes. They divide the admissible wedge into 24 generic chambers. Generic sign variations are
[
5,7,9,11
]
with chamber counts
[
12,6,2,4.
]
The maximum is 11. A consecutive-block merging lemma closes all wall/intersection cases, so the global four-level upper bound is
[
N_V(W)le11.
]

The current explicit rational construction supplies four physical stationary points, yielding
[
oxed{4le N_{max}(4)le11}.
]

## What remains before manuscript freeze

1. Replace floating-point sign brackets for the four-root lower-bound example by outward-rounded interval arithmetic.
2. Produce the complete 24-chamber certificate table as supplementary/repository artifact.
3. Continue the targeted search in the four variation-11 chambers for a fifth or higher root; this may improve the lower bound but is not required for the (4le N_{max}(4)le11) theorem.
4. Complete a focused prior-art audit before claiming the sharp (d=3) phase theorem or the dissipation-complexity framework as novel.
5. Draft the unified paper around the unconditional power-sum -> Rényi -> escort -> varentropy -> transition-complexity spine.
