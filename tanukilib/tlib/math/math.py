import numpy as np
from math import gcd


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
