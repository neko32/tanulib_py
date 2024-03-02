import cv2
import numpy as np
from cv2.typing import MatLike
from tlib.graphics import from_bgr_to_gray_scale
from tlib.graphics.threshold import apply_otsu_threshold


def preprocess_for_morph(img: MatLike, skip_gray: bool = False) -> MatLike:
    gr = img if skip_gray else from_bgr_to_gray_scale(img)
    return apply_otsu_threshold(
        img=gr,
        thresh=0,
        maxv=255.
    )


def morph_remove_noise_aka_open(
        img: MatLike,
        iteration: int = 1
) -> MatLike:
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    return cv2.morphologyEx(
        src=img,
        op=cv2.MORPH_OPEN,
        kernel=kernel,
        iterations=iteration
    )


def morph_remove_dots_aka_close(
        img: MatLike,
        iteration: int = 1
) -> MatLike:
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    return cv2.morphologyEx(
        src=img,
        op=cv2.MORPH_CLOSE,
        kernel=kernel,
        iterations=iteration
    )


def morph_remove_noises_aka_closeopen(
        img: MatLike,
        iteration: int = 1
) -> MatLike:
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    intermed = cv2.morphologyEx(
        src=img,
        op=cv2.MORPH_CLOSE,
        kernel=kernel,
        iterations=iteration
    )
    return cv2.morphologyEx(
        src=intermed,
        op=cv2.MORPH_OPEN,
        kernel=kernel,
        iterations=iteration
    )
