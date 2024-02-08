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

        self.assertEqual(get_uuid_version(valid_uuid1), 1)
        self.assertEqual(get_uuid_version(valid_uuid2), 2)
        self.assertEqual(get_uuid_version(valid_uuid3), 3)
        self.assertEqual(get_uuid_version(valid_uuid4), 4)
        self.assertEqual(get_uuid_version(valid_uuid5), 5)




if __name__ == "__main__":
    main()