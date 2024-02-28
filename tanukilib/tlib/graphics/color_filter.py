import cv2
from cv2.typing import MatLike
from tlib.graphics import HSVColorSchema


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
