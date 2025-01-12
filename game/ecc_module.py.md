---
created: 1736715933
modified: 1736715936
---

# ecc_module.py

import numpy as np
from zeta_function import riemann_zeta

def elliptic_curve(a, b):
    """
    Compute the elliptic curve at (a, b).
    """
    return riemann_zeta(a) * np.exp(-b**2)

def ecc_zeros(n):
    """
    Compute the first n zeros of the elliptic curve.
    """
    return [a for a in np.roots([1, -1, 1]) if np.isreal(a)]
