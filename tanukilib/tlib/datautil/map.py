from typing import Generic, TypeVar, Optional

K = TypeVar('K')
Q = TypeVar('Q')
V = TypeVar('V')


class DualKeyMap(Generic[K, Q, V]):
    """
    Support Dict with 2 keys
    """

    def __init__(self):
        self.dict = {}

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
