
from unittest import TestCase, main
from tlib.datautil.vector import *
from numpy.testing import assert_array_equal


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

    def test_ngram(self):
        intv = [7, 4, 8, 10, 9, 5, 6, 3]
        fv = [2.718, 3.442, 5.22, 6.0, 17.3]
        fv_2g = np.array([
            [2.718, 3.442],
            [3.442, 5.22],
            [5.22, 6.0],
            [6.0, 17.3]
        ])
        fv_3g = np.array([
            [2.718, 3.442, 5.22],
            [3.442, 5.22, 6.0],
            [5.22, 6.0, 17.3]
        ])
        iv_3g = np.array([
            [7, 4, 8],
            [4, 8, 10],
            [8, 10, 9],
            [10, 9, 5],
            [9, 5, 6],
            [5, 6, 3]
        ])
        iv_4g = np.array([
            [7, 4, 8, 10],
            [4, 8, 10, 9],
            [8, 10, 9, 5],
            [10, 9, 5, 6],
            [9, 5, 6, 3]
        ])
        try:
            assert_array_equal(ngram(intv, 3), iv_3g)
            assert_array_equal(ngram(intv, 4), iv_4g)
            assert_array_equal(ngram(fv, 2), fv_2g)
            assert_array_equal(ngram(fv, 3), fv_3g)
        except AssertionError as e:
            print(e)
            self.assertTrue(False)




if __name__ == "__main__":
    main()
