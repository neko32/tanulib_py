import cv2
from cv2.typing import MatLike
import numpy as np
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

def is_grayscale(img:MatLike) -> bool:
    return len(img.shape) == 2

def affine_transform(src:MatLike, scale:int, angle:int) -> MatLike:
    h, w = src.shape[:2]
    center = (w // 2, h // 2)
    # M is affin trans matrix
    M = cv2.getRotationMatrix2D(center, angle, scale)
    # M = [a    b   c]
    #     [d    e   f]
    # a .. scale up/down against X axis. scale * cos(angle)
    # e .. scale up/down against Y axis. scale * sin(angle)
    # b .. shear/rotate against x axis
    # d .. shear/rotate against y axis
    # c .. parallel move against x axis. (1-a)*center.x - b*center.y
    # f .. parallel move against y axis. b*center.x - (1-a)*center.y
    cos_theta = np.abs(M[0, 0])
    sin_theta = np.abs(M[0, 1])
    dest_w = int(w * cos_theta + h * sin_theta)
    dest_h = int(w * sin_theta + h * cos_theta)

    # adjust gap before/after move
    M[0, 2] += (dest_w - w) / 2.0 
    M[1, 2] += (dest_h - h) / 2.0

    return cv2.warpAffine(src, M, (dest_w, dest_h))

def persist_img(src:MatLike, dest_path:str) -> bool:
    return cv2.imwrite(dest_path, src)

def is_shift_invarient_for_grayscale_imgs(a:MatLike, b:MatLike) -> bool:
    
    if not(is_grayscale(a) and is_grayscale(b)):
        raise Exception("both a and b must be gray scale")
    
    a_hist = cv2.calcHist([a], [0], None, [256], [0, 256])
    b_hist = cv2.calcHist([b], [0], None, [256], [0, 256])
    return np.array_equal(a_hist, b_hist)
    