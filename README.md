# Information Dissipation Complexity

A reproducible computational laboratory for finite-level escort-varentropy dynamics, transition counting, exponential-polynomial structure, chamber geometry, and interval-certified four-level examples.

## Mathematical setting

For a finite probability vector (W=(w_i)), define the power-sum deformation

[
F_W(s)=\sum_i w_i^{1+s}, \qquad s\ge 0,
]

with logarithmic form (L_W(s)=-\log F_W(s)). The associated escort distribution is

[
q_i(s)=\frac{w_i^{1+s}}{F_W(s)},
]

and the information values are (I_i=-\log w_i).

The computational work in this repository uses the derivative hierarchy

[
L'_W(s)=\mathbb E_{q_s}[I], \qquad
L''_W(s)=-V_s, \qquad
V'_s=-\kappa_{3,s},
]

where (V_s) is escort varentropy and (kappa_{3,s}) is the third cumulant of information under the escort law. Consequently, stationary points of escort varentropy are zeros of a structured exponential polynomial.

The exact Rényi bridge is

[
F_W(s)=e^{-sH_{1+s}(W)}.
]

## Transition-counting problem

For distinct probability levels, switch to (t=1+s>1), write the distinct information levels as (x_1<\cdots<x_d), and define

[
u_j(t)=r_j e^{-t x_j}, \qquad
Q_j(t)=\frac{u_j(t)}{\sum_k u_k(t)}.
]

The quantity tested computationally is

[
N_V(W)=\#\{t>1:\kappa_3(t)=0\},
]

counting multiplicity where appropriate. The experiments therefore reduce information-dissipation transitions to finite zero-counting and sign-certification tasks.

## Exact identities used by the experiments

The implementation is built around the following identities:

[
sH(W)-L_W(s)=\int_0^s (s-u)V_u\,du
=s\{H(W)-H_{1+s}(W)\},
]

[
\int_0^\infty V_s\,ds=H-H_\infty,
\qquad
\int_0^\infty sV_s\,ds=H_\infty-\log r_1.
]

For two levels, with information gap (Delta) and upper-level escort mass (R(t)),

[
V(t)=\Delta^2R(t)(1-R(t)),
]

[
V'(t)=-\Delta^3R(t)(1-R(t))(1-2R(t)).
]

This gives at most one physical transition.

## Three-level structure

For three distinct levels the third-cumulant numerator is a seven-term real exponential polynomial. Rate ordering and coefficient-sign analysis give at most three sign variations, and explicit geometric families attain three transitions.

For geometrically spaced probability levels (M,Mr,Mr^2) with multiplicities (A,B,C), define

[
\lambda=\frac{B}{\sqrt{AC}},
\qquad
R=r\sqrt{\frac CA},
\qquad
y=Rr^s.
]

Up to a positive factor,

[
\kappa_3(s)\sim
(1-y^2)
\left[
y^2+
\left(\frac8\lambda-\lambda\right)y+1
\right].
]

The bifurcation occurs at (lambda=4). For (lambda>4), the quadratic contributes two additional positive candidate roots,

[
y_\pm=
\frac{\lambda-8/\lambda
\pm\sqrt{(\lambda-8/\lambda)^2-4}}{2},
\qquad
y_-y_+=1.
]

This produces zero-, one-, two-, or three-transition regimes depending on the initial value (R).

## Pair-triple decomposition

For arbitrary finite level count,

[
Z^3\kappa_3=
\sum_{i\ne j}(x_j-x_i)^3u_i^2u_j+
\sum_{i<j<k}C_{ijk}u_i u_j u_k,
]

where

[
C_{ijk}=
(x_i-2x_j+x_k)
(x_i+x_j-2x_k)
(2x_i-x_j-x_k).
]

The genuine triple interaction vanishes exactly when the middle information level is the arithmetic mean of the outer two, equivalently when the corresponding probability levels are in geometric progression.

## Four-level chamber certificate

For four information levels, translation and positive rescaling reduce the generic rate geometry to

[
x=(0,1,u,v), \qquad 1<u<v.
]

The pair-triple expansion has 12 ordered-pair atoms and 4 triple atoms. Rate ordering and triple-coefficient signs change only across ten affine walls. The chamber program enumerates all (2^{10}) wall-sign patterns, solves a strict-margin feasibility problem for each candidate chamber, orders the resulting exponential rates, combines collisions where necessary, and counts coefficient sign variation.

The corrected enumeration returns exactly 24 generic chambers with histogram:

| coefficient sign variation | number of chambers |
|---:|---:|
| 5 | 12 |
| 7 | 6 |
| 9 | 2 |
| 11 | 4 |

The maximum generic variation is 11. Boundary rate collisions are handled by coefficient merging, which cannot increase sign variation.

## Interval-certified five-transition witness

The explicit four-level test geometry is

[
x=\left(0,\frac{7}{250},\frac{57}{400},\frac{137}{500}\right),
\qquad
r=(1,103,5246,6376).
]

Five disjoint physical brackets are tested:

[
[2.5,3],\quad
[19,21],\quad
[31,34],\quad
[90,96],\quad
[160,175].
]

Outward-rounded interval evaluation gives opposite nonzero signs of (kappa_3) at the two endpoints of every bracket. Continuity therefore certifies at least one distinct zero in each bracket.

The current certified four-level range is

[
5\le N_{\max}(4)\le 11.
]

## Stable numerical kernel

For levels (x_i), multiplicities (r_i), and parameter (t), the numerical routines use log-weights

[
a_i=\log r_i-tx_i,
\qquad
\widetilde u_i=e^{a_i-\max_j a_j},
\qquad
Q_i=\frac{\widetilde u_i}{\sum_j\widetilde u_j}.
]

Central moments are then evaluated under (Q), followed by

[
V=\mu_2,\qquad
\kappa_3=\mu_3,\qquad
\kappa_4=\mu_4-3\mu_2^2,\qquad
\kappa_5=\mu_5-10\mu_3\mu_2.
]

This log-sum-exp normalization is used to avoid avoidable underflow in long-(t) calculations.

## Reproducibility workflow

The repository separates exploratory computation from finite certification:

1. derive and simplify the finite-level cumulant formulas;
2. explore parameter families and candidate transition patterns;
3. replace promising numerical examples by exact rational gaps and integer multiplicities;
4. enumerate the complete four-level affine chamber arrangement;
5. use strict interior representatives for generic sign-variation counts;
6. certify explicit root brackets with outward-rounded interval arithmetic;
7. save machine-readable outputs and diagnostic figures under `results/`.

The chamber certificate and the five-root interval certificate are the finite computations intended for direct reproducibility. Exploratory searches are retained separately and should not be confused with certificates.

## Repository layout

- `experiments/` — computational searches, chamber enumeration, and certification scripts.
- `results/` — generated numerical tables, certificates, and diagnostic artifacts.
- `notes/` — mathematical and computational development notes.
- `RESULTS.md` — compact record of currently certified computational results.
- `CITATION.cff` — citation metadata.

## Software

The computational stack uses Python with NumPy and SciPy for numerical exploration and finite feasibility, Matplotlib for diagnostic figures, and arbitrary-precision interval arithmetic for certified endpoint signs.

## Citation

Akhtar, M. A. K. (2026). *Power-Sum Deformation and Information-Dissipation Complexity: Sharp Low-Level Transition Theory and Four-Level Bounds* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22931055
