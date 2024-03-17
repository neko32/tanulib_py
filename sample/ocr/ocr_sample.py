from tlib.ocr import do_ocr_scan
from pathlib import Path
import os


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    target_file = str(Path(tmp_home_dir).joinpath("target.jpg"))
    ocr_result = do_ocr_scan(target_file)
    print(ocr_result)


if __name__ == "__main__":
    main()
