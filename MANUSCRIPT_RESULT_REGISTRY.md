# Manuscript Result Registry

This file is the authoritative status ledger for paper drafting.

## A. Analytic identities / theorem-grade derivations

- Power sum: (F_W(s)=\sum_iw_i^{1+s}=e^{-sH_{1+s}(W)}).
- APG first order: (delta_{K_P}=H(W)|K_P|/2+O(K_P^2)).
- Escort calculus: (L'=E_q[I]), (L''=-V), (V'=-\kappa_3), and (\kappa_r'=-\kappa_{r+1}).
- Exact remainder: (sH-L(s)=\int_0^s(s-u)V(u)du).
- Sum rules: (\int_0^\infty V=H-H_\infty) and (\int_0^\infty sV=H_\infty-\log r_1).
- Exact two-level classification and transient-amplification criterion.
- Minimum-coordinate phenomenon: two coordinates cannot transiently amplify; three can.
- General pair/triple decomposition of (Z^3\kappa_3).
- Three-level zero ceiling (N_V\le3), together with an attaining construction: (N_{\max}(3)=3).
- Three-geometric-level bifurcation at (\lambda=B/\sqrt{AC}=4).
- Boundary merging lemma: combining consecutive coefficients at coincident exponential rates cannot increase sign variation.

## B. Computer-assisted finite certificates

- Four-level normalization (x=(0,1,u,v)), (1<u<v).
- Exactly ten relevant affine walls.
- Exhaustive feasibility enumeration of all (2^{10}) wall-sign vectors yields 24 generic chambers.
- Generic chamber sign-variation histogram: 12 chambers at 5, 6 at 7, 2 at 9, 4 at 11.
- Analytic boundary-merging lemma extends the generic maximum to all walls/intersections, yielding the global four-level upper bound (N_V(W)\le11).
- Exact rational four-level family (x=(0,1/4,15/28,55/56)), multiplicities ((3,518,2786,135)), has four disjoint physical sign-changing brackets certified by outward-rounded interval arithmetic.
- Therefore the current four-level theorem is
[
\boxed{4\le N_{\max}(4)\le11}.
]

## C. Exploratory evidence — never state as theorem

- Broad random searches have not yet found a five-root four-level example.
- Four generic chambers attain coefficient sign variation 11, but this does not imply 11 zeros are attainable.
- The exact value of (N_{\max}(4)) remains open.

## D. Classical ingredients that require attribution

Rényi entropy, escort distributions, exponential-family cumulant identities, Laplace-transform uniqueness, Newton/Prony/Vandermonde reconstruction, and generalized Descartes/variation-diminishing zero bounds are classical. The exponential-polynomial sign-variation bound must be cited rather than presented as an APG theorem.

## E. Candidate contribution to foreground

The strongest candidate contribution is not the classical escort machinery itself, but the transition-complexity program:
finite probability-level geometry -> multiplicity-controlled escort varentropy -> transient amplification -> exact low-level transition classification -> sharp three-level complexity -> finite four-level complexity bounds.

Novelty wording remains provisional until the dedicated prior-art audit is complete.
