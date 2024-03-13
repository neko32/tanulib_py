from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists

def perf_morth(img:MatLike, morph_type:str) -> MatLike:
    preprocessed = preprocess_for_morph(img, True)
    if morph_type == "closeopen":
        return morph_remove_noises_aka_closeopen(preprocessed)
    else:
        raise Exception("not supported")

def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_name = str(Path(tmp_home_dir).joinpath("morph_closeopen_sample.jpg"))

    files = [f_name]
    morph_type = ["closeopen"]

    for f,mt in zip(files, morph_type):
        if exists(f):
            remove(f)
        img = imread_wrapper(str(Path(__file__).parent.parent.joinpath("img", "sabi.jpg")), cv2.IMREAD_GRAYSCALE)
        img = invert_grayscale(img)
        morphed = perf_morth(img, mt)
        cv2.imwrite(f, morphed)

    print("img_morph sample done.")

if __name__ == "__main__":
    main()