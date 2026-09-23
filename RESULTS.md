# Current Results Ledger

## Exact / proved in the working derivation

1. \(F_W(s)=\sum_i w_i^{1+s}\).
2. \(F_W(s)=e^{-sH_{1+s}(W)}\).
3. \(\delta_{K_P}=H(W)|K_P|/2+O(K_P^2)\).
4. \(L'(s)=E_{q_s}[I]\), \(L''(s)=-V_s\), \(V_s'=-\kappa_{3,s}\).
5. \(sH-L(s)=\int_0^s(s-u)V_u\,du\).
6. \(\int_0^\infty V=H-H_\infty\).
7. \(\int_0^\infty sV=H_\infty-\log r_1\).
8. Eventual exponential dissipation and tail recovery.
9. Complete two-level transition classification.
10. Transient information amplification criterion for two distinct probability levels with multiplicity.
11. Two coordinates cannot transiently amplify; three coordinates can.
12. Three geometric levels admit an exact two-parameter phase diagram with bifurcation \(\lambda=4\).
13. Arbitrary three-distinct-level complexity is sharply \(N_{\max}(3)=3\).
14. General pair/triple decomposition of \(Z^3\kappa_3\).
15. Signed-Laplace / rate-ordered variation-complexity viewpoint.
16. Conservative all-\(d\) structural ceiling from at most
   \[
   d(d-1)+\binom d3
   =\frac{d(d-1)(d+4)}6
   \]
   structural exponential terms.

## Four-level computational status

Exact rational information levels:
\[
\left(0,\frac14,\frac{15}{28},\frac{55}{56}\right)
\]

Integer multiplicities:
\[
(3,518,2786,135).
\]

Observed roots of \(\kappa_3(t)\):
\[
1.0861109364518937,
6.108820647433962,
14.463694679810832,
19.643675498550763.
\]

Therefore current working lower bound:
\[
N_{\max}(4)\ge4.
\]

A fresh targeted random search around and beyond this construction tested 12,000 parameter draws over broad gap and multiplicity ranges and found no five-root example; the best count remained four. This is exploratory only and must not be reported as an upper bound.

## Open problems

- Find a five-root four-level construction, if one exists.
- Otherwise derive a rigorous four-level upper bound.
- Determine exact \(N_{\max}(4)\).
- Derive the general sharp complexity law \(N_{\max}(d)\), if one exists.
- Replace floating-point sign checks by rigorous interval arithmetic for the four-root rational family.
- Complete prior-art audit before asserting novelty.
