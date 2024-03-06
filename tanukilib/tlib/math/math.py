import numpy as np

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("msut be positive")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def calc_npr(n: int, r: int) -> int:
    if n < r:
        raise ValueError(f"{n} must be bigger than or equal to {r}")
    sumv = 1
    lim = (n - r) + 1
    while n >= lim:
        sumv *= n
        n -= 1
    return sumv


def calc_ncr(n: int, r: int) -> int:
    numerator = calc_npr(n, r)
    denominator = factorial(r)
    return numerator // denominator


def sigmoid(x: float) -> float:
    return 1 / (1. + np.exp(-x))
