# Eventual-sign theorem for the third escort cumulant

## Setting

Let the distinct information levels be
[
x_1<x_2<cdots<x_d
]
with positive multiplicities (r_i), and let
[
u_i(t)=r_i e^{-t x_i},qquad
q_i(t)=rac{u_i(t)}{sum_j u_j(t)}.
]
Write
[
Delta=x_2-x_1>0,qquad
ho=rac{r_2}{r_1},
]
and, when (dge3),
[
Delta_3=x_3-x_1>Delta.
]

Because central cumulants are translation invariant, set (x_1=0).

## Leading asymptotic

Let
[
arepsilon(t)=ho e^{-tDelta}.
]
All remaining levels contribute
[
O(e^{-tDelta_3}).
]
Hence
[
q_2(t)=arepsilon(t)+O(arepsilon(t)^2)+O(e^{-tDelta_3}),
]
[
q_1(t)=1-arepsilon(t)+O(arepsilon(t)^2)+O(e^{-tDelta_3}),
]
and (q_j(t)=O(e^{-t(x_j-x_1)})) for (jge3).

The escort mean satisfies
[
mu(t)=Delta,arepsilon(t)
+O(arepsilon(t)^2)+O(e^{-tDelta_3}).
]

For the third central moment,
[
kappa_3(t)=sum_iq_i(t)(x_i-mu(t))^3.
]
The dominant contribution is from level 2:
[
q_2(Delta-mu)^3
=
Delta^3arepsilon(t)+O(arepsilon(t)^2)+O(e^{-tDelta_3}).
]
The level-1 contribution is (O(arepsilon^3)), and all higher levels are
(O(e^{-tDelta_3})). Therefore
[
oxed{
kappa_3(t)
=
hoDelta^3e^{-tDelta}
+
O(e^{-teta})
}
]
for some
[
eta>Delta,
qquad
eta=min(2Delta,Delta_3)
]
when (dge3) (with the obvious two-level simplification).

Consequently,
[
oxed{kappa_3(t)>0quad	ext{for all sufficiently large }t.}
]

Since
[
V'(t)=-kappa_3(t),
]
escort varentropy is eventually strictly decreasing.

## Stronger limit

The leading coefficient is explicit:
[
oxed{
lim_{t	oinfty}e^{tDelta}kappa_3(t)
=
rac{r_2}{r_1}Delta^3>0.
}
]

This complements the known varentropy tail
[
V(t)sim rac{r_2}{r_1}Delta^2e^{-tDelta}.
]

## Consequence for the six-zero program

A sequence of zeros cannot persist arbitrarily far into the tail for one fixed nondegenerate parameter vector: after a finite threshold the sign is positive.

For a *uniform* compactness argument across a parameter family, however, one still needs quantitative lower bounds on (Delta), upper/lower bounds on multiplicity ratios, and control of the next gap. Without such bounds the eventual-sign threshold need not be uniform.

Thus this theorem removes tail escape pointwise, but a global six-zero obstruction still requires a uniform tail lemma on the compact interior plus separate treatment of gap/multiplicity degeneracies.

## Status

Analytic theorem; no numerical assumption is used.
