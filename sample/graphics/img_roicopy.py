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
    f_roiimg_name = str(
        Path(__file__).parent.parent.joinpath("img", "neco.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath(
        "img_roicopy_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    roi_img = imread_wrapper(f_roiimg_name, cv2.IMREAD_UNCHANGED)
    copied = blockcopy(
        src_image=roi_img,
        dest_orig_img=img,
        roi_from_src=Rect(200, 180, 350, 250),
        dest_x=200,
        dest_y=300
    )
    try:
        cv2.imwrite(f_output_name, copied)
        print(f"image ROI copy sample done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
