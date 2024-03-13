from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(Path(__file__).parent.parent.joinpath("img", "windows_logo_1440_1080.jpg"))
    f_output_name1 = str(Path(tmp_home_dir).joinpath("flip_vert.jpg"))
    f_output_name2 = str(Path(tmp_home_dir).joinpath("flip_horiz.jpg"))

    for f in [f_output_name1, f_output_name2]:
        if exists(f):
            remove(f)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    f_out1 = flip_image(img, FlipDirection.FLIP_VERTICAL)
    f_out2 = flip_image(img, FlipDirection.FLIP_HORIZONTAL)
    try:
        cv2.imwrite(f_output_name1, f_out1)
        cv2.imwrite(f_output_name2, f_out2)
        print("flip image sample done.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
