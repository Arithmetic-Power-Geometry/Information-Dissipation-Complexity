# Multiplicity-degeneration boundary for the six-zero problem

## Projective nature of multiplicities

The escort weights are
[
q_i(t)=rac{r_i e^{-t x_i}}{sum_j r_j e^{-t x_j}}.
]
Multiplying every (r_i) by the same positive constant leaves (q_i), all escort moments, and all cumulants unchanged. Thus multiplicities live projectively. Normalize, for example,
[
sum_i r_i=1
]
when studying compact-time limits.

## Vanishing multiplicity on a fixed compact time interval

Suppose (r_k^{(n)}	o0), while the other normalized multiplicities converge to positive limits and the information levels remain in a fixed nondegenerate compact set. For (tin[1,T]),
[
0le
rac{r_k^{(n)}e^{-t x_k^{(n)}}}
{sum_j r_j^{(n)}e^{-t x_j^{(n)}}}
	o0
]
uniformly, because the denominator retains a uniform positive contribution from the surviving levels.

Therefore the escort law, all finite moments, and all cumulants converge locally uniformly (indeed analytically in (t)) to the system obtained by deleting level (k).

For four levels this gives a three-level or lower system. Since the three-level numerator has at most three zeros counting multiplicity, six distinct zeros contained in a common compact physical interval cannot persist into a pure vanishing-multiplicity boundary.

Hence
[
oxed{	ext{six compact physical zeros cannot escape through pure projective multiplicity deletion}.}
]

## Apparent multiplicity blow-up

A statement such as (r_k/r_j	oinfty) is not a separate projective boundary. After normalizing (sum r_i=1), it becomes one or more other multiplicities tending to zero. Thus, on a fixed compact time interval and with nondegenerate information levels, multiplicity blow-up reduces to the same support-deletion analysis.

## Important mixed-boundary caveat

There is a distinct phenomenon if a multiplicity ratio diverges while the relevant zero times also drift. For two levels,
[
rac{r_j e^{-t x_j}}{r_i e^{-t x_i}}
=
rac{r_j}{r_i}e^{-t(x_j-x_i)},
]
so a diverging ratio can be balanced by a time shift of order
[
tasymp rac{log(r_j/r_i)}{x_j-x_i}.
]
This is precisely why multiplicity degeneration combined with tail escape must not be treated as simple support deletion.

The uniform-tail lemma already controls tail escape when multiplicity ratios are uniformly bounded. When ratios degenerate, a moving-time recentering may reveal a nontrivial lower-level transition layer. That mixed regime needs a separate rescaling lemma.

## Consequence

Pure multiplicity degeneration at bounded physical times is now controlled. The unresolved noncompact cases are narrowed to:
1. multiplicity degeneration coupled to moving times;
2. scale degeneration;
3. zero-time collisions / multiple roots;
4. mixed combinations;
5. compact separated interior.

The global theorem remains
[
oxed{5le N_{max}(4)le11}.
]
