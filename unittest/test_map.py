from unittest import TestCase, main
from tlib.datautil.map import *
import random


class TestMap(TestCase):

    def test_dualkeymap(self):

        dkm = DualKeyMap()
        dkm.put(1, "tako", 27.45)
        dkm.put(2, "poko", 30.40)
        self.assertTrue(dkm.get_by_dualkey(1, "tako"), 27.45)
        self.assertTrue(dkm.get_by_k(2), 30.40)
        self.assertTrue(dkm.get_by_q("tako"), 27.45)

    def test_dump_hist(self):

        ls = [7, 3, 1, 10, 5, 3, 3, 7, 8, 10, 2, 5, 3]
        hist_expected = {1: 1, 2: 1, 3: 4, 5: 2, 7: 2, 8: 1, 10: 2}
        hist, summary = gen_hist(ls, 1)
        print(hist)
        print(summary)
        self.assertDictEqual(hist, hist_expected)
        a = [int(random.normalvariate(50, 10)) for _ in range(10000)]
        _, summary = gen_hist(a, 50)
        print(summary)


if __name__ == "__main__":
    main()
