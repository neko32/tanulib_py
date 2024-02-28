from tlib.graphics import *
import cv2
import os
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = "../img/sample_img.jpg"
    fout_name = f"{tmp_home_dir}/colorrange_filter_sample.jpg"

    if exists(fout_name):
        remove(fout_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    lower = HSVColorSchema(20, 50, 10)
    upper = HSVColorSchema(60, 255, 255)
    col_filted = filter_by_hsv_color_range(img, lower, upper)
    try:
        cv2.imwrite(fout_name, col_filted)
        print(
            f"filter by col range sample done. file written to {fout_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
