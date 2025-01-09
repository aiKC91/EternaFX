---
created: 2025-01-08T09:15:29-08:00
modified: 2025-01-09T00:01:33-08:00
---

# zeta_function.py

import numpy as np
from mpmath import zetazero, zeta

def calculate_zeta_values(REAL_RANGE, IMAG_RANGE):
    zeta_values = np.zeros((len(REAL_RANGE), len(IMAG_RANGE)))
    for i, real in enumerate(REAL_RANGE):
        for j, imag in enumerate(IMAG_RANGE):
            zeta_values[i, j] = abs(zeta(complex(real, imag))) 
    return zeta_values

def extract_critical_zeros(n):
    critical_zeros = zetazero(n)
    return critical_zeros---
created: 2025-01-08T09:15:29-08:00
modified: 2025-01-08T09:15:50-08:00
---

# zeta_function.py

import numpy as np
from mpmath import zetazero, zeta

def calculate_zeta_values(REAL_RANGE, IMAG_RANGE):
    zeta_values = np.zeros((len(REAL_RANGE), len(IMAG_RANGE)))
    for i, real in enumerate(REAL_RANGE):
        for j, imag in enumerate(IMAG_RANGE):
            zeta_values[i, j] = abs(zeta(complex(real, imag))) 
    return zeta_values

def extract_critical_zeros(n):
    critical_zeros = zetazero(n)
    return critical_zeros
