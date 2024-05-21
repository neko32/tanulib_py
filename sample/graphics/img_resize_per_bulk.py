from tlib.graphics.graphics import resize_img_by_percentage
from pathlib import Path
import os


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_dir = Path(tmp_home_dir).joinpath("bulksrc")
    f_output_dir = Path(tmp_home_dir).joinpath("bulkdest")
    f_output_dir.mkdir(exist_ok=True)

    try:
        for idx, file in enumerate(f_input_dir.glob("*")):
            f_input_name = str(file)
            f_output_name = str(Path(f_output_dir).joinpath(file.name))
            resize_img_by_percentage(f_input_name, f_output_name, 30)
            print(f"resize image per centage {f_output_name} @ {idx}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
