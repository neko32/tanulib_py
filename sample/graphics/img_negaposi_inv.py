from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(Path(__file__).parent.parent.joinpath("img", "sample_img.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath("negaposi_inv_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_GRAYSCALE)
    npinv = inverse_negative_positive(img)
    try:
        cv2.imwrite(f_output_name, npinv)
        print(f"nega-posi inverse sample done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
