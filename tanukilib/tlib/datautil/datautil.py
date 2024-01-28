import numpy as np
import random
import string
from typing import Any


def gen_scalar_randint(n:int, min_v:int, max_v:int) -> np.ndarray[Any, int]:
    return np.random.randint(min_v, max_v + 1, size = [n])

def gen_rand_alnum_str(n:int) -> str:
    alnums = string.ascii_letters + string.digits
    siz = len(alnums)
    buf = ""
    for _ in range(n):
        buf += alnums[random.randint(0, siz - 1)]
    return buf

def is_str_alnum(s:str) -> bool:
    alnums = string.ascii_letters + string.digits
    for c in s:
        if c not in alnums:
            return False
    return True

