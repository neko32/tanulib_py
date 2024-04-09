from unittest import TestCase, main
from tlib.datautil import DualKeyMap


class TestMap(TestCase):

    def test_dualkeymap(self):

        dkm = DualKeyMap()
        dkm.put(1, "tako", 27.45)
        dkm.put(2, "poko", 30.40)
        self.assertTrue(dkm.get_by_dualkey(1, "tako"), 27.45)
        self.assertTrue(dkm.get_by_k(2), 30.40)
        self.assertTrue(dkm.get_by_q("tako"), 27.45)


if __name__ == "__main__":
    main()
