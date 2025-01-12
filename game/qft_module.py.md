---
created: 1736715900
modified: 1736715911
---

# qft_module.py

import numpy as np
from zeta_function import riemann_zeta

def quantum_field_theory(s):
    """
    Compute the quantum field theory amplitude at s.
    """
    return riemann_zeta(s) * np.exp(-s**2)

def qft_zeros(n):
    """
    Compute the first n zeros of the quantum field theory amplitude.
    """
    return [s for s in np.roots([1, -1, 1]) if np.isreal(s)]
