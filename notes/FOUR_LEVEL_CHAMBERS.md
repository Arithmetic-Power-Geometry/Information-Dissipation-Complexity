# Four-Level Chamber Program

## Purpose

Determine the exact four-level escort-varentropy transition complexity without guessing from the low-level sequence.

Normalize the four distinct information levels by translation and positive scaling:

[
x_1=0,qquad x_2=1,qquad x_3=u,qquad x_4=v,qquad 1<u<v.
]

For positive multiplicities (r_i), set

[
u_i(t)=r_i e^{-t x_i},qquad Z(t)=sum_i u_i(t).
]

The stationary points of escort varentropy are the zeros of the third cumulant because

[
V'(s)=-kappa_3(1+s).
]

The numerator is

[
Z^3kappa_3=
sum_{i
e j}(x_j-x_i)^3u_i^2u_j+
sum_{i<j<k}C_{ijk}u_i u_j u_k,
]

where

[
C_{ijk}=(x_i-2x_j+x_k)(x_i+x_j-2x_k)(2x_i-x_j-x_k).
]

## Rate atoms

Pair atoms have rates

[
2x_i+x_j,qquad i
e j,
]

and triple atoms have rates

[
x_i+x_j+x_k,qquad i<j<k.
]

For (d=4) there are at most 16 structural atoms before collisions. After equal-rate atoms are combined, order the remaining coefficients by increasing rate and count their sign changes. Classical generalized Descartes / variation-diminishing theory bounds the number of real zeros of the exponential sum by this sign variation.

## Current computational observation

A dense two-parameter scan of (1<u<v) has found realizable rate/sign orderings with 11 sign variations. No larger value has yet been found. This is a **candidate variation ceiling only**, not a theorem.

Separately, the exact-rational family

[
x=left(0,rac14,rac{15}{28},rac{55}{56}ight),qquad
r=(3,518,2786,135)
]

has four numerically sign-changing roots on the physical branch. Hence the current safe lower-bound target is

[
N_{max}(4)ge4,
]

pending outward-rounded interval certification.

## Proof program

1. Enumerate all rate-order chambers in the ((u,v)) plane. Chamber boundaries are linear equalities between rates.
2. In each chamber, derive the coefficient-sign sequence symbolically, including the signs of all four triple coefficients.
3. Combine atoms on chamber boundaries before counting signs.
4. Prove the maximum realizable sign variation (mathcal C_4). The current computational candidate is 11.
5. Restrict zero searches to chambers with variation at least 5 when searching for a fifth stationary point.
6. Optimize positive multiplicities inside those chambers.
7. Rationalize any (5+)-root construction and certify each sign change by interval arithmetic.
8. If all (mathcal Cge5) chambers can be analytically excluded from realizing five zeros, prove (N_{max}(4)=4).

## Publication discipline

Do not state (N_{max}(4)=4), (N_{max}(4)=11), or (mathcal C_4=11) until proved. Negative random-search results are exploratory only.

The zero-count theorem for ordered real exponential sums and the signed-Laplace variation principle are classical tools; novelty, if established, lies in the constrained escort-varentropy transition problem and its sharp classifications.
