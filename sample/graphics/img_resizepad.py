from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(Path(__file__).parent.parent.joinpath("img", "sample_img.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath("resizepad_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    resize_img_with_padding(
        f_input_name,
        f_output_name,
        800,
        300,
        padding_color=BGRA(0, 255, 0)
    )

    print("resizing with padding done.")


if __name__ == "__main__":
    main()
