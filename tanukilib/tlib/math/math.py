import numpy as np
from numpy.linalg import norm
from typing import Tuple, Optional
from math import gcd


class Coordinate:
    """Represents 2D or 3D coordinate on Euclid space"""

    def __init__(self, x: float, y: float, z: Optional[float] = None):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> Optional[float]:
        return self._z

    def as_tuple2d(self) -> Tuple[float, float]:
        """Return tuple of x and y"""
        return (self._x, self._y)

    def as_tuple3d(self) -> Tuple[float, float, Optional[float]]:
        """Return tuple of x, y and z"""
        return (self._x, self._y, self._z)


def factorial(n: int) -> int:
    """
    Calculate factorial
    """
    if n < 0:
        raise ValueError("msut be positive")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def calc_npr(n: int, r: int) -> int:
    """Calculate permutation nPr"""
    if n < r:
        raise ValueError(f"{n} must be bigger than or equal to {r}")
    sumv = 1
    lim = (n - r) + 1
    while n >= lim:
        sumv *= n
        n -= 1
    return sumv


def calc_ncr(n: int, r: int) -> int:
    """Calculate combination nCr"""
    numerator = calc_npr(n, r)
    denominator = factorial(r)
    return numerator // denominator


def sigmoid(x: float) -> float:
    """calculate sigmoid x"""
    return 1 / (1. + np.exp(-x))


def is_coprime(m: int, n: int) -> bool:
    """checks whether m and n are co-prime or not"""
    return gcd(m, n) == 1


def cosaine_similarity2d(a: Coordinate, b: Coordinate) -> float:
    """
    Calculate cosaine similarty for 2 coordinates a and b.
    As the value closes to -1, 2 vecs are unsimilar.
    As the value closes to 1, 2 vecs are similar.
    As the value closes to 0, 2 vecs are unrelated.
    """
    am = np.array(a.as_tuple2d())
    bm = np.array(b.as_tuple2d())
    m = am.dot(bm)
    n1 = norm(am, ord=2)
    n2 = norm(bm, ord=2)
    n = n1 * n2
    return m / n
