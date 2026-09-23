# Rigorous interval certificate for the four-root lower bound

Exact family:
[
x=(0,1/4,15/28,55/56),qquad r=(3,518,2786,135).
]
For (t=1+s), define (u_i=r_i e^{-t x_i}), (q_i=u_i/sum_j u_j), and (kappa_3=sum_iq_i(x_i-mu_t)^3).

Outward-rounded interval arithmetic gives:

| bracket | left enclosure | right enclosure |
|---|---:|---:|
| [1.08,1.10] | [6.281054851861676e-6,6.281054851934969e-6] | [-1.420870500506424e-5,-1.420870500498704e-5] |
| [6.10,6.12] | [-5.581944821034507e-6,-5.581944820927224e-6] | [7.076710349129952e-6,7.076710349228127e-6] |
| [14.45,14.48] | [4.737378111076454e-6,4.737378111119413e-6] | [-5.619827113890722e-6,-5.619827113845161e-6] |
| [19.63,19.66] | [-4.717643894760126e-6,-4.717643894731718e-6] | [5.651079037857897e-6,5.651079037887933e-6] |

Every endpoint enclosure is separated from zero and each pair has opposite signs. Continuity gives at least one zero in each disjoint interval. All lie in (t>1), hence (s>0). Therefore (N_V(W)ge4) and (N_{max}(4)ge4).

Together with the global upper bound:
[
oxed{4le N_{max}(4)le11}.
]
