from unittest import TestCase, main

from tlib.datautil.wrangling import *
from numpy.testing import assert_array_equal
import numpy as np


class WranglerTest(TestCase):

    def test_binarlize(self):
        a = np.array([3, 8, 7, 2, 5, 6, 10, 4, 3])
        expected = np.array([
            [0, 1, 1],
            [0, 1, 1],
            [1, 0, 0]
        ])
        a = np.reshape(a, [3, 3])
        a = binarize(a, lambda x: 1 if x >= 5 else 0)
        try:
            assert_array_equal(a, expected)
        except AssertionError as ae:
            print(ae)
            self.assertTrue(False)

    def test_binarlize_bad_pred(self):
        a = np.array([3, 8, 7, 2, 5, 6, 10, 4, 3])
        a = np.reshape(a, [3, 3])
        with self.assertRaises(AssertionError):
            binarize(a, lambda x: 5 if x >= 5 else 0)


if __name__ == "__main__":
    main()
