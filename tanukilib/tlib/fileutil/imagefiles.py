from tlib.graphics.graphics import imread_wrapper
from tlib.fileutil.fileutil import split_filename_postfix
from typing import Dict
from pathlib import Path
from os import listdir


def generate_size_report(dir: str) -> Dict[str, int]:
    """Generate file size report in all images in the specified directory"""

    report_hash = {}
    supported_postfix = set(['jpg', 'jpeg', 'png', 'bmp'])

    path = Path(dir)
    if not path.exists():
        raise Exception(f"{dir} doesn't exist")

    for file in listdir(str(path)):
        _, postfix = split_filename_postfix(file)
        if postfix in supported_postfix:
            img = imread_wrapper(str(path.joinpath(file)))
            h, w = img.shape[:2]
            key = f"{w}x{h}"
            if key in report_hash:
                report_hash[key] += 1
            else:
                report_hash[key] = 1

    return report_hash
