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
        
    def test_uuid(self):
        s = gen_uuidv4()
        self.assertTrue(is_valid_uuidv4(s))
        self.assertFalse(is_valid_uuidv4("takoneko-nekotako"))

    def test_get_uuid_version(self):
        valid_uuid1 = "e4cccba0-c63f-11ee-a506-0242ac120002"
        valid_uuid2 = "000003e8-c640-21ee-9400-325096b39f47"
        valid_uuid3 = "3f703955-aaba-3e70-a3cb-baff6aa3b28f"
        valid_uuid4 = "3f72d10b-d705-4115-99e0-9534fcfb4f75"
        valid_uuid5 = "a8f6ae40-d8a7-58f0-be05-a22f94eca9ec"
        invalid_uuid1 = "adsdf"
        invalid_uuid2 = "a8f6ae40-d8a7--8f0-be05-a22f94eca9ec"

        self.assertEqual(get_uuid_version(valid_uuid1), 1)
        self.assertEqual(get_uuid_version(valid_uuid2), 2)
        self.assertEqual(get_uuid_version(valid_uuid3), 3)
        self.assertEqual(get_uuid_version(valid_uuid4), 4)
        self.assertEqual(get_uuid_version(valid_uuid5), 5)
        with self.assertRaises(Exception):
            get_uuid_version(invalid_uuid1)
        with self.assertRaises(Exception):
            get_uuid_version(invalid_uuid2)

    def test_can_be_guid(self):
        invalid_guid = "3f72d10b-d705-4115-99e0-9534fcfb4f75"
        valid_guid1 = "3F72D10B-D705-4115-99E0-9534FCFB4F75"
        valid_guid2 = "3F72D10B-D705-9115-25E0-9534FCFB4F75"
        self.assertTrue(can_be_guid(valid_guid1))
        self.assertTrue(can_be_guid(valid_guid2))
        self.assertFalse(can_be_guid(invalid_guid))

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


if __name__ == "__main__":
    main()