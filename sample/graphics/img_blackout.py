from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(
        Path(__file__).parent.parent.joinpath("img", "sample_img.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath(
        "img_blackout_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    blackout(
        a = img,
        st = [120, 30],
        end = [300, 290]
    )
    try:
        cv2.imwrite(f_output_name, img)
        print(f"image blackout sample done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
