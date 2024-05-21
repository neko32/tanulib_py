from tlib.graphics.graphics import resize_img_by_percentage
from pathlib import Path
import os
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = str(
        Path(__file__).parent.parent.joinpath("img", "sample_img.jpg"))
    f_output_name = str(Path(tmp_home_dir).joinpath("resize_per_sample.jpg"))

    if exists(f_output_name):
        remove(f_output_name)

    try:
        resize_img_by_percentage(f_input_name, f_output_name, 30)
        print(
            f"resize image per centage sample done. file written to {f_output_name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
