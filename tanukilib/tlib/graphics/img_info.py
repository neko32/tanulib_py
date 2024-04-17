from tlib.core import exec_cmd
from typing import Dict
from pathlib import Path


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
