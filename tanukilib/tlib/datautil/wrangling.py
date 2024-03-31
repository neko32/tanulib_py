import numpy as np
from numpy.typing import NDArray
from typing import Tuple
import pandas as pd


def binarize(
        data: NDArray,
        pred,
        verify: bool = True) -> NDArray:
    """
    Binarize given data based on pred's outcome.
    if verify is True and vectonized array has non 0 or 1 value,
    then AssertionError is thrown.
    """
    v_pred = np.vectorize(pred)
    b = v_pred(data)
    binalized_rez = [0, 1]
    v = [True if x in binalized_rez else False for x in b.ravel()]
    if not verify:
        return v_pred
    elif verify and all(v):
        return v_pred(data)
    else:
        raise AssertionError("binalized results contain non 0/non 1 value")


def discretize_by_fixed_space(
        a: NDArray,
        expected_num: int = 10
) -> Tuple[NDArray, float]:
    if expected_num <= 1:
        raise AssertionError("expected num must be more than equal 2")
    if len(a.shape) != 1:
        raise AssertionError("Currently only single dim is supported")
    minv = np.min(a)
    maxv = np.max(a)
    lin = np.linspace(minv, maxv, expected_num)
    bin = lin[1] - lin[0]
    return (np.array([x // bin for x in a]), bin)

def discretize_by_quantile(
        a: NDArray
) -> NDArray:
    s = pd.Series(a)
    qs = pd.qcut(s, 4, labels = False)
    return qs.to_numpy()
