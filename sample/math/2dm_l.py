import numpy as np
import numpy.linalg as LA
from tlib.math.la import *


def main():

    m = np.array([
        [3, 2],
        [1, -1]
    ])
    loc = np.array([[2], [1]])
    print(f"DET - {LA.det(m)}")
    print(f"RANK - {LA.matrix_rank(m)}")
    print("INV - ")
    try:
        print(LA.inv(m))
    except:
        print("N/A")
    lt_m_with_scaler_2d(
        m,
        loc,
        verbose=True,
        gen_graph=True,
        show_graph=True
    )



if __name__ == "__main__":
    main()
