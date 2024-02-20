import cv2
import numpy as np
from cv2.typing import MatLike
from tlib.graphics import from_bgr_to_gray_scale

def preprocess_for_morph(img: MatLike, skip_gray:bool = False) -> MatLike:
    gr = img if skip_gray else from_bgr_to_gray_scale(img)
    _, dst = cv2.threshold(
        src = gr,
        thresh = 0,
        maxval = 255,
        type = cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )
    return dst

def morph_remove_noise_aka_open(
        img: MatLike,
        iteration:int = 1
) -> MatLike:
    kernel = np.ones(shape = (3, 3), dtype = np.uint8)
    return cv2.morphologyEx(
        src = img, 
        op = cv2.MORPH_OPEN,
        kernel = kernel,
        iterations = iteration
    )


def morph_remove_dots_aka_close(
        img: MatLike,
        iteration:int = 1
) -> MatLike:
    kernel = np.ones(shape = (3, 3), dtype = np.uint8)
    return cv2.morphologyEx(
        src = img, 
        op = cv2.MORPH_CLOSE,
        kernel = kernel,
        iterations = iteration
    )

def morph_remove_noises_aka_closeopen(
        img: MatLike,
        iteration:int = 1
) -> MatLike:
    kernel = np.ones(shape = (3, 3), dtype = np.uint8)
    intermed = cv2.morphologyEx(
        src = img, 
        op = cv2.MORPH_CLOSE,
        kernel = kernel,
        iterations = iteration
    )
    return cv2.morphologyEx(
        src = intermed, 
        op = cv2.MORPH_OPEN,
        kernel = kernel,
        iterations = iteration
    )


