from tlib.graphics import *
import cv2
import os
from os import remove
from os.path import exists


def main():
    img = gen_white_canvas(600, 400)
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    fname = f"{tmp_home_dir}/draw_sample.jpg"

    if exists(fname):
        remove(fname)

    draw_rect(img, [100, 100], [140, 120])
    fill_rect(img, [500, 300], [520, 350], BGRA(255, 128, 0), LineType.LINE_TYPE_4)
    draw_line(img, [150, 30], [300, 200], color = BGRA(128, 255, 0), line_thickness = 3, line_type = LineType.LINE_TYPE_AA)
    draw_text(img, "takoring", (230, 170), BGRA(125, 125, 125))

    cv2.imwrite(fname, img)

    print("done.")


if __name__ == "__main__":
    main()