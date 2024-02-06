from unittest import TestCase, main
from tlib.core import *

class CoreTest(TestCase):

    def test_get_num_cpu(self):
        n_cpu = get_num_cpu()
        self.assertTrue(n_cpu > 0)

if __name__ == "__main__":
    main()