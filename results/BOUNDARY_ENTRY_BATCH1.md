# Boundary-entry search from the certified five-root family — Batch 1

## Executed experiment

The scale-aware boundary continuation was executed around the certified family
[
x=(0,7/250,57/400,137/500),qquad r=(1,103,5246,6376).
]

A batch of 180 randomized local anchors was used. Nonlinear least squares targeted
[
kappa_3(1)=0.
]
Candidates were retained only when (|kappa_3(1)|<2\times10^{-8}) and (|kappa_4(1)|>10^{-9}), excluding numerically degenerate boundary crossings.

135 transverse boundary solutions passed these filters.

For each accepted solution, all six gap/multiplicity coordinates were perturbed on both sides (steps 0.02 and 0.05), and the complete sign-changing root count was recomputed on a mixed grid over (1<t\le1000).

## Result

The largest physical root count observed was
[
oxed{5}.
]
No six-root family was found in this local boundary batch.

## Interpretation

This is negative computational evidence only. It does not prove that a six-root family cannot arise through the (t=1) boundary elsewhere in parameter space.

The result does suggest that the certified five-root family is not immediately adjacent, under the tested local perturbations, to a simple boundary crossing that raises the count to six.

The next targeted mechanism is therefore the interior bifurcation surface
[
kappa_3(t_*)=kappa_4(t_*)=0,qquad t_*>1,
]
searched locally around the certified five-root family with the absolute information scale retained. A nondegenerate crossing can change the root count by two, making a (5\to7) transition the natural target.

## Certified theorem status

Unchanged:
[
oxed{5\le N_{\max}(4)\le11}.
]
