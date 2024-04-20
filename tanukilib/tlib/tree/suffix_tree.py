from typing import Dict, Any


class SuffixTree:
    """Build and maintain suffix tree for a given string"""

    def __init__(self, input: str, term_c: str = '*') -> None:
        self.raw_input = input
        self._h = {}
        self.term_c = term_c
        for i in range(len(input)):
            subst = input[i:]
            self._build(subst, term_c)

    def _build(self, s: str, term_c: str) -> None:
        """Build suffix tree of s with term_c"""
        p = self._h

        for c in s:
            if c not in p:
                h = {}
                p[c] = h
                p = p[c]

        p[term_c] = True

    def get_tree_copy(self) -> Dict[Any, Any]:
        """get copy of suffix tree built"""
        return self._h.copy()

    def search(self, key: str) -> bool:
        """search key through the built suffix tree"""
        p = self._h
        for c in key:
            if c in p:
                p = p[c]
            else:
                return False
        return self.term_c in p and p[self.term_c]
