from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(
        Path(__file__).parent.parent.joinpath("img", "neco.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath("roi_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name)
    roi_img = roi(img, 120, 50, 200, 150)
    try:
        cv2.imwrite(f_output_name, roi_img)
        print(f"ROI done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
