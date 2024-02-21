import cv2
from tlib.graphics.graphics import *
from cv2.typing import MatLike


def filter_by_laplacian(
        img: MatLike,
        output_img_depth: ImageDepthType,
        kernel_size: int
) -> MatLike:
    return cv2.Laplacian(
        src=img,
        ddepth=IMG_DEPTH_MAP[output_img_depth],
        ksize=kernel_size
    )
