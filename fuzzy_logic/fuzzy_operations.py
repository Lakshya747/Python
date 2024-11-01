from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class FuzzySet:
    """ A class for representing and manipulating triangular fuzzy sets. """
    name: str
    left_boundary: float
    peak: float
    right_boundary: float

    def __str__(self) -> str:
        return (
            f"{self.name}: [{self.left_boundary}, {self.peak}, {self.right_boundary}]"
        )

    def complement(self) -> FuzzySet:
        """ Calculate the complement (negation) of this fuzzy set. """
        return FuzzySet(
            f"¬{self.name}",
            1 - self.right_boundary,
            1 - self.left_boundary,
            1 - self.peak,
        )

    def intersection(self, other) -> FuzzySet:
        """ Calculate the intersection of this fuzzy set with another fuzzy set. """
        return FuzzySet(
            f"{self.name} ∩ {other.name}",
            max(self.left_boundary, other.left_boundary),
            min(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def membership(self, x: float) -> float:
        """ Calculate the membership value of an input 'x' in the fuzzy set. """
        if x <= self.left_boundary or x >= self.right_boundary:
            return 0.0
        elif self.left_boundary < x <= self.peak:
            return (x - self.left_boundary) / (self.peak - self.left_boundary)
        elif self.peak < x < self.right_boundary:
            return (self.right_boundary - x) / (self.right_boundary - self.peak)
        msg = f"Invalid value {x} for fuzzy set {self}"
        raise ValueError(msg)

    def union(self, other) -> FuzzySet:
        """ Calculate the union of this fuzzy set with another fuzzy set. """
        return FuzzySet(
            f"{self.name} U {other.name}",
            min(self.left_boundary, other.left_boundary),
            max(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def plot(self):
        """ Plot the membership function of the fuzzy set. """
        x = np.linspace(0, 1, 1000)
        y = [self.membership(xi) for xi in x]

        plt.plot(x, y, label=self.name)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    a = FuzzySet("A", 0, 0.5, 1)
    b = FuzzySet("B", 0.2, 0.7, 1)

    a.plot()
    b.plot()

    plt.xlabel("x")
    plt.ylabel("Membership")
    plt.legend()
    plt.show()

    union_ab = a.union(b)
    intersection_ab = a.intersection(b)
    complement_a = a.complement()

    union_ab.plot()
    intersection_ab.plot()
    complement_a.plot()

    plt.xlabel("x")
    plt.ylabel("Membership")
    plt.legend()
    plt.show()
