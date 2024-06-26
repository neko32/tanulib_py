from typing import List, TypeVar, Optional
from numpy.lib.stride_tricks import as_strided
from numpy.typing import NDArray
import numpy as np

T = TypeVar('T')


def dedupe(ls: List[T]) -> List[T]:
    """
    Dedupe items in the list. Note this ops is not in place action.
    """
    s = set()
    t = []
    for x in ls:
        if x not in s:
            t.append(x)
            s.add(x)
    return t


def coalesce(ls: List[Optional[T]]) -> Optional[T]:
    """
    Return the first non-None element in ls.
    If all None, then None is returned
    """
    filtered = filter(lambda x: x is not None, ls)
    for item in filtered:
        return item
    return None


def ngram(v: List[T], window: int) -> List[T]:
    """
    Derive v's n-gram with given window size.
    Item size (which is required to derive the n-gram) is assumed by first elem of v
    """
    itemsize = np.dtype(type(v[0])).itemsize
    return as_strided(
        v,
        shape=[len(v) - window + 1, window],
        strides=[itemsize, itemsize]
    )


def discard_till(v: List[T], key: T, discard_key_line: bool = False) -> List[T]:
    """Discard list's items till key is found"""
    newv = []
    found = False
    found_idx = -1
    for idx, val in enumerate(v):
        if not found and val == key:
            found = True
            found_idx = idx

        if found:
            if not discard_key_line and found_idx == idx:
                newv.append(val)
            elif discard_key_line and found_idx == idx:
                pass
            else:
                newv.append(val)

    return newv


def pprint(v: List[T]) -> None:
    """Print each item with line breaking"""
    for elem in v:
        print(elem)


def find_single_dupe(v: List[int]) -> int:
    """
    Assume there's single dupe number, find it.
    If v contains multiple dupes not single one, then the output becomes sum of dupes.
    """
    return sum(v) - sum(set(v))


def transform_tensor_with_fixed_2d_bottom(n: NDArray, deep_dim: tuple[int, int]) -> NDArray:
    """
    Transform array n to array with X number of dimensions which has deep_dim dimensions at bottom
    """
    return np.reshape(n, [-1, deep_dim[0], deep_dim[1]])


def transform_tensor_with_folded_1d_bottom(n: NDArray, deep_dim: int) -> NDArray:
    """
    Transform array n to array with X number of dimensions which has deep_dim dimensions at bottom
    """
    return np.reshape(n, [-1, deep_dim])


def transform_tensor_with_fixed_top(n: NDArray, top_dim: int) -> NDArray:
    """
    Transform array n to array with X number of top dimension
    """
    return np.reshape(n, [top_dim, -1])


def transform_tensor_with_fixed_2d(a: NDArray, m: int, n: int) -> NDArray:
    """
    Transform array n to array with dimension (m, n)
    """
    return np.reshape(a, [m, n])
