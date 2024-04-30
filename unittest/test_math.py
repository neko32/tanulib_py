from tlib.math import *
from tlib.datautil.number import round_up, round_to_nearest_half_up
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

    def test_polynominal_derivative_with_m4(self):
        adash, bdash, cdash = polynominal_derivative_by_mat4(1, 5, 4, 5)
        self.assertListEqual([adash, bdash, cdash], [3, 10, 4])

    def test_coordinates(self):
        coord2d = Coordinate(3., 7.)
        coord3d = Coordinate(1., 2., 0.)
        self.assertEqual(coord2d.x, 3.)
        self.assertEqual(coord2d.y, 7.)
        self.assertIsNone(coord2d.z)
        self.assertEqual(coord3d.x, 1.)
        self.assertEqual(coord3d.y, 2.)
        self.assertEqual(coord3d.z, 0.)
        self.assertTupleEqual(coord2d.as_tuple2d(), (3., 7.))
        self.assertTupleEqual(coord3d.as_tuple3d(), (1., 2., 0.))

    def test_cosaine_similarity(self):
        vec_a = Coordinate(3, 1)
        vec_b = Coordinate(1, 3)
        cs_similar = round_up(cosaine_similarity2d(vec_a, vec_b), 2)
        self.assertEqual(cs_similar, 0.6)

        vec_c = Coordinate(3, 0)
        vec_d = Coordinate(0, 2)
        cs_unrelated = round_up(cosaine_similarity2d(vec_c, vec_d), 2)
        self.assertEqual(cs_unrelated, 0.)

        vec_e = Coordinate(2, 1)
        vec_f = Coordinate(-2, -1)
        cs_unsimilar = round_up(cosaine_similarity2d(vec_e, vec_f), 2)
        self.assertEqual(cs_unsimilar, -1.)

    def test_get_y_by_theta_and_x(self):
        theta = 45.
        x = 10.
        y = round_to_nearest_half_up(derive_yloc_by_theta_and_x(theta, x), 3)
        self.assertEqual(y, 53.64)

    def test_can_make_triangle(self):
        non_tr = [13, 15, 30]
        tr = [10, 20, 15]
        self.assertFalse(can_make_triangle(non_tr[0], non_tr[1], non_tr[2]))
        self.assertTrue(can_make_triangle(tr[0], tr[1], tr[2]))

    def test_logit(self):
        like_choco = 8    
        like_bean = 2
        sample_num = like_choco + like_bean
        like_choco_p = like_choco / sample_num
        like_bean_p = like_bean / sample_num
        like_odds = odds_ratio(like_choco_p, like_bean_p)
        like_choco_o = odds(like_choco_p)
        like_bean_o = odds(like_bean_p)
        like_choco_logit = logit(like_choco_p)
        like_bean_logit = logit(like_bean_p)
        self.assertEqual(int(like_odds), 16)
        self.assertEqual(int(like_choco_o), 4)
        self.assertEqual(like_bean_o, 0.25)
        self.assertEqual(round_to_nearest_half_up(like_choco_logit, 3), 1.39)
        self.assertEqual(round_to_nearest_half_up(like_bean_logit, 3), -1.39)
        
    def test_avg_change_formula(self):
        case1_f1_rez = -7
        case1_f2_rez = 3
        case1_f1_ipt = 0
        case1_f2_ipt = 9
        case1_r = avg_change_formula(case1_f1_rez, case1_f2_rez, case1_f1_ipt, case1_f2_ipt)
        self.assertEqual(round_to_nearest_half_up(case1_r, 2), 1.1)

        case2_f1_rez = -8
        case2_f2_rez = 162
        case2_f1_ipt = 1
        case2_f2_ipt = 6
        case2_r = avg_change_formula(case2_f1_rez, case2_f2_rez, case2_f1_ipt, case2_f2_ipt)

        self.assertEqual(round_to_nearest_half_up(case2_r, 2), 34.0)





if __name__ == "__main__":
    main()
