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
    f_output_name1 = str(Path(tmp_home_dir).joinpath("gamma0.5.jpg"))
    f_output_name2 = str(Path(tmp_home_dir).joinpath("gamma2.jpg"))

    if exists(f_output_name1):
        remove(f_output_name1)

    if exists(f_output_name2):
        remove(f_output_name2)

    img = imread_wrapper(f_input_name, cv2.IMREAD_GRAYSCALE)
    gr1 = apply_gamma_correction(
        img, GammaCorrectionPreset.GAMMA_CORRECTION_REASONABLY_DARKER.value)
    gr2 = apply_gamma_correction(
        img, GammaCorrectionPreset.GAMMA_CORRECTION_TOO_BRIGHTER.value)

    try:
        cv2.imwrite(f_output_name1, gr1)
        cv2.imwrite(f_output_name2, gr2)
        print("Gamma Correction sample done.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
