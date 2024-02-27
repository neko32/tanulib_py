import os
import argparse
from os import walk, remove
from os.path import isdir
from tlib.fileutil import is_JFIF_img_file
from shutil import copy


def main(dir_name: str, backup_dir: str, is_test_run: bool):
    if os.environ['TLIB_ML_DATA_DIR'] is None:
        print("TLIB_ML_DATA_DIR must be defined")
        exit(1)

    root_dir = os.path.join(os.environ["TLIB_ML_DATA_DIR"], dir_name)
    backup_dir = os.path.join(os.environ["TLIB_ML_DATA_DIR"], backup_dir)
    print(f"root dir - {root_dir}, is_test_run - {is_test_run}")
    print(f"backup dir - {backup_dir}")
    if not isdir(root_dir):
        print(f"{root_dir} must be existing directory")
        exit(1)
    if not isdir(backup_dir):
        print(f"{backup_dir} must be existing directory")
        exit(1)

    removed_num = traverse(root_dir, backup_dir, is_test_run)
    print(f"total removed - {removed_num}")


def traverse(dir: str, backup_dir: str, is_test_run: bool) -> int:
    cnt = 0
    for cur_path, dirs, files in walk(dir):
        for file in files:
            fpath = os.path.join(cur_path, file)
            is_JFIF = is_JFIF_img_file(fpath)
            # print(f"{fpath} is supported? {is_JFIF}")
            if not is_JFIF:
                backup_file_path = os.path.join(backup_dir, file)
                if is_test_run:
                    print(f"DRYRUN::{fpath} moved to {backup_file_path}")
                else:
                    copy(fpath, backup_file_path)
                    remove(fpath)
                    print(f"{fpath} moved to {backup_file_path}")
                cnt += 1

        for dir in dirs:
            cnt += traverse(os.path.join(cur_path, dir),
                            backup_dir, is_test_run)

    return cnt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="remove_bad_images.py",
        usage="remove broken image files from image data set",
    )

    parser.add_argument("-d", "--dir", required=True)
    parser.add_argument("-b", "--backup_dir", required=True)
    parser.add_argument("-t", "--testrun", default=False)
    args = parser.parse_args()
    dir = args.dir
    backup_dir = args.backup_dir
    is_test_run = False if args.testrun.lower() == "false" else True
    main(dir, backup_dir, is_test_run)
