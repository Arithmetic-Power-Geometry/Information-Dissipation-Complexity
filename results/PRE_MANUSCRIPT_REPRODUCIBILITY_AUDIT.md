# Reproducibility audit before manuscript drafting

Date: 2026-09-24.

Two headline computational ingredients were independently rerun before manuscript freezing.

## Five-root interval certificate

The script experiments/interval_certify_five_roots.py was rerun independently. All five endpoint interval enclosures reproduced with the recorded signs for the brackets
[2.5,3], [19,21], [31,34], [90,96], and [160,175].
Thus the exact four-level family continues to certify at least five physical roots.

## Four-level chamber enumeration

An initial rerun of experiments/certify_four_level_generic_chambers.py exposed a numerical representative-point defect: one LP representative could lie effectively on a triple-coefficient sign wall, yielding the spurious histogram {4:1,5:11,7:6,9:2,11:4} although the number of feasible sign regions remained 24.

An independent rate-order sampling/enumeration reproduced the intended generic result:
24 chambers with histogram {5:12,7:6,9:2,11:4}, maximum variation 11.

The finite-certificate script was therefore corrected to maximize an explicit common signed-wall margin and to reject non-generic zero coefficient signs. This places each representative strictly inside its feasible chamber rather than arbitrarily near a wall.

Manuscript use: report the 24-chamber histogram and maximum 11 only from the corrected certificate and analytic boundary-merging argument.
