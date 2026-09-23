# Direct six-zero feasibility program

## Question

Can a four-level escort-varentropy trajectory have six distinct physical stationary points?

A six-root family would require six ordered times
[
1<t_1<t_2<cdots<t_6
]
such that
[
kappa_3(t_j)=0,qquad j=1,ldots,6.
]

## Parameterization

Use the scale-aware four-level geometry
[
x=a(0,1,u,v),qquad a>0,quad1<u<v,
]
three independent positive multiplicity ratios, and six positive time increments
[
t_j=1+sum_{kle j}e^{	au_k}.
]
This enforces the physical domain and strict ordering automatically.

The residuals are normalized by the cube of the information span. This is essential: without normalization, an optimizer can create a false near-solution simply by collapsing all information gaps toward zero, since (kappa_3) scales cubically.

## Logical status

This is an incompatibility *search*, not an incompatibility proof.

- A genuine six-zero solution would immediately disprove the conjecture (N_{max}(4)=5) and become a candidate for exact certification.
- Persistent nonzero residuals, even across many starts, are only numerical evidence.
- A proof of (N_{max}(4)=5) would require an analytic certificate: elimination, sign-definite resultant/minor, Chebyshev restriction, or another rigorous obstruction valid for all admissible parameters.

## Why this is stronger than blind root maximization

The optimizer is asked to satisfy all six zero equations simultaneously rather than hoping six crossings appear on a sampling grid. It also exposes degeneracies directly: time collisions, geometry collapse, or roots escaping to infinity can be diagnosed from the optimized variables.

The certified theorem remains
[
oxed{5le N_{max}(4)le11}
]
until a rigorous obstruction or stronger certified construction is obtained.
