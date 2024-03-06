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

    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
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


def filter_by_log(
        img: MatLike,
        output_img_depth: ImageDepthType,
        kernel_size: int,
        scale: float = 1.0,
        sigma_x: float = 0,
        sigma_y: float = 0
) -> MatLike:
    g = cv2.GaussianBlur(
        src=img,
        ksize=(kernel_size, kernel_size),
        sigmaX=sigma_x,
        sigmaY=sigma_y
    )
    return filter_by_laplacian(
        img=g,
        output_img_depth=output_img_depth,
        kernel_size=kernel_size,
        scale=scale
    )


def filter_by_box_mean(
        img: MatLike,
        kernel_size: int = 3,
        normalize: bool = True
) -> MatLike:
    out = np.zeros(shape=img.shape, dtype=img.dtype)
    cv2.boxFilter(
        src=img,
        ddepth=IMG_DEPTH_MAP[ImageDepthType.IMG_DEPTH_8UINT],
        dst=out,
        ksize=(kernel_size, kernel_size),
        normalize=normalize)

    width, height = out.shape
    out_buf = np.zeros(shape=img.shape, dtype=img.dtype)
    for h in range(height):
        for w in range(width):
            if img[w][h] >= out[w][h]:
                out_buf[w][h] = 255
            else:
                out_buf[w][h] = 0

    return out_buf
