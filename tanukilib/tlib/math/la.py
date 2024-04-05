import numpy as np
import numpy.linalg as LA
from numpy.typing import NDArray
import os
from pathlib import Path
import matplotlib.pyplot as plt


def lt_m_with_scaler_2d(
        m: NDArray,
        loc: NDArray,
        verbose: bool = False,
        gen_graph: bool = False,
        show_graph: bool = False,
) -> NDArray:
    """
    Perform Linear Transformation for 2*2 matrix and scaler (x,y).
    if gen_graph is True, generate a lt.jpg in {tmp_dir}/la
    """
    tmp_dir = Path(os.environ["HOME_TMP_DIR"]).joinpath("la")
    if not tmp_dir.exists():
        os.mkdir(str(tmp_dir))
    fname = str(tmp_dir.joinpath("lt_m_with_scaler_2d.jpg"))

    if m.shape != (2, 2):
        raise ValueError("M must be 2*2")
    if loc.shape != (2, 1):
        raise ValueError("loc must be (2,1)")

    n = np.dot(m, loc)
    if verbose:
        print("=== M ===")
        print(m)
        print("=== loc ===")
        print(loc)
        print("=== result ===")
        print(n)

    if gen_graph:
        plt.grid(True)
        # plt.set_xlabel("x")
        # plt.set_ylabel("y")
        plt.title("Linear Transformation with 2x2 M with Loc scaler 2D")
        plt.axline((0, 0), (m[0][0], m[1][0]), label="i-hat", color='b')
        plt.axline((0, 0), (m[0][1], m[1][1]), label="j-hat", color='r')
        plt.plot(m[0][0], m[1][0], color='b', marker='*')
        plt.plot(m[0][1], m[1][1], color='r', marker='*')
        plt.plot(loc[0][0], loc[1][0], color='gray', marker='o')
        plt.plot(n[0][0], n[1][0], color='y', marker='x')
        plt.plot(
            (loc[0][0], n[0][0]),
            (loc[1][0], n[1][0]),
            color='y',
            label='transformation'
        )
        plt.legend()

        if verbose:
            print(f"saving the graph to {fname}..")
        plt.savefig(fname)
        if verbose:
            print("graph saved successfully.")

        if show_graph:
            plt.show()

    return n


def crossproduct_m_with_scaler_2d(
        m: NDArray,
        verbose: bool = False,
        gen_graph: bool = False,
        show_graph: bool = False
) -> (float, float):
    """
    Calculate crossproduct for 2*2 matrix.
    Results are (det, cross product). Both must be equal (almost equal)
    Currently graph feature is not implemented
    """
    tmp_dir = Path(os.environ["HOME_TMP_DIR"]).joinpath("la")
    if not tmp_dir.exists():
        os.mkdir(str(tmp_dir))
    fname = str(tmp_dir.joinpath("cp.jpg"))

    if m.shape != (2, 2):
        raise ValueError("M must be 2*2")

    det = LA.det(m)
    cp = np.cross([m[0][0], m[1][0]], [m[0][1], m[1][1]])
    if verbose:
        print("=== M ===")
        print(m)
        print("=== DET ===")
        print(det)
        print("=== result ===")
        print(cp)

    if gen_graph:
        plt.grid(True)
        # plt.set_xlabel("x")
        # plt.set_ylabel("y")
        plt.title("Linear Transformation with 2x2 M with Loc scaler 2D")
        plt.axline((0, 0), (m[0][0], m[1][0]), label="i-hat", color='b')
        plt.axline((0, 0), (m[0][1], m[1][1]), label="j-hat", color='r')
        plt.plot(m[0][0], m[1][0], color='b', marker='*')
        plt.plot(m[0][1], m[1][1], color='r', marker='*')
        plt.legend()

        if verbose:
            print(f"saving the graph to {fname}..")
        plt.savefig(fname)
        if verbose:
            print("graph saved successfully.")

        if show_graph:
            plt.show()

    return (det, cp)
