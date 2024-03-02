import cv2
from cv2.typing import MatLike
from enum import Enum
import tlib.graphics


class AdaptiveThresholdType(Enum):
    MEAN_C = cv2.ADAPTIVE_THRESH_MEAN_C
    GAUSSIAN_C = cv2.ADAPTIVE_THRESH_GAUSSIAN_C


def apply_otsu_threshold(
        img: MatLike,
        thresh: float = 0.,
        maxv: float = 255.,
) -> MatLike:
    _, rez = cv2.threshold(
        src=img,
        thresh=thresh,
        maxval=maxv,
        type=cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )
    return rez


def apply_adaptive_threshold(
        img: MatLike,
        maxv: float = 255,
        at_method: AdaptiveThresholdType = AdaptiveThresholdType.MEAN_C,
        block_size: int = 7,
        C: float = 3.,
        preprocess_noise: bool = False
) -> MatLike:
    img = tlib.graphics.morph_remove_noises_aka_closeopen(img) if preprocess_noise else img
    return cv2.adaptiveThreshold(
        src=img,
        maxValue=maxv,
        adaptiveMethod=at_method.value,
        blockSize=block_size,
        thresholdType=cv2.THRESH_BINARY,
        C=C
    )
