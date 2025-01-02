import numpy as np
from sympy import primerange
from scipy.fftpack import fft
from core.golden_ratio import phi_scale, phi_harmonic_series

class PrimeGapAnalyzer:
    """
    Includes references to advanced math breakthroughs:
    Riemann Hypothesis, Navier–Stokes, etc. for scenario generation.
    """
    def __init__(self, prime_limit=1000):
        self.prime_limit = prime_limit
        self.primes = self.generate_primes()
        self.prime_gaps = self.calculate_prime_gaps()
        self.gap_ratios = self.calculate_gap_ratios()
        self.wave_patterns = None

    def generate_primes(self):
        return list(primerange(2, self.prime_limit))

    def calculate_prime_gaps(self):
        gaps = [self.primes[i+1] - self.primes[i] for i in range(len(self.primes)-1)]
        return [phi_scale(gap) for gap in gaps]

    def calculate_gap_ratios(self):
        return [self.prime_gaps[i+1]/self.prime_gaps[i] for i in range(len(self.prime_gaps)-1)]

    def detect_wave_patterns(self):
        self.wave_patterns = np.abs(fft(self.prime_gaps))
        return phi_harmonic_series(len(self.wave_patterns))