# Exact four-level chamber certificate

Normalize the distinct information levels to
[
x=(0,1,u,v),qquad 1<u<v.
]

## Ten canonical walls

All rate collisions that meet the admissible wedge reduce to the ten affine equations
[
2u-v=0,quad 1-2u+v=0,quad 1+u-v=0,quad 1+2u-2v=0,quad 1+2u-v=0,
]
[
2-2u+v=0,quad 2-u=0,quad 2-v=0,quad 2+u-2v=0,quad 2+u-v=0.
]

The triple coefficients factor as
[
C_{123}=(u-2)(u+1)(2u-1),
]
[
C_{124}=(v-2)(v+1)(2v-1),
]
[
C_{134}=(u-2v)(u+v)(2u-v),
]
[
C_{234}=(u-2v+1)(u+v-2)(2u-v-1).
]
Inside (1<u<v), every possible triple-coefficient sign change therefore lies on one of the same ten walls. Hence the ten-line arrangement controls both rate ordering and coefficient signs.

## Finite chamber count

Each open chamber is determined by the signs of the ten affine wall functions. For any prescribed sign vector, its feasible set is an intersection of open half-planes with the wedge (1<u<v), hence convex and therefore connected. Consequently each feasible sign vector corresponds to exactly one chamber.

Exhaustive feasibility testing of all (2^{10}=1024) sign vectors gives 24 feasible open sign vectors. Thus the arrangement has 24 generic chambers.

The accompanying script performs the complete finite enumeration and independently computes the rate ordering and coefficient-sign sequence in every feasible chamber.

The resulting sign-variation histogram is
[
egin{array}{c|cccc}
mathcal C&5&7&9&11\\
#	ext{ chambers}&12&6&2&4.
end{array}
]

Therefore the maximum chamber variation is
[
mathcal C_4=11.
]

Combined with the classical generalized Descartes/variation-diminishing theorem for real exponential sums, this yields
[
N_V(W)le 11
]
for every four-distinct-level finite probability vector, provided coincident-rate boundary cases are handled by combining equal-rate coefficients. Boundary collisions cannot be inferred solely from the generic chamber count; the boundary audit is the final step before promoting the statement to the manuscript theorem.

Together with the explicit four-root construction, the current rigorous-interior / boundary-pending bracket is
[
4le N_{max}(4)le 11.
]

Do not label the upper bound fully proved in the manuscript until the lower-dimensional wall/intersection audit is completed.
