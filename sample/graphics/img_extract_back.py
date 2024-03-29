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
    f_output_name = str(Path(tmp_home_dir).joinpath("extract_back_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_UNCHANGED)
    img = erode(img)

    high_s = int(conv_to_opencv_sat_val(56))
    low = [10, 30, 20]
    high = [40, high_s, 250]
    back_ext = extract_background_by_col_range(img, low, high)
    f_out = generate_background_pattern_image(back_ext)
    try:
        cv2.imwrite(f_output_name, f_out)
        print("extract background done.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
