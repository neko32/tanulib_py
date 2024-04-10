from tlib.graphics import *
import cv2
import os
from pathlib import Path
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    base_path = Path(tmp_home_dir)
    f_output_name_lat = str(base_path.joinpath("ruled_line_lattice.jpg"))
    f_output_name_hor = str(base_path.joinpath("ruled_line_horizontal.jpg"))
    f_output_name_ver = str(base_path.joinpath("ruled_line_vertical.jpg"))

    f_output_names = [f_output_name_lat, f_output_name_hor, f_output_name_ver]

    for f_output_name in f_output_names:
        if exists(f_output_name):
            remove(f_output_name)

    try:
        for output_name in f_output_names:
            cvs = gen_white_canvas(640, 480)
            if "lattice" in output_name:
                cvs = draw_ruled_lines(cvs, 20)
            elif "horizontal" in output_name:
                cvs = draw_ruled_lines(
                    cvs, 20, ruled_line_type=RuledLineType.RULED_LINE_ONLY_HORIZONTAL)
            elif "vertical" in output_name:
                cvs = draw_ruled_lines(
                    cvs, 20, ruled_line_type=RuledLineType.RULED_LINE_ONLY_VERTICAL)
            cv2.imwrite(output_name, cvs)
            print(f"Ruled Line Canvas done. written to {output_name}")
    except Exception as e:
        print(e)
        raise e


if __name__ == "__main__":
    main()
