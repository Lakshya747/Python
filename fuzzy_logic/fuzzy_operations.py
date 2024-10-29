from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt

import numpy as np

@dataclass
class FuzzySet:
    """
    A class for representing and manipulating triangular fuzzy sets.
    """
    name: str
    left_boundary: float
    peak: float
    right_boundary: float

    def __str__(self) -> str:
        return f"{self.name}: [{self.left_boundary}, {self.peak}, {self.right_boundary}]"

    def complement(self) -> FuzzySet:
        return FuzzySet(
            f"¬{self.name}",
            1 - self.right_boundary,
            1 - self.left_boundary,
            1 - self.peak,
        )

    def intersection(self, other: FuzzySet) -> FuzzySet:
        return FuzzySet(
            f"{self.name} ∩ {other.name}",
            max(self.left_boundary, other.left_boundary),
            min(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def membership(self, x: float) -> float:
        if x <= self.left_boundary or x >= self.right_boundary:
            return 0.0
        elif self.left_boundary < x <= self.peak:
            return (x - self.left_boundary) / (self.peak - self.left_boundary)
        elif self.peak < x < self.right_boundary:
            return (self.right_boundary - x) / (self.right_boundary - self.peak)
        
        msg = f"Invalid value {x} for fuzzy set {self}"
        raise ValueError(msg)

    def union(self, other: FuzzySet) -> FuzzySet:
        return FuzzySet(
            f"{self.name} U {other.name}",
            min(self.left_boundary, other.left_boundary),
            max(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def plot(self):
        x = np.linspace(0, 1, 1000)
        y = [self.membership(xi) for xi in x]
        plt.plot(x, y, label=self.name)
        plt.xlabel("x")
        plt.ylabel("Membership")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # Sample Fuzzy Sets
    a = FuzzySet("A", 0, 0.5, 1)
    b = FuzzySet("B", 0.2, 0.7, 1)

    # Plot the fuzzy sets
    a.plot()
    b.plot()

    # Plot union, intersection, and complement of sets
    a.union(b).plot()
    a.intersection(b).plot()
    a.complement().plot()
