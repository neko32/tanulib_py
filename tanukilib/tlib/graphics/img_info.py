from tlib.core import exec_cmd
from typing import Dict, Tuple
from cv2.typing import MatLike
from pathlib import Path
import math


def get_exif_data(file_path: str) -> Dict[str, str]:
    """get exif info from a file. exiftool must be installed in your PC"""

    if not Path(file_path).is_file():
        raise Exception(f"{file_path} is not a file")

    (retcode, stdout, _) = exec_cmd(['exiftool', file_path])
    if retcode != 0:
        raise Exception("executing exiftool command failed")

    exif_dict = {}
    for line in stdout.splitlines():
        line_l = line.split(":")
        k = line_l[0]
        v = "".join(line_l[1:])
        k = k.strip()
        v = v.strip()
        exif_dict[k] = v
    return exif_dict


def aspect_ratio(w: float, h: float) -> Tuple[float, float]:
    """calculate aspect ratio of provided width and height"""
    gcd = math.gcd(int(w), int(h))
    return (w / gcd, h / gcd)


def aspect_ratio_of_image(img: MatLike) -> Tuple[float, float]:
    """calculate aspect ratio of provided image"""
    h, w = img.shape[:2]
    gcd = math.gcd(int(w), int(h))
    return (w / gcd, h / gcd)


def is_horizontal_image_by_aspect_ratio(img: MatLike) -> bool:
    """
    Check whether the provided image is horizontal image or vertical one.
    If aspect ratio is > 1, then assume it's horizontal. Else vertical.
    """
    ar = aspect_ratio_of_image(img)
    return ar[0] / ar[1] > 1


def is_square_image_by_aspect_ratio(img: MatLike) -> bool:
    """
    Check whether the provided image is square image or not.
    If aspect ratio is 0, then assume it's square.
    """
    ar = aspect_ratio_of_image(img)
    return (ar[0] / ar[1]) == 1.
