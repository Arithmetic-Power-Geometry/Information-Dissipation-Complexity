# Exact Feasible Rate-Equality Lines for d=4

Normalize the four distinct information levels to
[
x=(0,1,u,v),qquad 1<u<v.
]

Among the 33 distinct formal equalities between the 16 pair/triple exponential rates, exactly 10 normalized affine lines intersect the admissible open wedge. In canonical form (A+Bu+Cv=0), they are

[
egin{array}{rcl}
2u-v&=&0,\\
1-2u+v&=&0,\\
1+u-v&=&0,\\
1+2u-2v&=&0,\\
1+2u-v&=&0,\\
2-2u+v&=&0,\\
2-u&=&0,\\
2-v&=&0,\\
2+u-2v&=&0,\\
2+u-v&=&0.
end{array}
]

Equivalently:
[
v=2u,; v=2u-1,; v=u+1,; v=u+	frac12,; v=2u+1,
]
[
v=2u-2,; u=2,; v=2,; v=	frac{u+2}{2},; v=u+2.
]

This corrects the earlier provisional human-readable line list. The computational derivation enumerates all 16 rates, forms all pairwise differences, canonicalizes proportional affine equations, and tests intersection with (1<u<v) by linear programming.

The next exact step is arrangement-cell enumeration from these 10 lines, followed by a symbolic coefficient-sign certificate in every cell. Only after that step should the observed 24 chambers and candidate maximum sign variation 11 be promoted to a theorem.
