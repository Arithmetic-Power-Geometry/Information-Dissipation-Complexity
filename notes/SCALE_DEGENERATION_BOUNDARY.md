# Scale-degeneration boundary

## Exact scaling law

Let a fixed normalized information geometry be y_i with distinct y_1<...<y_d, and set
x_i=a y_i, a>0.
For multiplicities r_i,
q_i^{(a)}(t)
=
r_i exp(-a t y_i) / sum_j r_j exp(-a t y_j)
=
q_i^{(1)}(a t).

Central cumulants scale homogeneously:
[
\boxed{\kappa_r^{(a)}(t)=a^r\kappa_r^{(1)}(a t).}
]
In particular,
[
\boxed{\kappa_3^{(a)}(t)=a^3\kappa_3^{(1)}(a t).}
]

Therefore positive zeros obey the exact correspondence
[
\kappa_3^{(a)}(t)=0
\iff
\kappa_3^{(1)}(\tau)=0,qquad \tau=a t.
]

## Physical boundary

The APG/escort physical domain is t>1. Under tau=a t this becomes
[
\tau>a.
]
Thus scale does not change the total zero pattern of the normalized trajectory; it changes which part of that trajectory lies beyond the physical boundary.

If Z(y,r) denotes the multiset of positive zeros of the normalized kappa3, counting multiplicity, then
[
\boxed{
N_a=\#\{\tau\in Z(y,r):\tau>a\}.
}
]
Consequently N_a is nonincreasing as a increases.

## Limit a -> infinity

For any fixed normalized geometry and multiplicities, the normalized kappa3 is eventually positive, so it has no zeros above some finite T. Hence for a>T,
[
N_a=0.
]
Thus scale blow-up cannot create or hide a six-zero physical configuration for a fixed normalized four-level model.

Uniformly on a compact nondegenerate family, the uniform-tail lemma gives a common T, so all sufficiently large a have zero physical transitions.

## Limit a -> 0

The physical threshold tau>a tends to 0. Hence decreasing a can only reveal zeros of the normalized trajectory that were previously below the physical threshold; it cannot manufacture new normalized zeros.

Therefore scale degeneration a->0 is not a new singular root mechanism. It converts the physical problem toward the full positive-time zero problem of the same normalized four-level exponential polynomial.

This is important but does not by itself exclude six roots: if a normalized four-level trajectory possesses six positive zeros with some below tau=1, sufficiently small a would move all six into the physical t>1 domain.

Hence:
- a -> infinity is controlled by the tail theorem;
- a -> 0 reduces exactly to the intrinsic positive-zero problem for the normalized four-level trajectory.

## Consequence for the obstruction program

Scale is no longer an independent noncompact pathology. It is an exact threshold parameter:
[
N_a=\#(Z\cap(a,\infty)).
]
The unresolved issue is therefore the intrinsic four-level zero count itself, plus multiple-root/compact-interior analysis. No separate scale-boundary theorem can prove N_max(4)=5 without solving that core problem.

The rigorous frontier remains
[
5\le N_{\max}(4)\le11.
]
