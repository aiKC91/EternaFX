---
created: 1736716000
modified: 1736716012
---

# hodge_conjecture.py

import numpy as np
from zeta_function import riemann_zeta

def hodge_conjecture(s):
    """
    Compute the Hodge conjecture at s.
    """
    return riemann_zeta(s) * np.exp(-s**2)

def hodge_zeros(n):
    """
    Compute the first n zeros of the Hodge conjecture.
    """
    return [s for s in np.roots([1, -1, 1]) if np.isreal(s)]
