import cv2
import numpy as np
from cv2.typing import MatLike
from tlib.graphics import from_bgr_to_gray_scale
from tlib.graphics.threshold import apply_otsu_threshold
from tlib.graphics.movie import Effecter


def preprocess_for_morph(img: MatLike, skip_gray: bool = False) -> MatLike:
    """
    Performs the following preprocessing to make morph most effective
    - convert to gray scale
    - apply threshold (Otsu only for now)
    """
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
    """Apply morphology with open. Best to remove white noise"""
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
    """Apply morphology with close. Best to remove black dots"""
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    return cv2.morphologyEx(
        src=img,
        op=cv2.MORPH_CLOSE,
        kernel=kernel,
        iterations=iteration
    )


def morph_morphological_gradient(
        img: MatLike,
        iteration: int = 1
) -> MatLike:
    """Apply morphology with morphlogical gradient. Best to emphasize edge/rim"""
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    return cv2.morphologyEx(
        src=img,
        op=cv2.MORPH_GRADIENT,
        kernel=kernel,
        iterations=iteration
    )


def morph_remove_noises_aka_closeopen(
        img: MatLike,
        iteration: int = 1
) -> MatLike:
    """Performs close and open morphology successively"""
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


def erode(
    img: MatLike,
    iteration: int = 1
) -> MatLike:
    """Perform erosion. White portion becomes thinner"""
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    return cv2.erode(
        src=img,
        kernel=kernel,
        iterations=iteration
    )


class SkeltonizationEffect(Effecter):
    """Provides Skeltonization effect"""

    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        """Cause skeltonization effect"""
        th = preprocess_for_morph(img)
        w = int(device.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(device.get(cv2.CAP_PROP_FRAME_HEIGHT))
        skelton_buf = np.zeros(shape=(h, w), dtype=np.uint8)

        while True:
            opened = morph_remove_noise_aka_open(th)
            diff_with_without_noise = cv2.subtract(
                src1=th,
                src2=opened
            )
            th = erode(th)

            skelton_buf = cv2.bitwise_or(
                src1=skelton_buf,
                src2=diff_with_without_noise
            )

            if cv2.countNonZero(th) == 0:
                break

        return skelton_buf
