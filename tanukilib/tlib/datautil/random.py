import numpy as np
import random
import string
from typing import Any


def gen_scalar_randint(n: int, min_v: int, max_v: int) -> np.ndarray[Any, int]:
    """Generate scalar array with random int with specified min and max range"""
    return np.random.randint(min_v, max_v + 1, size=[n])


def gen_rand_alnum_str(n: int) -> str:
    """generate random alphanumeric string with length n"""
    alnums = string.ascii_letters + string.digits
    siz = len(alnums)
    buf = ""
    for _ in range(n):
        buf += alnums[random.randint(0, siz - 1)]
    return buf


class MultiClassRandDataGen:
    """
    Generate multiple different items with specified percentage.
    In order to generate random data, registration must sum percentrage to 100
    """

    def __init__(self):
        self.current_max_percentage = 0
        self.generators = []

    def add(self, percentage: int, generator) -> None:
        """
        register generator with given percentage.
        If sum of percentage goes beyond 100, then error is returned
        """
        if self.current_max_percentage + percentage > 100:
            raise ValueError("total percentrage is over 100")
        for _ in range(self.current_max_percentage, self.current_max_percentage + percentage):
            self.generators.append(generator)
        self.current_max_percentage += percentage

    def get_current_percentage(self) -> int:
        """
        Get current percentage sum
        """
        return self.current_max_percentage

    def gen(self) -> Any:
        """
        generate random data. If current percentage sum not reach to 100,
        then error is raised.
        """
        if self.current_max_percentage != 100:
            raise Exception("total percentrage is over 100")
        randv = random.randint(0, 99)
        print(randv)
        return self.generators[randv]()
