from typing import Optional, Tuple, List
from os import remove, rmdir, listdir
from pathlib import Path
import cv2
import csv
import magic


def split_filename_postfix(file_name: str) -> Tuple[str, Optional[str]]:
    """
    split file name and postfix.
    If no postfix, Tuple's second element is None
    """
    sp = file_name.split('.')
    if len(sp) == 1:
        return (sp[0], None)
    else:
        return (".".join(sp[0:-1]), sp[-1])


def rmdir_and_files(dir_path: str) -> Tuple[int, int]:
    """
    remove dirs and files recursively.
    Number of removed files and number of failures to remove files
    are return as Tuple
    """
    success_n = 0
    fail_n = 0
    for f in listdir(dir_path):
        try:
            remove(str(Path(dir_path).joinpath(f)))
            success_n += 1
        except Exception:
            fail_n += 1

    if fail_n == 0:
        rmdir(dir_path)

    return (success_n, fail_n)


def gen_image_files_summary(dir_path: str, dest_csv_path: str) -> bool:
    """
    Generates image file summary.
    Summary includes the following data;
    - file path
    - postfix
    - image width
    - image height
    - number of channels
    - magic words
    """
    try:
        supported_postfix = ['jpg', 'jpeg', 'png', 'bmp']
        with open(dest_csv_path, 'w') as fp:

            csv_w = csv.writer(fp)
            csv_w.writerow(
                [
                    'filename', 'postfix', 'width',
                    'height', 'channel', 'magic'
                ]
            )

            for f in listdir(dir_path):
                _, postfix = split_filename_postfix(f)
                if postfix.lower() in supported_postfix:
                    fpath = str(Path(dir_path).joinpath(f))
                    img = cv2.imread(fpath, cv2.IMREAD_UNCHANGED)
                    shape = img.shape
                    height = shape[0]
                    width = shape[1]
                    channel = shape[2]
                    magicwords = magic.from_file(fpath)
                    csv_w.writerow(
                        [f, postfix, width, height, channel, magicwords])

    except Exception as e:
        print(e)
        return False
    return True


def is_JFIF_img_file(fpath: str) -> bool:
    """A util function to tell if the file is JFIF image file or not"""
    try:
        with open(fpath, 'rb') as fp:
            return b"JFIF" in fp.peek(10)
    except Exception as e:
        print(e)
        return False


def list_files_and_dirs(
        fpath: str,
        glob_str: str = "*",
) -> Tuple[List[str], List[str]]:
    """
    List files and dirs in the given fpath with the given GLOB-formatted filter.
    Tuple of (found dirs, found files) is returned.
    If Path doesn't exist, then Tuple of (empty list, empty list) is returned
    """

    path = Path(fpath)
    if not path.exists():
        return ([], [])

    dirs = []
    files = []
    print(glob_str)
    for f in path.glob(glob_str):
        if f.is_dir():
            dirs.append(str(f))
        else:
            files.append(str(f))
    return (dirs, files)
