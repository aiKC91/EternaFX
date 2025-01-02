import matplotlib.pyplot as plt
import numpy as np
from core.golden_ratio import PHI

class PrimeGapVisualizer:
    @staticmethod
    def visualize(prime_gaps, gap_ratios):
        plt.figure(figsize=(12, 6))
        plt.plot(prime_gaps, label="Prime Gaps", marker="o", color="blue")
        plt.axhline(y=np.mean(prime_gaps), color="red", linestyle="--", label="Mean Gap")
        plt.axhline(y=PHI, color="gold", linestyle="--", label="Golden Ratio")
        plt.title("Prime Gaps Visualization")
        plt.xlabel("Index")
        plt.ylabel("Gap Size")
        plt.legend()
        plt.grid()

        plt.figure(figsize=(12, 6))
        plt.plot(gap_ratios, label="Gap Ratios", marker="x", color="green")
        plt.axhline(y=PHI, color="gold", linestyle="--", label="Golden Ratio")
        plt.title("Prime Gap Ratios")
        plt.xlabel("Index")
        plt.ylabel("Ratio")
        plt.legend()
        plt.grid()
        plt.show()