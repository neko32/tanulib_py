from typing import List, TypeVar, Optional
from numpy.lib.stride_tricks import as_strided
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
    filtered = filter(lambda x:x is not None, ls)
    for item in filtered:
        return item
    return None


def ngram(v: List[T], window:int) -> List[T]:
    """
    Derive v's n-gram with given window size.
    Item size (which is required to derive the n-gram) is assumed by first elem of v
    """
    itemsize = np.dtype(type(v[0])).itemsize
    return as_strided(
        v,
        shape = [len(v) - window + 1, window],
        strides = [itemsize, itemsize]
    )
