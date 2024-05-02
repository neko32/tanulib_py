from tlib.awt.cache import *
from unittest import TestCase, main


class InMemCacheTest(TestCase):

    def test_basic_ops(self):
        mem = InMemCache()
        mem.add("abc", "takonga")
        mem.add("xyz", "bayaya")
        self.assertEqual(mem.size(), 2)
        self.assertEqual(mem.get("xyz", "<NA>"), "bayaya")
        self.assertEqual(mem.get("mno", "<NA>"), "<NA>")
        self.assertEqual(mem.evict("abc"), "takonga")
        self.assertEqual(mem.size(), 1)
        mem.add(32, 100.25)
        print(f"{mem}")
        self.assertEqual(mem.get(32, -1), 100.25)


if __name__ == "__main__":
    main()