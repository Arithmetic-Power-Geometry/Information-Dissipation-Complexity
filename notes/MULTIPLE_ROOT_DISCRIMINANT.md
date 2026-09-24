# Multiple-root boundary: cumulant constraints

## 1. Derivative chain

Along the escort flow,
[
kappa_r'(t)=-kappa_{r+1}(t).
]
Hence for
[
f(t)=kappa_3(t),
]
we have
[
f'(t)=-kappa_4(t),qquad
f''(t)=kappa_5(t),qquad
f^{(m)}(t)=(-1)^mkappa_{m+3}(t).
]

Therefore a zero t=t_* of kappa3 has multiplicity at least m iff
[
oxed{kappa_3(t_*)=kappa_4(t_*)=cdots=kappa_{m+2}(t_*)=0.}
]

In particular:
- double zero: kappa3=kappa4=0;
- triple zero: kappa3=kappa4=kappa5=0;
- quadruple zero: kappa3=kappa4=kappa5=kappa6=0.

This converts root collision into a finite moment/cumulant problem for the escort distribution at the collision time.

## 2. Double-zero interpretation

At kappa3=0 the escort information distribution has zero third central moment. At a double zero it also satisfies kappa4=0. Since
[
kappa_4=mu_4-3mu_2^2,
]
the conditions are
[
mu_3=0,qquad mu_4=3mu_2^2.
]
Thus a double transition is an escort state whose centered information values have zero skewness and Gaussian kurtosis (in the cumulant sense), despite finite support.

These are two independent algebraic constraints on the instantaneous four-point escort law.

## 3. Higher multiplicity is increasingly constrained

A triple zero additionally imposes kappa5=0; multiplicity m imposes m scalar cumulant equations. For a fixed four-level geometry, time is one scalar variable, so multiple roots are nongeneric. Allowing geometry and multiplicities makes them possible as bifurcation boundaries, but they lie on lower-dimensional parameter sets.

This codimension statement is structural/generic; it is not by itself an exclusion theorem.

## 4. Local root birth

Suppose parameters theta vary smoothly and at (t_*,theta_*) we have
[
f=0,quad f_t=0,quad f_{tt}
e0.
]
Equivalently
[
kappa_3=kappa_4=0,qquad kappa_5
e0.
]
Then the local Taylor form is
[
f(t,	heta)
=
rac{kappa_5(t_*,	heta_*)}{2}(t-t_*)^2
+

abla_	heta fcdot(	heta-	heta_*)
+cdots.
]
Generically this is a fold: crossing the discriminant creates or annihilates a pair of simple zeros. Hence the number of simple real transitions changes by two at an ordinary double-root boundary.

This explains why a transition from a five-root region to a hypothetical seven-root region would naturally pass through a double-root discriminant. A six-simple-root region is not forced by such a fold; parity must also account for roots crossing the physical boundary or other degeneracies.

## 5. Odd endpoint signs

For a fixed nondegenerate four-level trajectory, kappa3(t)>0 for all sufficiently large t. Therefore the sign after the last simple root is positive. Root-count changes inside a compact interval occur through multiple roots; changes in the physical count can additionally occur when a root crosses t=1.

This separates two mechanisms:
1. interior discriminant: kappa3=kappa4=0;
2. physical-boundary crossing: kappa3(1)=0.

## 6. What is proved and what remains open

Proved:
- exact multiplicity criterion through consecutive cumulant vanishing;
- ordinary double roots satisfy kappa3=kappa4=0, kappa5 != 0;
- generic local unfolding of an ordinary double root changes simple-root count by two;
- root collision is therefore an algebraic discriminant problem, not a separate noncompact escape.

Not yet proved:
- a global upper bound of five roots;
- impossibility of six positive roots;
- impossibility of high-order four-level multiple roots;
- connectivity of all relevant parameter regions.

Thus the multiple-root boundary is reduced to an explicit discriminant system but does not close N_max(4).

## 7. Manuscript-safe conclusion

The rigorous four-level statement remains
[
oxed{5le N_{max}(4)le11.}
]
The equations
[
kappa_3=kappa_4=0
]
define the transition discriminant for changes of interior root topology and provide a natural open route toward the exact value of N_max(4).
