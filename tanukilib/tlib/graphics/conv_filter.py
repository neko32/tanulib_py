import cv2
from tlib.graphics.graphics import *
from cv2.typing import MatLike
from tlib.graphics.movie import Effecter


class LaplacianEffecter(Effecter):

    def __init__(
        self,
        output_img_depth: ImageDepthType,
        kernel_size: int,
        scale: float = 1.0
    ) -> None:
        self.output_img_depth = output_img_depth
        self.kernel_size = kernel_size
        self.scale = scale

    def process(self, img: MatLike) -> MatLike:
        return filter_by_laplacian(
            img,
            self.output_img_depth,
            self.kernel_size,
            self.scale
        )


def filter_by_laplacian(
        img: MatLike,
        output_img_depth: ImageDepthType,
        kernel_size: int,
        scale: float = 1.0
) -> MatLike:
    return cv2.Laplacian(
        src=img,
        ddepth=IMG_DEPTH_MAP[output_img_depth],
        scale=scale,
        ksize=kernel_size
    )
