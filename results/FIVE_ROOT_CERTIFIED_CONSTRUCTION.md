# Certified five-root four-level construction

## Exact family

Take four information-gap levels
[
x=left(0,rac{7}{250},rac{57}{400},rac{137}{500}ight)
]
with integer multiplicities
[
r=(1,103,5246,6376).
]

These gaps define a valid probability vector by setting
[
M_i=rac{e^{-x_i}}{Z},qquad
Z=sum_i r_i e^{-x_i},
]
and repeating (M_i) exactly (r_i) times. The actual information levels are (x_i+log Z); the common additive shift leaves all escort central cumulants unchanged.

For (t=1+s), let
[
q_i(t)=rac{r_i e^{-t x_i}}{sum_jr_j e^{-t x_j}},
qquad
kappa_3(t)=sum_iq_i(t)(x_i-mu_t)^3.
]

## Outward-rounded sign certificate

Interval arithmetic gives:

| bracket | left endpoint enclosure | right endpoint enclosure |
|---|---:|---:|
| [2.5,3] | [-4.455212559667971e-6,-4.455212559661384e-6] | [1.215024167923551e-5,1.215024167924140e-5] |
| [19,21] | [2.060723049906782e-5,2.060723049907411e-5] | [-1.244111549561510e-5,-1.244111549560949e-5] |
| [31,34] | [-2.058836362059476e-5,-2.058836362058925e-5] | [2.847380708312678e-5,2.847380708313220e-5] |
| [90,96] | [7.607851531856307e-7,7.607851531856831e-7] | [-5.922891468258661e-7,-5.922891468258342e-7] |
| [160,175] | [-4.206000982172088e-7,-4.206000982171722e-7] | [7.111758647775078e-7,7.111758647775345e-7] |

Each endpoint enclosure excludes zero and every bracket has opposite signs. By continuity, each disjoint bracket contains at least one zero of (kappa_3). Every bracket lies in (t>1), hence all five zeros are physical ((s>0)).

Therefore
[
oxed{N_V(W)ge5}
]
for this exact four-level probability vector, and hence
[
oxed{N_{max}(4)ge5}.
]

Combined with the certified global upper bound,
[
oxed{5le N_{max}(4)le11}.
]

Approximate roots for orientation only:
[
tapprox2.63289037, 20.20352693, 32.35486720, 92.91009793, 165.52204937.
]

## Search-design correction

The discovery required restoring an independent positive scale (a) in
[
x=a(0,1,u,v).
]
Fixing the first information gap to one is legitimate for the all-real-zero sign-variation upper bound, but not for optimization restricted to the physical half-line (t>1), because scaling information gaps rescales root locations relative to the fixed boundary (t=1). This distinction must be retained in all future physical-root searches.
