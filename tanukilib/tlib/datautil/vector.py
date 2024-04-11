from typing import List, TypeVar, Optional

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
