from tlib.graphics import imread_wrapper
from tlib.graphics.threshold import apply_adaptive_threshold
from tlib.graphics.threshold import AdaptiveThresholdType
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(Path(__file__).parent.parent.joinpath("img", "sample_img.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath("adaptive_thresh_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    img = imread_wrapper(f_input_name, cv2.IMREAD_GRAYSCALE)
    f_out1 = apply_adaptive_threshold(
        img=img,
        maxv=255.,
        at_method=AdaptiveThresholdType.GAUSSIAN_C,
        block_size=7,
        C=5,
        preprocess_noise=False
    )
    try:
        cv2.imwrite(f_output_name, f_out1)
        print("Adaptive thresh sample done.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
