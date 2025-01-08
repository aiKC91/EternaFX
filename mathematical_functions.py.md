---
created: 2025-01-08T09:16:25-08:00
modified: 2025-01-08T09:16:27-08:00
---

# mathematical_functions.py

import numpy as np

def calculate_eigenvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

def calculate_eigenvectors(matrix):
    eigenvectors = np.linalg.eig(matrix)[1]
    return eigenvectors
