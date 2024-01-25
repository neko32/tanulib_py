import numpy as np
from typing import Any


def gen_scalar_randint(n:int, min_v:int, max_v:int) -> np.ndarray[Any, int]:
    return np.random.randint(min_v, max_v + 1, size = [n])
