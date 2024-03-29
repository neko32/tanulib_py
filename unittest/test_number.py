from tlib.datautil import *
from unittest import TestCase, main
import numpy as np


class DataUtilTest(TestCase):

    def test_gen_scalar_randint(self):
        r = gen_scalar_randint(10000, 0, 100)

        self.assertTrue(np.all(r >= 0) and np.all(r <= 100))

    def test_gen_rand_alnum_str(self):
        n = 15
        outs = [gen_rand_alnum_str(n) for _ in range(10)]
        self.assertTrue(any([is_str_alnum(s) for s in outs]))
        self.assertTrue(all([len(s) == n for s in outs]))

    def test_round_to_nearest_half_up(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_to_nearest_half_up(v, 0)
        self.assertEqual(round_to_nearest_half_up(v, 1), 251)
        self.assertEqual(round_to_nearest_half_up(v, 2), 250.7)
        self.assertEqual(round_to_nearest_half_up(v, 3), 250.73)
        nv = -250.7259
        with self.assertRaises(Exception):
            round_to_nearest_half_up(nv, 0)
        self.assertEqual(round_to_nearest_half_up(nv, 1), -251)
        self.assertEqual(round_to_nearest_half_up(nv, 2), -250.7)
        self.assertEqual(round_to_nearest_half_up(nv, 3), -250.73)

    def test_round_to_nearest_half_down(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_to_nearest_half_down(v, 0)
        self.assertEqual(round_to_nearest_half_down(v, 1), 251)
        self.assertEqual(round_to_nearest_half_down(v, 2), 250.7)
        self.assertEqual(round_to_nearest_half_down(v, 3), 250.73)  # wrong?
        nv = -250.7259
        with self.assertRaises(Exception):
            round_to_nearest_half_up(nv, 0)
        self.assertEqual(round_to_nearest_half_down(nv, 1), -251)
        self.assertEqual(round_to_nearest_half_down(nv, 2), -250.7)
        self.assertEqual(round_to_nearest_half_down(nv, 3), -250.73)  # wrong?

    def test_round_to_nearest_half_even(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_to_nearest_half_even(v, 0)
        self.assertEqual(round_to_nearest_half_even(v, 1), 251)
        self.assertEqual(round_to_nearest_half_even(v, 2), 250.7)
        self.assertEqual(round_to_nearest_half_even(v, 3), 250.73)  # wrong?
        nv = -250.7259
        with self.assertRaises(Exception):
            round_to_nearest_half_even(nv, 0)
        self.assertEqual(round_to_nearest_half_even(nv, 1), -251)  # wrong?
        self.assertEqual(round_to_nearest_half_even(nv, 2), -250.7)
        self.assertEqual(round_to_nearest_half_even(nv, 3), -250.73)

    def test_round_truncate(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_truncate(v, 0)
        self.assertEqual(round_truncate(v, 1), 250)
        self.assertEqual(round_truncate(v, 2), 250.7)
        self.assertEqual(round_truncate(v, 3), 250.72)
        nv = -250.7259
        with self.assertRaises(Exception):
            round_truncate(nv, 0)
        self.assertEqual(round_truncate(nv, 1), -250)
        self.assertEqual(round_truncate(nv, 2), -250.7)
        self.assertEqual(round_truncate(nv, 3), -250.72)

    def test_round_up(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_up(v, 0)
        self.assertEqual(round_up(v, 1), 251)
        self.assertEqual(round_up(v, 2), 250.8)
        self.assertEqual(round_up(v, 3), 250.73)
        nv = -250.7259
        with self.assertRaises(Exception):
            round_up(nv, 0)
        self.assertEqual(round_up(nv, 1), -251)
        self.assertEqual(round_up(nv, 2), -250.8)
        self.assertEqual(round_up(nv, 3), -250.73)

    def test_round_floor(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_truncate(v, 0)
        self.assertEqual(round_floor(v, 1), 250)
        self.assertEqual(round_floor(v, 2), 250.7)
        self.assertEqual(round_floor(v, 3), 250.72)
        nv = -250.7259
        with self.assertRaises(Exception):
            round_floor(nv, 0)
        self.assertEqual(round_floor(nv, 1), -251)
        self.assertEqual(round_floor(nv, 2), -250.8)
        self.assertEqual(round_floor(nv, 3), -250.73)

    def test_round_ceil(self):
        v = 250.7259
        with self.assertRaises(Exception):
            round_ceil(v, 0)
        self.assertEqual(round_ceil(v, 1), 251)
        self.assertEqual(round_ceil(v, 2), 250.8)
        self.assertEqual(round_ceil(v, 3), 250.73)
        nv = -250.7259
        with self.assertRaises(Exception):
            round_ceil(nv, 0)
        self.assertEqual(round_ceil(nv, 1), -250)
        self.assertEqual(round_ceil(nv, 2), -250.7)
        self.assertEqual(round_ceil(nv, 3), -250.72)

    def test_two_compliment(self):
        with self.assertRaises(ValueError):
            get_two_complement(3)
        th = from_binary_to_hex
        self.assertEqual(th(get_two_complement(-1)).lower(), "0xffffffff")
        self.assertEqual(th(get_two_complement(-1, 16)).lower(), "0xffff")
        self.assertEqual(th(get_two_complement(-1, 8)).lower(), "0xff")
        self.assertEqual(th(get_two_complement(-17)).lower(), "0xffffffef")


if __name__ == "__main__":
    main()
