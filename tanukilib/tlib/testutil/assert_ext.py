from numpy.typing import NDArray
from numpy.testing import assert_array_equal


def is_ndarray_equal(a: NDArray, b: NDArray, verbose: bool = False) -> bool:
    """
    do equal comparision against 2 NDArrays
    """
    try:
        assert_array_equal(a, b)
        return True
    except AssertionError as aE:
        if verbose:
            print(aE)
        return False
