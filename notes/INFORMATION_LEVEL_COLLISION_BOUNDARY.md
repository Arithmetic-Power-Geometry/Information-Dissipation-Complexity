# Information-level collision boundary

## Setting

Let
[
x_1<x_2<x_3<x_4,qquad r_i>0,
]
and
[
Z(t)=sum_{i=1}^4 r_i e^{-t x_i}.
]
The escort distribution is obtained by normalizing these four tilted masses.

Consider a collision (x_{k+1}	o x_k). At exact collision,
[
r_k e^{-t x_k}+r_{k+1}e^{-t x_k}
=(r_k+r_{k+1})e^{-t x_k}.
]
Thus the four-level model reduces exactly to a three-distinct-level model with merged multiplicity
[
r_k^{m new}=r_k+r_{k+1}.
]

## Exact boundary reduction

At the collision boundary, every escort moment and cumulant agrees with that of the merged three-level system. In particular,
[
kappa_3^{(4)}(t)longrightarrow kappa_3^{(3)}(t)
]
locally uniformly in (t) on every compact interval, provided the remaining levels and multiplicities remain nondegenerate.

The same holds for all derivatives because
[
rac{d}{dt}kappa_r=-kappa_{r+1},
]
and the tilted finite sums are analytic in both (t) and the level parameters.

Therefore the exact collision boundary inherits
[
N_{max}(3)=3.
]

## What continuity alone does NOT prove

It is not valid to conclude immediately that every sufficiently near-collision four-level system has at most three zeros. Under analytic perturbation, a multiple zero of the limiting three-level function can split into several nearby simple zeros.

Hence a six-zero sequence approaching a collision can only be excluded after controlling the multiplicities of zeros of the limiting three-level (kappa_3).

## Multiplicity accounting

If (f_n	o f) locally uniformly analytically and six distinct real zeros of (f_n) remain in a compact interval while parameters approach a collision, then every accumulation point of those zeros is a zero of (f), counted with sufficient complex-analytic multiplicity. Thus six real zeros can collapse to at most three distinct limiting zeros only if the limiting three-level (kappa_3) has total zero multiplicity at least six across those accumulation points.

This converts the collision-boundary problem into a sharper finite question:

> What is the maximum total multiplicity of zeros of three-level (kappa_3) on the physical interval?

The existing generalized-Descartes/Chebyshev proof gives at most three zeros **counting multiplicity** when formulated for the nonzero three-level exponential polynomial after rate collisions are combined.

Therefore the total multiplicity is at most three, not merely the number of distinct sign changes.

## Collision exclusion

Consequently, a sequence of four-level systems with six distinct physical zeros contained in a common compact interval cannot converge to a nondegenerate information-level collision boundary. Otherwise analytic convergence would force the limiting three-level numerator to possess at least six zeros counting multiplicity, contradicting the three-level Chebyshev bound.

Thus, subject to the standard nonzero-numerator condition already used in the three-level theorem,
[
oxed{	ext{six compact physical zeros cannot escape through an information-level collision}.}
]

## Scope

This argument controls collisions while:
- zero times remain in a common compact interval;
- the remaining distinct gaps stay nonzero;
- multiplicity ratios do not simultaneously degenerate.

Mixed boundaries (collision plus multiplicity blow-up, scale degeneration, or tail escape) require separate rescaling/limit analysis.

## Consequence for the compactness program

Combined with the uniform-tail lemma, pure information-level collisions are no longer an admissible escape mechanism for a hypothetical six-zero sequence. The unresolved boundaries are now primarily:
1. root-time collisions / multiple roots;
2. multiplicity degeneration;
3. scale degeneration;
4. mixed combinations of the above.
