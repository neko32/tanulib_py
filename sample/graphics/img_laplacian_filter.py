from tlib.graphics import *
import cv2
import os
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = "../img/sample_img.jpg"
    f_output_name = f"{tmp_home_dir}/laplacian_sample.jpg"

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_GRAYSCALE)
    lap_filted = filter_by_laplacian(img, ImageDepthType.IMG_DEPTH_32FLOAT, 3)
    try:
        cv2.imwrite(f_output_name, lap_filted)
        print(f"laplacian filter sample done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
