import numpy as np
from tlib.math.la import *


def main():

    m = np.array([
        [0, -1],
        [1, 0]
    ])
    loc = np.array([[2], [1]])
    lt_m_with_scaler_2d(
        m,
        loc,
        verbose=True,
        gen_graph=True,
        show_graph=True
    )


if __name__ == "__main__":
    main()
