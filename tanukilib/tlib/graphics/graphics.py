import cv2
from typing import List
from os.path import isdir
from os import listdir

_TLIBG_W_JPG_DEFAULT = [cv2.IMWRITE_JPEG_QUALITY, 100]
_TLIBG_W_PNG_DEFAULT = [cv2.IMWRITE_PNG_STRATEGY, cv2.IMWRITE_PNG_STRATEGY_DEFAULT]
_TLIG_W_FLG_MAP = {
    "png": _TLIBG_W_PNG_DEFAULT, 
    "jpg": _TLIBG_W_JPG_DEFAULT,
    "jpeg": _TLIBG_W_JPG_DEFAULT,
}

def resize_img(src_path:str, dest_path:str, new_width:int, new_height:int) -> bool:
    buf = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(buf, [new_width, new_height])
    prefix = dest_path.split('.')[-1].lower()
    cfg = _TLIG_W_FLG_MAP[prefix]
    return cv2.imwrite(dest_path, resized, cfg)

def resize_all_imgs(src_path:str, dest_path:str, new_width:int, new_height:int) -> int:
    if not(isdir(src_path) and isdir(dest_path)):
        raise Exception(f"{src_path} and {dest_path} must be directory")
    cnt = 0
    for file in listdir(src_path):
        src_file = f"{src_path}/{file}"
        dest_file = f"{dest_path}/{file}"
        cnt += 1 if resize_img(src_file, dest_file, new_width, new_height) else 0

    return cnt
    

def copy_img(src_path:str, dest_path) -> bool:
    buf = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    prefix = dest_path.split('.')[-1].lower()
    cfg = _TLIG_W_FLG_MAP[prefix]
    return cv2.imwrite(dest_path, buf, cfg)

def to_gray_image(src_path:str, dest_path:str) -> bool:
    buf = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
    return cv2.imwrite(dest_path, buf)
