from unittest import TestCase, main

from tlib.datautil.wrangling import *
from tlib.testutil import is_ndarray_equal
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
        self.assertTrue(is_ndarray_equal(a, expected))

    def test_binarlize_bad_pred(self):
        a = np.array([3, 8, 7, 2, 5, 6, 10, 4, 3])
        a = np.reshape(a, [3, 3])
        with self.assertRaises(AssertionError):
            binarize(a, lambda x: 5 if x >= 5 else 0)

    def test_discretize_by_fixed_space(self):
        a = np.array([12.5, 7.3, 2.9, 4.8, 15.5, 3.7, 5.6, 8.9])
        rank = np.array([2, 1, 0, 1, 3, 0, 1, 2])
        b, bin = discretize_by_fixed_space(a, 4)
        print(b)
        print(bin)
        self.assertTrue(is_ndarray_equal(b, rank))

    def test_discretize_by_quartile(self):
        a = np.array([12.5, 7.3, 2.9, 4.8, 15.5, 3.7, 5.6, 8.9])
        expected = np.array([3, 2, 0, 1, 3, 0, 1, 2])
        q = discretize_by_quantile(a)
        self.assertTrue(is_ndarray_equal(q, expected))

    def test_logarithmic_conv(self):
        a = np.array(
            [
                5732343, 323272, 34832, 33023, 11234,
                2332, 980, 450, 103, 20, 10, 7, 0
            ]
        )
        b = logaritmic_conv(a)
        self.assertTrue(all([True if x < 10 else False for x in b]))


if __name__ == "__main__":
    main()
