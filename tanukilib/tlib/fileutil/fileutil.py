from typing import Optional, Tuple, List
from os import remove, rmdir, listdir
from pathlib import Path
import cv2
import csv
import magic
from collections import OrderedDict
from tlib.datautil.random import gen_rand_alnum_str


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


def touch(path: str, file_name: Optional[str] = None) -> str:
    """Create an empty file"""
    p = Path(path)
    if not p.exists():
        raise Exception(f"{path} doesn't exist")
    fname = file_name if file_name is not None else gen_rand_alnum_str(16)
    fpath = str(p.joinpath(fname))
    with open(fpath, "w"):
        pass

    return fpath


class PaginatedFileList:
    """
    Cache files locations under specified directory and
    provide pagination feature. Directoies are ignored.
    """

    def __init__(
            self,
            dir_path: str,
            page_size: int,
            title: str,
            init_page_idx: int = 0,
            sort_files_by_name: bool = True,
            max_file_size: int = 65535):
        self.dir_path = dir_path
        self.page_size = page_size
        self.title = title
        self.idx = init_page_idx
        self.max_file_size = max_file_size
        self.sort_files_by_name = sort_files_by_name

        dir_path_obj = Path(self.dir_path)
        if not dir_path_obj.exists():
            raise Exception(f"{self.dir_path} doesn't exist")
        if dir_path_obj.is_file():
            raise Exception(f"{self.dir_path} must be directory")

        self.cache = OrderedDict()

        buf = []
        for idx, file in enumerate(dir_path_obj.iterdir()):
            if idx == self.max_file_size:
                break
            if file.is_file():
                buf.append((file.name, str(file)))
        if self.sort_files_by_name:
            buf = sorted(buf)

        for fname, f in buf:
            self.cache[fname] = f

        if self.idx >= len(self.cache):
            raise Exception(f"index specified {self.idx} is beyond \
                            size of the files loaded ({len(self.cache)})")

    def get(self) -> List[str]:
        """
        get pagenated list of files from index to index + window size.
        If index + window size goes beyond cached file numbers,
        then range becomes index to num of cached files.
        """
        files = self.cache.values()
        st = self.idx
        ed = min(self.idx + self.page_size, len(self.cache))
        return list(files)[st:ed]

    def next(self) -> bool:
        """
        advance index to next page size.
        If index + page size goes beyond num of cached files, then False is returned.
        """
        next_idx = self.idx + self.page_size
        if next_idx >= len(self.cache):
            return False
        self.idx = next_idx
        return True

    def prev(self) -> bool:
        """
        go back index to next page size.
        if index is already index 0, then False is returned.
        """
        if self.idx <= 0:
            return False

        self.idx = max(self.idx - self.page_size, 0)
        return True

    def __repr__(self) -> str:
        return self.cache.__repr__()
