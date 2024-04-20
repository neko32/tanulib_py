from unittest import TestCase, main
from tlib.tree.suffix_tree import *


class SuffixTreeTest(TestCase):

    def test_suffixtree(self):
        t = SuffixTree("tako")
        print(t.get_tree_copy())
        self.assertTrue(t.search('tako'))
        self.assertTrue(t.search('ako'))
        self.assertTrue(t.search('ko'))
        self.assertTrue(t.search('o'))
        self.assertFalse(t.search('wako'))
        self.assertFalse(t.search('taka'))
        self.assertFalse(t.search('tak'))
        self.assertFalse(t.search('ak'))
        self.assertFalse(t.search('kor'))
        self.assertFalse(t.search('takoo'))
        self.assertFalse(t.search('takeo'))
        self.assertFalse(t.search('t'))
        self.assertFalse(t.search('k'))


if __name__ == "__main__":
    main()
