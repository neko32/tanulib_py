import numpy as np
import numpy.linalg as LA
from tlib.math.la import *


def main():

    m = np.array([
        [2, -1],
        [0, 1]
    ])
    dest_loc = np.array([[4], [2]])
    print(f"RANK - {LA.matrix_rank(m)}")
    print("INV - ")
    try:
        print(LA.inv(m))
    except Exception:
        print("N/A")
    rez = cramer_2d(m, dest_loc, True)
    print(rez)


if __name__ == "__main__":
    main()
