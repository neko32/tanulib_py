from tlib.datautil import gen_scalar_randint
from unittest import TestCase, main
import numpy as np

class DataUtilTest(TestCase):

    def test_gen_scalar_randint(self):
        r = gen_scalar_randint(10000, 0, 100)
        
        self.assertTrue(np.all(r >= 0) and np.all(r <= 100))

if __name__ == "__main__":
    main()