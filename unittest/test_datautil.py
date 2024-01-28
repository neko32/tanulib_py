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
        



if __name__ == "__main__":
    main()