# Information Dissipation Complexity

This repository supports the mathematical development of finite-level escort-varentropy / information-dissipation complexity.

## Core objects

For a finite probability vector \(W=(w_i)\),

\[
F_W(s)=\sum_i w_i^{1+s},\qquad
q_i(s)=\frac{w_i^{1+s}}{F_W(s)},
\]

and with \(I_i=-\log w_i\),

\[
L(s)=-\log F_W(s),\qquad
L'(s)=\mathbb E_{q_s}[I],\qquad
L''(s)=-V_W(s),\qquad
V_W'(s)=-\kappa_{3,s}.
\]

The exact Rényi bridge is

\[
F_W(s)=e^{-sH_{1+s}(W)}.
\]

The original APG first-order law is recovered as

\[
\delta_{K_P}=\frac{H(W)}2|K_P|+O(K_P^2).
\]

## Established results retained for the paper

- Exact remainder:
  \[
  sH(W)-L(s)=\int_0^s (s-u)V_W(u)\,du.
  \]
- Sum rules:
  \[
  \int_0^\infty V_W(s)\,ds=H-H_\infty,
  \]
  \[
  \int_0^\infty sV_W(s)\,ds=H_\infty-\log r_1.
  \]
- Eventual exponential dissipation and tail recovery from the two largest probability levels.
- Complete two-level classification, including transient information amplification.
- Minimum-coordinate phenomenon: ordinary two-coordinate distributions cannot amplify, while three coordinates can.
- Sharp complexity values:
  \[
  N_{\max}(1)=0,\qquad N_{\max}(2)=1,\qquad N_{\max}(3)=3.
  \]
- For geometric three-level probabilities \(M,Mr,Mr^2\) with multiplicities \(A,B,C\), define
  \[
  \lambda=\frac{B}{\sqrt{AC}},\qquad
  R=r\sqrt{\frac CA}.
  \]
  The critical third-cumulant factor is proportional to
  \[
  (1-y^2)\left[y^2+\left(\frac8\lambda-\lambda\right)y+1\right].
  \]
  The bifurcation occurs at \(\lambda=4\), and \(\lambda>4\) can yield an exact max-min-max varentropy profile with up to three stationary points.
- General pair/triple third-cumulant decomposition:
  \[
  Z^3\kappa_3=
  \sum_{i\ne j}(x_j-x_i)^3u_i^2u_j+
  \sum_{i<j<k}C_{ijk}u_iu_ju_k,
  \]
  where
  \[
  C_{ijk}=(x_i-2x_j+x_k)(x_i+x_j-2x_k)(2x_i-x_j-x_k).
  \]
  In particular,
  \[
  C_{ijk}=0
  \iff x_j=\frac{x_i+x_k}{2}
  \iff M_j^2=M_iM_k.
  \]

## Four-level status

An exact-rational four-level test family currently used is

\[
x=\left(0,\frac14,\frac{15}{28},\frac{55}{56}\right)
\]

with multiplicities

\[
(3,518,2786,135).
\]

Numerically, its escort third cumulant has four distinct sign-changing roots on the physical branch \(t=1+s>1\), approximately

\[
t\approx
1.0861109365,\;
6.1088206474,\;
14.4636946798,\;
19.6436754986.
\]

Thus the current supported lower bound is

\[
N_{\max}(4)\ge 4,
\]

pending a fully rigorous interval-arithmetic certificate of the signs.

A targeted search for a fifth stationary point has not yet produced one. This is **not** evidence that \(N_{\max}(4)=4\); the exact four-level maximum remains open.

## Classical ingredients vs candidate contribution

Rényi entropy, escort distributions, exponential-family cumulant calculus, Prony/Vandermonde reconstruction, and generic exponential-polynomial zero-count machinery are treated as classical.

The candidate contribution is the synthesis

\[
\text{finite probability-level geometry}
\to
\text{escort-varentropy dynamics}
\to
\text{multiplicity bifurcations}
\to
\text{dissipation-transition complexity}.
\]

Novelty claims remain provisional until a deeper prior-art audit is complete.
