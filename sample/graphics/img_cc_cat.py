import cv2
from tlib.graphics import CascadeClassifier, CascadeClassifierFilter
from tlib.graphics import imread_wrapper
from pathlib import Path
import os
from os import remove
from os.path import exists


def main():

    cc = CascadeClassifier(
        classifier_name=CascadeClassifierFilter.CAT_EXT,
        min_neighbors=7,
        min_posible_obj_size=[30, 30],
        max_possible_obj_size=[300, 300]
    )

    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(Path(__file__).parent.parent.joinpath("img", "two_cats.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath("cc_cat_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)
    
    img = imread_wrapper(f_input_name)
    img2 = cc.process(img, None)

    try:
        cv2.imwrite(f_output_name, img2)
        print("Cascade Classifier with cats done.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()