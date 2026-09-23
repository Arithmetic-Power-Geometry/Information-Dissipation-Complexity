# Four-level bifurcation search — Batch 1

## Executed search

A numerical batch of 1000 randomized starts was run for the simultaneous equations
[
kappa_3(t)=0,qquad kappa_4(t)=0
]
with normalized levels (x=(0,1,u,v)), (1<u<v), positive multiplicity ratios in log coordinates, and physical (1<t<200).

The solve was parameter-sliced: for each random geometry and two fixed multiplicity log-ratios, the tilt (t) and remaining multiplicity log-ratio were solved by nonlinear least squares. Candidates required residual norm below (10^{-9}) and (|kappa_5|>10^{-7}).

## Outcome

80 nondegenerate numerical double-root solutions passed these filters.

For each solution the first multiplicity log-ratio was perturbed by (pm0.005) and (pm0.02), and physical sign-changing roots of (kappa_3) were recounted on a dense mixed linear/log grid extending to (t=250).

The largest perturbed count observed in this batch was **3**, not 5 or 6. Thus this unrestricted bifurcation batch did not improve the certified four-root construction.

Representative bifurcation:
[
uapprox1.5654715153,quad vapprox2.1809783152,quad
t_*approx1.9243112568,
]
with log multiplicity ratios approximately
[
(4.47620453, 5.01894778, 5.80933863)
]
and
[
kappa_5(t_*)approx-0.09438656
e0.
]
After a (+0.005) perturbation of the first log-ratio, three sign-changing roots were observed near
[
tapprox1.812,quad2.037,quad4.165.
]

## Interpretation

This is exploratory negative evidence only. It does not lower the upper bound and does not imply that 5- or 6-root families do not exist.

The important methodological lesson is that unrestricted double-root solving overwhelmingly locates low-complexity bifurcations. The next search should be constrained to the four already-certified (mathcal C=11) chambers and seeded from four-root families, rather than sampling the full admissible wedge.

## Theorem status

Unchanged:
[
oxed{4le N_{max}(4)le11}.
]
