# Targeted four-level root search protocol

## Goal
Improve the certified lower bound in
[
4le N_{max}(4)le11
]
by finding a four-distinct-level family with at least five physical stationary points.

## Why target the high-variation chambers
The finite chamber certificate shows only four of the 24 generic chambers have coefficient sign variation 11. Variation is an upper bound, not a prediction of attained zeros. Search therefore optimizes actual sign changes of the escort third cumulant on (t=1+s>1).

## Search variables
Normalize information levels as
[
x=(0,1,u,v),quad1<u<v.
]
Overall multiplicity scale cancels, so optimize three independent positive multiplicity ratios. Log coordinates enforce positivity and permit many orders of magnitude.

## Acceptance pipeline
A numerical candidate is never promoted directly to a paper theorem. A successful candidate must pass:
1. dense-grid discovery of 5+ separated sign changes;
2. high-precision root refinement;
3. rationalization of (u,v) and integerization of multiplicity ratios;
4. re-verification that all roots remain on (t>1);
5. outward-rounded interval sign certificates on disjoint brackets;
6. addition to the manuscript result registry only after certification.

## Negative-result policy
Failure to find five roots is exploratory evidence only and cannot improve the upper bound or establish (N_{max}(4)=4).

## Current target
Run multiple differential-evolution restarts, then concentrate local searches around the best families. The accompanying script is the reproducible starting point.
