from tlib.math import *
import numpy as np
from unittest import TestCase, main


class MathTest(TestCase):

    def test_factorial(self):
        pair = [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24),
                (5, 120), (6, 720), (7, 5040), (8, 40320),
                (9, 362880), (10, (3628800))]
        for ipt, expected in pair:
            self.assertEqual(factorial(ipt), expected)
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_npr(self):
        self.assertEqual(calc_npr(6, 2), 30)
        self.assertEqual(calc_npr(9, 4), 3024)
        self.assertEqual(calc_npr(1, 1), 1)
        self.assertEqual(calc_npr(4, 0), 1)
        self.assertEqual(calc_npr(3, 1), 3)
        self.assertEqual(calc_npr(7, 7), 5040)
        with self.assertRaises(ValueError):
            calc_npr(3, 4)
            calc_npr(-3, 2)
            calc_npr(6, -2)

    def test_ncr(self):
        self.assertEqual(calc_ncr(9, 2), 36)
        self.assertEqual(calc_ncr(9, 7), 36)
        self.assertEqual(calc_ncr(4, 2), 6)
        self.assertEqual(calc_ncr(1, 1), 1)
        self.assertEqual(calc_ncr(2, 1), 2)
        self.assertEqual(calc_ncr(6, 6), 1)
        self.assertEqual(calc_ncr(6, 0), 1)
        with self.assertRaises(ValueError):
            calc_ncr(3, 4)
            calc_ncr(-2, 5)
            calc_ncr(6, -2)

    def test_sigmoid(self):
        xl = np.arange(-5., 5., step=0.5)
        prev_y = -1
        for x in xl:
            y = sigmoid(x)
            self.assertTrue(y >= 0. and y <= 1. and prev_y < y)
            prev_y = y

    def test_coprime(self):
        self.assertTrue(is_coprime(8, 9))
        self.assertFalse(is_coprime(6, 9))


if __name__ == "__main__":
    main()
