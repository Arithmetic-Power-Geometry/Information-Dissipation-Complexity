# Uniform tail lemma on compact nondegenerate families

## Purpose

The pointwise theorem
[
kappa_3(t)sim (r_2/r_1)Delta^3e^{-tDelta}>0
]
shows eventual positivity for each fixed spectrum. For the six-zero compactness program we need a threshold that is uniform over a controlled family.

## Compact family

Translate (x_1=0). Assume constants
[
0<deltale Delta=x_2-x_1,qquad x_dle X,
]
and positive multiplicity bounds
[
0<mle r_ile M.
]
For (jge2), put (d_j=x_j-x_1). Then (d_2=Deltagedelta), and distinct-level separation may additionally be bounded below by (delta) when a fully uniform remainder exponent is required.

Let
[
z_j(t)=rac{r_j}{r_1}e^{-td_j},qquad
R(t)=sum_{jge2}z_j(t).
]
Since (r_j/r_1le M/m) and (d_jgedelta),
[
R(t)le (d-1)rac{M}{m}e^{-delta t}.
]

## Uniform concentration

Choose
[
T_0=rac1deltalog!left(2(d-1)rac{M}{m}ight).
]
Then (tge T_0) implies (R(t)le1/2), so
[
q_1=rac1{1+R}gerac23
]
and every nondominant escort mass is uniformly small.

For a sharp sign proof, isolate level 2:
[
z_2=(r_2/r_1)e^{-tDelta}.
]
The leading positive contribution to (kappa_3) is (Delta^3z_2). If all consecutive information gaps are at least (delta), then every level (jge3) satisfies
[
d_jgeDelta+delta,
]
so its relative contribution to the level-2 scale is bounded by a constant times (e^{-delta t}). Quadratic normalization/mean corrections are likewise bounded by a constant times (R(t)).

Hence on any family with fixed
[
(d,delta,X,m,M)
]
there exists an explicit finite constant (C=C(d,delta,X,m,M)) such that
[
left|
rac{kappa_3(t)}
{(r_2/r_1)Delta^3e^{-tDelta}}-1
ight|
le Ce^{-delta t}.
]
Therefore
[
T=T_0+rac1deltamax(0,log(2C))
]
is a uniform tail threshold, and
[
oxed{kappa_3(t)>0quad	ext{for all }tge T}
]
throughout the compact nondegenerate family.

## Consequence

Within such a family, every physical zero of (kappa_3) lies in the finite interval
[
1<t<T.
]
Thus the last zero cannot escape to infinity in the compact-interior branch of the six-zero proof.

The remaining work is to make one convenient explicit (C) sufficiently sharp for interval certification; existence of a uniform finite (C) follows directly from the displayed bounds.

## Boundary caveat

If the gap lower bound tends to zero or multiplicity ratios become unbounded, the threshold need not remain uniform. Those regimes must be handled separately by lower-level limits/rescaling, exactly as prescribed by the compactness decomposition.
