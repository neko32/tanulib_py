import numpy as np
import numpy.linalg as LA
from tlib.math.la import *


def main():

    m = np.array([
        [3, 1],
        [0, 2]
    ])
    loc = np.array([[1], [1]])
    print(f"EIGENVALS - {LA.eigvals(m)}")
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
