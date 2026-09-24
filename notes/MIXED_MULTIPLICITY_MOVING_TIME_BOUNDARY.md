# Mixed multiplicity--moving-time transition layers

## Balance coordinates

For tilted masses u_i(t)=r_i exp(-t x_i), every pair satisfies
log(u_j/u_i)=log(r_j/r_i)-t(x_j-x_i).

Suppose parameters vary with n and a multiplicity ratio diverges. Choose a moving center tau_n and write t=tau_n+s. Then
u_i(t)=exp[-tau_n x_i] r_i exp[-s x_i].
After dividing by any common positive factor, the transition-layer limit is determined by the finite limits of
b_i^(n)=log r_i^(n)-tau_n x_i^(n).

Only indices for which b_i^(n)-max_j b_j^(n) remains O(1) survive. Indices whose relative log-weight tends to -infinity disappear uniformly on compact s-intervals.

## Consequence

A moving-time multiplicity degeneration does not automatically reduce to three levels: in principle several affine log-weight lines can meet within O(1) height at the chosen center. However, with fixed distinct x_i, exact simultaneous balance of four levels at a single diverging tau_n requires the four quantities log r_i to become asymptotically affine functions of x_i with the same slope tau_n.

Thus the correct boundary object is not raw multiplicity blow-up but the set of surviving affine log-weight lines after recentering.

If at most three lines survive, the limiting escort cumulant is a three-level-or-lower system and six compact zeros in the recentered coordinate are excluded by the three-level zero bound counting multiplicity.

The only unresolved mixed multiplicity boundary is therefore the exceptional four-line survival regime, where
log r_i^(n)=alpha_n+tau_n x_i^(n)+beta_i+o(1)
for all four i with finite beta_i.

In that regime, after t=tau_n+s and removal of the common factor exp(alpha_n), the escort law converges to a genuine four-level law with effective multiplicities exp(beta_i):
q_i^*(s) proportional to exp(beta_i-s x_i).

So a four-line transition layer is not a new singular model; it is another ordinary four-level escort trajectory viewed in shifted time.

## Reduction of the escape question

If tau_n -> +infinity and the original physical zeros t>1 remain near tau_n, then in s-coordinates a hypothetical cluster of six roots converges to six roots (counting multiplicity) of an ordinary four-level limit. This does not by itself contradict the present 11-zero upper bound.

Therefore mixed multiplicity--time degeneration cannot yet be fully excluded. It is reduced to the same intrinsic four-level six-zero problem, rather than to an uncontrolled new boundary phenomenon.

This is useful structurally:
- <=3 surviving lines: excluded;
- 4 surviving lines: renormalizes to the core four-level problem.

No claim N_max(4)=5 follows from this reduction.
