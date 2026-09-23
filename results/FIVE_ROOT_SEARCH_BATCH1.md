# Targeted five-root search — Batch 1

## Purpose
Test whether the certified lower bound (N_{max}(4)ge4) can be improved to 5 by direct optimization of actual physical zeros of (kappa_3(t)), (t>1).

## Search performed
Eight independent differential-evolution restarts were run over normalized four-level geometries
[
x=(0,1,u,v),qquad1<u<v,
]
and three independent positive multiplicity ratios. The search domain used log-parameter bounds ([-3,3]) for the two positive gaps and ([-9,9]) for each multiplicity log-ratio. Physical roots were detected as sign changes on a dense mixed linear/logarithmic grid over (1le tle160).

## Outcome
No five-root candidate was found in this batch. The best attained count was four physical sign-changing roots, reached independently by several substantially different parameter families.

Representative best candidates (multiplicity scale normalized to first entry 1):

1. (uapprox2.2340958997, vapprox6.9586146566),
   (rpropto(1,406.0625,3312.9688,760.8510)): 4 roots.

2. (uapprox2.0458762949, vapprox10.3762579057),
   (rpropto(1,176.3771,1224.5627,3144.2226)): 4 roots.

3. (uapprox1.5714595532, vapprox12.1709081349),
   (rpropto(1,776.6280,1524.1222,603.6302)): 4 roots.

## Interpretation
This is exploratory negative evidence only. It does **not** prove (N_{max}(4)=4), does not lower the rigorous upper bound 11, and must not be described in the manuscript as an impossibility result.

The repeated appearance of four roots across geometrically distinct families suggests that the next search should not merely increase random restarts. The higher-value next step is to characterize the four (mathcal C=11) chambers explicitly and constrain optimization to remain inside each one, then use continuation near root-birth (double-root) surfaces satisfying
[
kappa_3(t)=0,qquad kappa_4(t)=0.
]
A new pair of roots can be born or annihilated only through such a multiple-root event (away from domain boundaries). This converts the five-root hunt into a bifurcation search rather than a blind global search.

## Theorem status unchanged
[
oxed{4le N_{max}(4)le11}.
]
