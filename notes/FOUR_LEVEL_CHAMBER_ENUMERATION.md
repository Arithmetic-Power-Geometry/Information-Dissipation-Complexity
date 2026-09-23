# Four-Level Chamber Enumeration — Reduced Geometry

Normalize distinct information levels to

[
(0,1,u,v),qquad 1<u<v.
]

The 12 ordered-pair rates (2x_i+x_j) and four triple rates (x_i+x_j+x_k) generate 33 distinct formal rate-equality lines. After feasibility reduction, only the following 10 lines intersect the admissible open wedge (1<u<v):

[
v=2u,quad v=2u-1,quad v=u+1,quad v=u+2,
]
[
v=u+2 	ext{(rate equality represented after normalization where applicable)},quad
v=2u+1,quad 2v=2u+1,quad 2v=u+2,quad v=2,quad u=2.
]

**Important:** the executable enumeration script is the authoritative source for the exact normalized line list; duplicate algebraic renderings must be simplified before this list is quoted in a manuscript.

Computational arrangement sampling identifies 24 generic rate-order chambers. Their observed coefficient-sign variation distribution is:

| variation | number of sampled generic chambers |
|---:|---:|
| 5 | 12 |
| 7 | 6 |
| 9 | 2 |
| 11 | 4 |

Thus every generic chamber encountered has odd variation, and the largest observed value is 11.

This materially strengthens the earlier dense-scan observation, but it is still recorded as a **computational chamber-enumeration result**, not yet a proof that the arrangement has exactly 24 chambers or that 11 is the global realizable maximum. The next proof step is to derive the arrangement cells exactly from the 10 feasible lines and verify one symbolic sign/order certificate per cell.

The four variation-11 chambers are the only highest-priority regions for a targeted search for five or more actual roots. Variation count is only an upper bound; it does not imply that the bound is attainable.

Classical input: ordered exponential sums obey a Descartes-type zero bound by coefficient sign changes. This classical theorem is not claimed as new.
