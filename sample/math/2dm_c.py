import numpy as np
from tlib.math.la import *


def main():

    m = np.array([
        [3, 2],
        [1, -1]
    ])
    (det, cp) = crossproduct_m_with_scaler_2d(
        m,
        verbose=True,
        gen_graph=True,
        show_graph=True
    )
    print(f"DET - {det}, CP - {cp}")


if __name__ == "__main__":
    main()
