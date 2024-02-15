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
    draw_circle(img, (100, 100), 32, BGRA(0, 0, 255), 2, LineType.LINE_TYPE_4)
    fill_circle(img, (300, 300), 16, BGRA(0, 0, 200), LineType.LINE_TYPE_AA)
    draw_ellipse(img, [180, 250], [25, 80], 20, BGRA(128, 256, 30))
    fill_ellipse(img, [400, 50], [40, 20], 0, BGRA(30, 256, 128))
    draw_arc(img, [280, 350], [25, 40], 20, 0, 45, BGRA(20, 100, 60), 3, LineType.LINE_TYPE_AA)
    fill_arc(img, [380, 150], [30, 30], 0, 180, 260, BGRA(20, 20, 190), LineType.LINE_TYPE_AA)

    cv2.imwrite(fname, img)

    print("done.")


if __name__ == "__main__":
    main()