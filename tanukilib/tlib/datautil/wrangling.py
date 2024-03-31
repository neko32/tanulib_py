import numpy as np
from numpy.typing import NDArray


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
