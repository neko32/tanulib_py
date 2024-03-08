from tlib.graphics import *
import cv2
import os
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = "../img/sample_img.jpg"
    f_output_name = f"{tmp_home_dir}/harriscorner_sample.jpg"

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    hc = detect_corner_by_harris(img)

    try:
        cv2.imwrite(f_output_name, hc)
        print(f"harris corner sample done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
