import math

PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio constant

def phi_scale(value: float, factor: float = 1.0) -> float:
    """Scales a value using the Golden Ratio."""
    return round(value * (PHI ** factor), 8)

def phi_inverse_scale(value: float, factor: float = 1.0) -> float:
    """Scales a value using the inverse of PHI."""
    return round(value / (PHI ** factor), 8)

def phi_harmonic_series(n: int) -> list:
    """Generates a harmonic series based on the Golden Ratio."""
    return [round(PHI / (i + 1), 8) for i in range(n)]