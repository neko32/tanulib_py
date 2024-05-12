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
        "img_coutout_sample.jpg"))
    f_output_name_rand = str(Path(tmp_home_dir).joinpath(
        "img_cutout_random_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)
    if exists(f_output_name_rand):
        remove(f_output_name_rand)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    img2 = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    cutout(
        m=img,
        region=Rect(20, 50, 250, 40)
    )
    cutout(
        m=img2,
        color=BGRA(127, 127, 127)
    )
    try:
        cv2.imwrite(f_output_name, img)
        cv2.imwrite(f_output_name_rand, img2)
        print("image cutout sample done.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
