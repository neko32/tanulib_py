
from unittest import TestCase, main
from tlib.datautil.vector import *


class VectorTest(TestCase):

    def test_dedupe(self):
        v = [2, 11, 25, 30, 11, 9, 6, 3, 25, 3, 2, 48, 5, 30]
        expected = [2, 11, 25, 30, 9, 6, 3, 48, 5]
        deduped = dedupe(v)
        self.assertListEqual(deduped, expected)


    def test_coalesce(self):
        v = [None, None, 23, None, 35, 40]
        self.assertEqual(coalesce(v), 23)
        w = [None, None, None]
        self.assertIsNone(coalesce(w))


if __name__ == "__main__":
    main()
