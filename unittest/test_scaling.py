from unittest import TestCase, main
from tlib.stats.scaling import *
import numpy as np


class ScalingTest(TestCase):

    def test_minmax_scaling(self):
        data = np.array([
            [100, 0.001],
            [8, 0.05],
            [50, 0.005],
            [88, 6],
            [120, 3]
        ])
        mm = scale_by_minmax(data)
        print(mm)
        self.assertEqual(mm[1][0], 0.)
        self.assertEqual(mm[4][0], 1.)
        self.assertEqual(mm[3][1], 1.)
        self.assertEqual(mm[0][1], 0.)

    def test_standardization_scaling(self):

        data = np.array([
            [100, 0.001],
            [8, 0.05],
            [50, 0.005],
            [88, 6],
            [120, 3]
        ])
        std = scale_by_standardization(data)
        print(std)


if __name__ == "__main__":
    main()
