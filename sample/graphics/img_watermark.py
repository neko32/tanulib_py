from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(Path(__file__).parent.parent.joinpath("img", "sample_img.jpg"))
    f_watermark_name = str(Path(__file__).parent.parent.joinpath("img", "windows_logo_1440_1080.jpg"))
    fout_name = str(Path(tmp_home_dir).joinpath("watermark_sample.jpg"))

    if exists(fout_name):
        remove(fout_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    wm = imread_wrapper(f_watermark_name, cv2.IMREAD_UNCHANGED)
    img_with_wm = add_watermark(img, wm, 0.2, 0.)
    try:
        cv2.imwrite(fout_name, img_with_wm)
        print(
            f"watermark sample done. file written to {fout_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
