# Direct six-zero feasibility — Batch 1

## Executed question

The scale-normalized six-equation system
[
kappa_3(t_j)=0,qquad 1<t_1<cdots<t_6
]
was attacked numerically with the four-level parameterization
[
x=a(0,1,u,v),qquad a>0,quad1<u<v,
]
three independent multiplicity ratios, and positive-increment coordinates for the six ordered times.

The residuals were divided by the cube of the information span to prevent the false solution mechanism in which all gaps collapse and every third cumulant becomes numerically tiny.

## Outcome

The search produced very small residual configurations, but the best near-solutions approached degeneracies rather than a robust configuration of six separated simple physical zeros. The recurring failure modes were:

1. **time collision:** two or more proposed zero times approach one another, indicating a multiple-root limit rather than six separated roots;
2. **boundary approach:** the earliest proposed zero approaches (t=1);
3. **tail escape:** the latest proposed zero is driven to increasingly large (t), where the escort distribution is already close to its dominant-level asymptotic regime;
4. **geometry/multiplicity ill-conditioning:** large parameter ratios create numerically tiny residuals without a stable six-crossing sign pattern.

No candidate from this batch survived the stronger test of six disjoint sign-changing brackets.

## What this means

This is **not** a proof that six roots are impossible. It is, however, more informative than the previous root-maximization searches: forcing six simultaneous equations appears to push the system toward the boundary of the admissible/separated-root configuration space.

That suggests a possible compactness-plus-boundary strategy:

- impose quantitative separation (t_{j+1}-t_jgearepsilon);
- bound the geometry away from collisions and the multiplicity ratios away from 0/infinity;
- bound the final root using the explicit asymptotic sign of (kappa_3);
- prove the resulting compact interior contains no six-zero solution, possibly by interval branch-and-bound;
- separately analyze every excluded boundary regime analytically.

Such a program could turn the observed degeneracies into a rigorous obstruction.

## Certified theorem status

Unchanged:
[
oxed{5le N_{max}(4)le11}.
]

No claim (N_{max}(4)=5) is justified yet.
