from unittest import TestCase, main
from tlib.datautil import gen_scalar_randint
from tlib.core import *
from typing import Tuple
import time

def calc_with_wait_multi_params_out(p:Tuple[int, int]):
    r = gen_scalar_randint(1, 10, 1000)
    m, n = p
    print(f"this will take {r[0] / 1000} msecs..")
    time.sleep(r[0] / 100)
    return m * n

class CoreTest(TestCase):

    def test_get_num_cpu(self):
        n_cpu = get_num_cpu()
        self.assertTrue(n_cpu > 0)

    def test_exec_parallel_async(self):
        ipt = [(x, x) for x in range(1, 6)]
        print(ipt)
        for i, r in enumerate(exec_parallel_async(5, calc_with_wait_multi_params_out, ipt)):
            self.assertEqual(r, ipt[i][0] * ipt[i][1])

if __name__ == "__main__":
    main()