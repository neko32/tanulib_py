from typing import List, TypeVar

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
