# Four-Level Global Upper Bound — Boundary Closure

## Theorem

Let (W) be a finite probability vector having exactly four distinct positive probability levels. Let (V_W(s)) be the escort varentropy along the power deformation, and let
[
N_V(W)=#{s>0:V'_W(s)=0}
]
count stationary points with multiplicity. Then
[
N_V(W)le 11.
]

Consequently, with the explicit four-root construction,
[
4le N_{max}(4)le 11.
]

## Proof architecture

Normalize the four distinct information levels to
[
x=(0,1,u,v),qquad 1<u<v.
]
The numerator of the third escort cumulant is a finite real exponential sum
[
Z(t)^3kappa_3(t)=sum_ho A_ho e^{-ho t}.
]
Its structural rates arise from (2x_i+x_j) and (x_i+x_j+x_k).

The admissible ((u,v))-wedge is cut by ten rate-collision/sign walls. Exhaustive exact half-plane feasibility enumeration gives 24 generic chambers. In every generic chamber the rate ordering and coefficient signs are fixed. The complete chamber variation histogram is
[
mathcal C=5:12,qquad
mathcal C=7:6,qquad
mathcal C=9:2,qquad
mathcal C=11:4.
]
Hence every generic four-level numerator has at most 11 coefficient sign variations.

### Boundary lemma

Suppose several adjacent ordered rates coalesce on a chamber wall. In the limiting exponential sum, all coefficients belonging to the same limiting rate are replaced by their sum. Replacing any consecutive block of a real coefficient sequence by its sum, deleting a zero sum if necessary, cannot increase the number of sign changes.

Proof: signs outside the block are unchanged. The original block together with its two neighboring signs contains at least as many transitions as can occur after replacing the whole block by one sign; if the block sum is zero, deletion likewise cannot create more transitions than were already present. Iterating proves the assertion for simultaneous collisions.

Therefore a boundary coefficient sequence has sign variation no greater than that of an adjacent generic chamber. Since every adjacent generic chamber has variation at most 11, every wall, wall intersection, and higher-codimension collision satisfies
[
mathcal Cle11.
]

The generalized Descartes rule for real exponential sums then gives
[
#{tinmathbb R: kappa_3(t)=0}le11
]
(counting multiplicity, unless the numerator is identically zero). Restricting to the physical branch (t=1+s>1) cannot increase this count. Since (V'(s)=-kappa_3(1+s)),
[
N_V(W)le11.
]

The identically-zero case corresponds to degenerate information geometry and must be excluded/handled separately in the formal theorem definition; for exactly four distinct levels the working derivation assumes the nonzero numerator case.

## Status

The chamber enumeration is computer-assisted finite verification; the boundary closure is analytic. For a fully self-contained manuscript proof, include either (i) the 24-chamber certificate table in supplementary material, or (ii) a short machine-verifiable script plus checksum/repository release.

The lower bound (N_{max}(4)ge4) comes from the rational four-level family already recorded in the repository. Its sign brackets should still be upgraded to outward-rounded interval arithmetic before calling that lower-bound construction formally computer-certified.
