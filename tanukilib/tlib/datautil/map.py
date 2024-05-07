from typing import Generic, TypeVar, Optional, Dict, List, Tuple
import os

K = TypeVar('K')
Q = TypeVar('Q')
V = TypeVar('V')


class DualKeyMap(Generic[K, Q, V]):
    """
    Support Dict with 2 keys
    """

    def __init__(self):
        self.dict = {}
        self.iter_index = 0

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self) -> Tuple[K, Q, V]:
        if self.iter_index < len(self.dict):
            keys = list(self.dict.keys())
            vals = list(self.dict.values())
            (k, q) = keys[self.iter_index]
            v = vals[self.iter_index]
            self.iter_index += 1
            return (k, q, v)
        else:
            raise StopIteration

    def put(self, k: K, q: Q, v: V) -> None:
        """put item with dual key"""
        self.dict[(k, q)] = v

    def get_by_dualkey(self, k: K, q: Q) -> Optional[V]:
        """get item by dual key"""
        if (k, q) in self.dict:
            return self.dict[(k, q)]
        else:
            return None

    def get_by_k(self, k: K) -> Optional[V]:
        """
        get item by first key k.
        NOTE: this case calculation is not O(1) but O(N)
        """
        for (dict_k, _), v in self.dict.items():
            if k == dict_k:
                return v
        return None

    def get_by_q(self, q: Q) -> Optional[V]:
        """
        get item by second key q.
        NOTE: this case calculation is not O(1) but O(N)
        """
        for (_, dict_q), v in self.dict.items():
            if q == dict_q:
                return v
        return None


def gen_hist(ls: List[V], by_n: int = 1) -> Tuple[Dict[V, int], str]:
    """
    Generate histgram of value occurence in l.
    Histgram's dot is accumulated by by_n
    """
    h = {}
    sumk = 0
    for v in ls:
        if v in h:
            h[v] += 1
        else:
            h[v] = 1
        sumk += 1
    buf = ""
    sumv = 0
    for k, v in h.items():
        buf += f"{k}:{__hist_mark_gen(v, by_n)}{os.linesep}"
        sumv += v
    buf += f"total number of keys:{sumk}{os.linesep}"
    buf += f"total number of values:{sumv}{os.linesep}"

    return (h, buf)


def __hist_mark_gen(val: int, by_n: int) -> str:
    """Generate marks for val by by_n accumulator"""
    if by_n == 1:
        return "".join(["*"] * (val // by_n))
    else:
        return "".join(["*"] * ((val // by_n) + 1))


def pprint(d: Dict[K, V]) -> None:
    """Pretty print the given dict"""
    for k, v in d.items():
        print(f"{k} : {v}")


def pprint_with_sort(d: Dict[K, V], asc: bool = True) -> None:
    """Pretty print the given dict after sorting key"""
    ks = sorted(d.keys(), reverse=not asc)
    for k in ks:
        print(f"{k} : {d[k]}")
