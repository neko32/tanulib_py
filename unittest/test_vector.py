
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

    def test_discard_till(self):
        v1 = ["tako", "neko", "pako", "pako", "poko", "piko"]
        v1_1 = discard_till(v1, "pako", True)
        v1_2 = discard_till(v1, "pako", False)
        self.assertListEqual(v1_1, ["pako", "poko", "piko"])
        self.assertListEqual(v1_2, ["pako", "pako", "poko", "piko"])

        v2 = []
        v2 = discard_till(v2, "")
        self.assertListEqual(v2, [])

        v3 = ["tako", "miko", "puko"]
        v3_1 = discard_till(v3, "ziko")
        v3_2 = discard_till(v3, "tako")
        v3_3 = discard_till(v3, "tako", True)
        self.assertListEqual(v3_1, [])
        self.assertListEqual(v3_2, ["tako", "miko", "puko"])
        self.assertListEqual(v3_3, ["miko", "puko"])

    def test_pprint(self):
        v = ["tako", "neko", "poko"]
        pprint(v)

    def test_find_single_dupe(self):
        v = [1, 2, 2, 4]
        self.assertEqual(find_single_dupe(v), 2)
        v = [3]
        self.assertEqual(find_single_dupe(v), 0)
        v = [1, 2, 3, 4]
        self.assertEqual(find_single_dupe(v), 0)
        v = []
        self.assertEqual(find_single_dupe(v), 0)
        v = [1, 2, 2, 2, 4]
        self.assertEqual(find_single_dupe(v), 4)
        v = [1, 2, 2, 2, 4, 4]
        self.assertEqual(find_single_dupe(v), 8)


if __name__ == "__main__":
    main()
