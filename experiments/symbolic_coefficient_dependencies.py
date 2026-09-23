"""Symbolic identities for constrained four-level kappa3 coefficients.

This script is an algebraic audit, not a zero-bound proof.
"""
import sympy as sp
ri,rj,rk=sp.symbols('r_i r_j r_k', positive=True)
xi,xj,xk=sp.symbols('x_i x_j x_k', real=True)
Aij=(xj-xi)**3*ri**2*rj
Ajk=(xk-xj)**3*rj**2*rk
Aki=(xi-xk)**3*rk**2*ri
C=(xi-2*xj+xk)*(xi+xj-2*xk)*(2*xi-xj-xk)
B=C*ri*rj*rk
compat=sp.factor(B**3/(Aij*Ajk*Aki))
print("B^3/(Aij Ajk Aki) =",compat)
# Expected: geometry-only rational function (including orientation sign).
