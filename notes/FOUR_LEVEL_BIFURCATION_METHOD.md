# Four-level bifurcation search

## Principle

For the escort family, differentiation with respect to the tilt parameter gives
[
kappa_r'(t)=-kappa_{r+1}(t).
]
Therefore an interior multiple zero of the third cumulant satisfies
[
kappa_3(t_*)=0,qquad kappa_4(t_*)=0.
]
Such points are the generic birth/death loci for pairs of zeros of (kappa_3), equivalently pairs of stationary points of escort varentropy.

## Search parameterization

Use
[
x=(0,1,u,v),quad 1<u<v,quad t>1,
]
with positive multiplicity ratios represented in logarithmic coordinates. The simultaneous equations leave a positive-dimensional bifurcation set, so the objective is not a single isolated optimum: random starts locate points on this set, after which a transverse multiplicity perturbation is used to compare physical root counts on the two sides.

## Promotion rule

A candidate is scientifically meaningful only if crossing the double-root locus changes the physical sign-changing root count. If one side has at least five roots, that side becomes a candidate for rationalization and interval certification. A numerical double root by itself is not a theorem and is not evidence that five roots exist.

## Reproducibility

The companion script performs:
- 5000 randomized nonlinear least-squares starts;
- strict residual filtering for (kappa_3=kappa_4=0);
- physical-domain checks (1<u<v), (1<t<200);
- deduplication of discovered bifurcation points;
- transverse perturbations and dense physical root recounting;
- reporting of (kappa_5), useful for identifying nondegenerate double roots because (kappa_3''=kappa_5) at (kappa_4=0).

The next paper-grade action after any successful 5+ side is exact rational/integer approximation followed by outward-rounded interval certification.
