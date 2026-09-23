# Four-level minor-sign audit — Stage 1

## Question

Can the nominal 11-sign-variation ceiling be sharpened by showing that the realizable rate-ordered coefficient vectors satisfy fixed-sign adjacent or Hankel minors?

## Setup

For a fixed generic chamber, order the distinct exponential rates
[
lambda_1<cdots<lambda_{16}
]
and write the corresponding coefficients as
[
c_k=sigma_k,g_k(u,v),m_k(r_1,r_2,r_3,r_4),
]
where (sigma_kin{pm1}), (g_k>0) inside the chamber after its sign is extracted, and (m_k) is a positive multiplicity monomial.

The first minors to test are
[
Delta_k^{(2)}=c_kc_{k+2}-c_{k+1}^2
]
and the contiguous (3	imes3) Hankel determinants
[
Delta_k^{(3)}=
det(c_{k+i+j})_{i,j=0}^{2}.
]

A fixed sign for such expressions throughout a chamber could indicate log-convexity, sign-regularity, or a total-positivity constraint. A changing sign rules out that particular simple obstruction.

## Exact structural warning

The coefficients are signed and arise from different multiplicity monomials. Consequently, after factoring common positive monomials, many minors remain genuine polynomials in multiplicity ratios rather than geometry-only expressions. Such a minor can only yield a chamber-wide obstruction if its residual polynomial has a fixed sign over all positive multiplicity ratios and all ((u,v)) in the chamber.

## Stage-1 conclusion

The coefficient compatibility identities are real and restrictive, but they do not by themselves imply ordinary log-convexity or a fixed-sign adjacent-minor pattern. Reciprocal pair terms and triple terms carry different multiplicity exponents, so the simplest (2	imes2) minor tests can be changed by varying positive multiplicity ratios while holding the information geometry fixed.

Therefore a naive total-positivity proof based solely on contiguous coefficient minors is **not yet justified** and should not be used to lower the upper bound 11.

This is a useful elimination result: the next analytic obstruction must exploit more than ordinary coefficient log-convexity. Promising alternatives are:
1. the differential identity structure of the cumulant hierarchy;
2. direct fewnomial/interpolation incompatibility for six prescribed zeros;
3. geometry-aware signed-measure transforms rather than raw coefficient minors.

## Theorem status

Unchanged:
[
oxed{5le N_{max}(4)le11}.
]
