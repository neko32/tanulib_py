import cv2
from tlib.graphics.graphics import *
from cv2.typing import MatLike
from tlib.graphics.movie import Effecter
from enum import Enum, auto


class SOBELOrder(Enum):
    """Determines order of SOBEL Filter, X or Y"""
    ORDER_X = auto()
    ORDER_Y = auto()


class LaplacianEffecter(Effecter):
    """Effecter to apply Laplacian Filter"""

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
        """Cause laplacian filter effect"""
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
    """
    Filter by laplacian filter
    """
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
    """Filter Gaussian blur first and then apply laplacian filter"""
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
    """Apply box mean filtering"""
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


def filter_by_SOBEL(
        img: MatLike,
        output_img_depth: ImageDepthType,
        order: SOBELOrder,
        kernel_size: int = 3,
        scale: float = 1.,
        delta: float = 0.,
) -> MatLike:
    """Apply SOBEL filter. Need to specify X or Y"""
    dx, dy = (1, 0) if order == SOBELOrder.ORDER_X else (0, 1)
    return cv2.Sobel(
        src=img,
        ddepth=IMG_DEPTH_MAP[output_img_depth],
        dx=dx,
        dy=dy,
        ksize=kernel_size,
        scale=scale,
        delta=delta
    )
