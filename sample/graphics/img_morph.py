from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def perf_morth(img: MatLike, morph_type: str) -> MatLike:
    preprocessed = preprocess_for_morph(img)
    if morph_type == "open":
        return morph_remove_noise_aka_open(preprocessed)
    elif morph_type == "close":
        return morph_remove_dots_aka_close(preprocessed)
    elif morph_type == "morphologicalgradient":
        return morph_morphological_gradient(preprocessed)
    elif morph_type == "blackhat":
        return morph_blackhat(preprocessed)
    elif morph_type == "tophat":
        return morph_tophat(preprocessed)
    else:
        raise Exception("not supported")


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_open_name = str(Path(tmp_home_dir).joinpath("morph_open_sample.jpg"))
    f_close_name = str(Path(tmp_home_dir).joinpath("morph_close_sample.jpg"))
    f_mg_name = str(Path(tmp_home_dir).joinpath(
        "morph_morphologicalgradient_sample.jpg"))
    f_tophat_name = str(Path(tmp_home_dir).joinpath("morph_tophat_sample.jpg"))
    f_blackhat_name = str(Path(tmp_home_dir).joinpath("morph_blackhat_sample.jpg"))

    files = [f_open_name, f_close_name, f_mg_name, f_blackhat_name, f_tophat_name]
    morph_type = ["open", "close", "morphologicalgradient", "blackhat", "tophat"]

    for f, mt in zip(files, morph_type):
        if exists(f):
            remove(f)
        img = imread_wrapper(str(Path(__file__).parent.parent.joinpath(
            "img", "sample_img.jpg")), cv2.IMREAD_UNCHANGED)
        morphed = perf_morth(img, mt)
        cv2.imwrite(f, morphed)

    print("img_morph sample done.")


if __name__ == "__main__":
    main()
