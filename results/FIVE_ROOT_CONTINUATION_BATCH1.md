# Continuation from the certified five-root family — Batch 1

## Seed

Exact certified family:
[
x=(0,7/250,57/400,137/500),qquad r=(1,103,5246,6376).
]

Its five physical sign-changing roots are approximately
[
tapprox2.6329, 20.2035, 32.3549, 92.9101, 165.5220.
]

## Executed local search

A scale-aware local differential-evolution search was run around the certified family in six logarithmic coordinates:
- one positive information-gap scale (a);
- two normalized shape coordinates (u,v);
- three independent multiplicity ratios.

Six independent differential-evolution restarts were used, each with population size 15 and 100 generations. Root counting used a mixed dense grid over (1<t<1000).

## Result

Every restart attained at most five physical sign-changing roots. No six-root candidate was found in this batch.

An additional diagnostic extended the seed-family root count to (t>0), including the region below the physical boundary (t=1). The seed still exhibited exactly five positive-(t) sign-changing roots and no hidden positive root below (t=1).

Therefore changing only the common positive information-gap scale cannot expose a sixth positive root for this seed. A stronger construction requires a genuine shape/multiplicity deformation that creates an additional root pair (or changes the positive-root structure), not merely movement of an existing root across the physical boundary.

## Interpretation

This is negative computational evidence only. It does not prove (N_{max}(4)=5), nor does it lower the certified upper bound 11.

The certified theorem remains
[
oxed{5le N_{max}(4)le11}.
]

## Next mathematical target

The next search should target creation of an additional pair directly. Rather than optimizing root count on a plateau, solve a constrained multiple-root system near high-complexity geometry:
[
kappa_3(t_*)=0,qquad kappa_4(t_*)=0,
]
while simultaneously requiring the remaining trajectory to retain the existing five-root pattern away from (t_*). This is a codimension-aware continuation problem and is more selective than unconstrained double-root solving.
