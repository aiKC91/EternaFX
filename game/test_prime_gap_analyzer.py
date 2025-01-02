import pytest
from ai.prime_gap_analyzer import PrimeGapAnalyzer

def test_prime_generation():
    analyzer = PrimeGapAnalyzer(prime_limit=30)
    assert len(analyzer.primes) > 0
    assert all(analyzer.primes[i] < analyzer.primes[i+1] for i in range(len(analyzer.primes)-1))

def test_gap_calculation():
    analyzer = PrimeGapAnalyzer(prime_limit=50)
    assert len(analyzer.prime_gaps) == len(analyzer.primes) - 1