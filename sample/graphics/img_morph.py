from tlib.graphics import *
import cv2
import os
from os import remove
from os.path import exists

def main():
    img = cv2.imread("../img/sample_img.jpg", cv2.IMREAD_UNCHANGED)
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    fname = f"{tmp_home_dir}/morph_sample.jpg"

    if exists(fname):
        remove(fname)

    img = preprocess_for_morph(img)
    img = morph_remove_noise_aka_open(img)

    cv2.imwrite(fname, img)

    print("img_morph sample done.")



if __name__ == "__main__":
    main()