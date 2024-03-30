import cv2
import numpy as np
from typing import Tuple
from cv2.typing import MatLike
from tlib.graphics import HSVColorSchema
from tlib.graphics.movie import Effecter


def filter_by_hsv_color_range(
        img: MatLike,
        lower_range: HSVColorSchema,
        upper_range: HSVColorSchema,
        back_to_bgr: bool = True
) -> MatLike:
    """
    Filter images by HSV color range.
    If back_to_bgr flag is True, then returned MatLike is converted back to BGR format
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower_range.as_mat(), upper_range.as_mat())
    masked = cv2.bitwise_and(
        src1=hsv_img,
        src2=hsv_img,
        mask=mask
    )
    return cv2.cvtColor(masked, cv2.COLOR_HSV2BGR) if back_to_bgr else masked


def inverse_negative_positive(
        img: MatLike
) -> MatLike:
    """Inverse negative/positive"""
    return 255 - img


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
    """
    Subtracts background using accumulated weighted with given alpha.
    The bigger alpha is, the faster older image's residue is gone
    """

    def update(self, img: MatLike) -> MatLike:
        fimg = np.float32(img)
        absbuf = cv2.absdiff(fimg, self.background)
        cv2.accumulateWeighted(
            src=fimg,
            dst=self.background,
            alpha=self.alpha
        )
        return np.uint8(absbuf)


def extract_background_by_col_range(
        img: MatLike,
        background_low_hsv: Tuple[int, int, int],
        background_high_hsv: Tuple[int, int, int]
) -> MatLike:
    """Extract background with specified color range (HSV, not BGR)"""
    blow = np.array(background_low_hsv)
    bhigh = np.array(background_high_hsv)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_range = cv2.inRange(hsv_img, blow, bhigh)
    extracted = cv2.bitwise_and(img, img, mask=hsv_range)
    return extracted


def generate_background_pattern_image(
        img: MatLike,
        ignore_white: bool = True,
        ignore_black: bool = True,
        apply_blur: bool = True
) -> MatLike:
    """
    Generate background pattern image with black/white dot filter
    """
    buf = np.zeros(shape=img.shape)
    print(img.shape)
    h = img.shape[0]
    w = img.shape[1]
    img_x_cursor = 0
    img_y_cursor = 0
    buf_x_cursor = 0
    buf_y_cursor = 0
    while True:
        # print(f"buf({buf_x_cursor}, {buf_y_cursor}), img({img_x_cursor}, {img_y_cursor})")
        if buf_x_cursor == w:
            buf_x_cursor = 0
            buf_y_cursor += 1
            if buf_y_cursor == h:
                break
        b = img[img_y_cursor][img_x_cursor][0]
        g = img[img_y_cursor][img_x_cursor][1]
        r = img[img_y_cursor][img_x_cursor][2]
        avg = (b + g + r) / 3
        if avg < 5 and ignore_black:
            img_x_cursor += 1
            if img_x_cursor == w:
                img_x_cursor = 0
                img_y_cursor += 1
                if img_y_cursor == h:
                    img_y_cursor = 0
        elif avg > 250 and ignore_white:
            img_x_cursor += 1
            if img_x_cursor == w:
                img_x_cursor = 0
                img_y_cursor += 1
                if img_y_cursor == h:
                    img_y_cursor = 0
        else:
            buf[buf_y_cursor][buf_x_cursor][0] = img[img_y_cursor][img_x_cursor][0]
            buf[buf_y_cursor][buf_x_cursor][1] = img[img_y_cursor][img_x_cursor][1]
            buf[buf_y_cursor][buf_x_cursor][2] = img[img_y_cursor][img_x_cursor][2]
            img_x_cursor += 1
            if img_x_cursor == w:
                img_x_cursor = 0
                img_y_cursor += 1
                if img_y_cursor == h:
                    img_y_cursor = 0
            buf_x_cursor += 1
    if apply_blur:
        buf = cv2.blur(buf, [3, 3])
    return buf


class BackgroundSubtractionEffects(Effecter):
    """Effecter for background subtraction"""

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
        """execute background subtraction as an effect"""
        return self.se.update(img)
