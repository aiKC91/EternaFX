---
created: 1736715922
modified: 1736715927
---

# navier_stokes.py

import numpy as np
from zeta_function import riemann_zeta

def navier_stokes(u, v):
    """
    Compute the Navier-Stokes equations at (u, v).
    """
    return riemann_zeta(u) * np.exp(-v**2)

def ns_zeros(n):
    """
    Compute the first n zeros of the Navier-Stokes equations.
    """
    return [u for u in np.roots([1, -1, 1]) if np.isreal(u)]
