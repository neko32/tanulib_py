from typing import Optional
from os import remove, rmdir, listdir
import cv2
import csv
import magic

def split_filename_postfix(file_name:str) -> (str, Optional[str]):
    sp = file_name.split('.')
    if len(sp) == 1:
        return (sp[0], None)
    else:
        return (".".join(sp[0:-1]), sp[-1])

def rmdir_and_files(dir_path:str) -> (int, int):
    success_n = 0
    fail_n = 0
    for f in listdir(dir_path):
        try:
            remove(f"{dir_path}/{f}")
            success_n += 1
        except:
            fail_n += 1

    if fail_n == 0:
        rmdir(dir_path)

    return (success_n, fail_n)

def gen_image_files_summary(dir_path:str, dest_csv_path:str) -> bool:
    try:
        supported_postfix = ['jpg', 'jpeg', 'png', 'bmp']
        with open(dest_csv_path, 'w') as fp:

            csv_w = csv.writer(fp)
            csv_w.writerow(['filename', 'postfix', 'width', 'height', 'channel', 'magic'])

            for f in listdir(dir_path):
                _, postfix = split_filename_postfix(f)
                if postfix.lower() in supported_postfix:
                    fpath = f"{dir_path}/{f}"
                    img = cv2.imread(fpath, cv2.IMREAD_UNCHANGED)
                    shape = img.shape
                    height = shape[0]
                    width = shape[1]
                    channel = shape[2]
                    magicwords = magic.from_file(fpath)
                    csv_w.writerow([f, postfix, width, height, channel, magicwords])

    except Exception as e:
        print(e)
        return False
    return True



