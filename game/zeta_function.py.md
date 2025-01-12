---
created: 1736715881
modified: 1736715897
---

# zeta_function.py

import numpy as np
from mpmath import zetazero, zeta

def riemann_zeta(s):
    """
    Compute the Riemann zeta function at s.
    """
    return zeta(s)

def zeta_zeros(n):
    """
    Compute the first n zeros of the Riemann zeta function.
    """
    return [zetazero(i) for i in range(1, n+1)]
