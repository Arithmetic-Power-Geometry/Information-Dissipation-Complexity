"""Seeded continuation strategy for high-complexity four-level bifurcations.

Use this after importing exact representatives of the four C=11 chambers.
The purpose is to start from known four-root families / high-variation
geometry and seek nearby kappa3=kappa4 loci, rather than low-complexity loci
throughout the whole wedge.

Paper rule: numerical output is exploratory until rationalized and interval
certified.
"""
# Planned continuation:
# 1. load the four C=11 chamber representatives from the chamber certificate;
# 2. impose their ten wall-sign inequalities as constraints;
# 3. seed multiplicities from known four-root families and broad log-ratio clouds;
# 4. solve kappa3=kappa4 for t plus one continuation parameter;
# 5. perturb transversely and count roots on both sides;
# 6. retain only transitions with max(side counts) >= 5;
# 7. rationalize/integerize and interval-certify any retained family.
