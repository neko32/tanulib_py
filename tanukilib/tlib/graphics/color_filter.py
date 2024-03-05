import cv2
import numpy as np
from cv2.typing import MatLike
from tlib.graphics import HSVColorSchema
from tlib.graphics.movie import Effecter


def filter_by_hsv_color_range(
        img: MatLike,
        lower_range: HSVColorSchema,
        upper_range: HSVColorSchema,
        back_to_bgr: bool = True
) -> MatLike:
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower_range.as_mat(), upper_range.as_mat())
    masked = cv2.bitwise_and(
        src1=hsv_img,
        src2=hsv_img,
        mask=mask
    )
    return cv2.cvtColor(masked, cv2.COLOR_HSV2BGR) if back_to_bgr else masked


class BackgroundSubtractor:
    def __init__(
            self,
            frame_width: int,
            frame_height: int,
            alpha: float):
        self.alpha = alpha
        self.background = np.zeros(
            shape=[frame_height, frame_width, 3],
            dtype=np.float32
        )

    def update(self, img: MatLike) -> MatLike:
        fimg = np.float32(img)
        absbuf = cv2.absdiff(fimg, self.background)
        cv2.accumulateWeighted(
            src=fimg,
            dst=self.background,
            alpha=self.alpha
        )
        return np.uint8(absbuf)


class BackgroundSubtractionEffects(Effecter):

    def __init__(
            self,
            frame_width: int,
            frame_height: int,
            alpha: float):
        self.se = BackgroundSubtractor(
            frame_width,
            frame_height,
            alpha
        )

    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        return self.se.update(img)
