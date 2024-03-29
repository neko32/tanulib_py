import cv2
from cv2.typing import MatLike
import numpy as np
from typing import Tuple, Optional, List
from os.path import isdir, exists
from os import listdir
from enum import Enum, auto

_TLIBG_W_JPG_DEFAULT = [cv2.IMWRITE_JPEG_QUALITY, 100]
_TLIBG_W_PNG_DEFAULT = [cv2.IMWRITE_PNG_STRATEGY,
                        cv2.IMWRITE_PNG_STRATEGY_DEFAULT]
_TLIG_W_FLG_MAP = {
    "png": _TLIBG_W_PNG_DEFAULT,
    "jpg": _TLIBG_W_JPG_DEFAULT,
    "jpeg": _TLIBG_W_JPG_DEFAULT,
}


class FlipDirection(Enum):
    FLIP_HORIZONTAL = 0
    FLIP_VERTICAL = 1
    FLIP_HORIZONTAL_AND_VERTICAL = -1


class ImageDepthType(Enum):
    IMG_DEPTH_8UINT = auto()
    IMG_DEPTH_8INT = auto()
    IMG_DEPTH_16UINT = auto()
    IMG_DEPTH_16INT = auto()
    IMG_DEPTH_32INT = auto()
    IMG_DEPTH_32FLOAT = auto()
    IMG_DEPTH_64FLOAT = auto()


IMG_DEPTH_MAP = {
    ImageDepthType.IMG_DEPTH_8UINT: cv2.CV_8U,
    ImageDepthType.IMG_DEPTH_8INT: cv2.CV_8S,
    ImageDepthType.IMG_DEPTH_16UINT: cv2.CV_16U,
    ImageDepthType.IMG_DEPTH_16INT: cv2.CV_16S,
    ImageDepthType.IMG_DEPTH_32INT: cv2.CV_32S,
    ImageDepthType.IMG_DEPTH_32FLOAT: cv2.CV_32F,
    ImageDepthType.IMG_DEPTH_64FLOAT: cv2.CV_64F
}


class FontFace(Enum):
    FONT_FACE_PLAIN = auto()
    FONT_FACE_ITALIC = auto()
    FONT_FACE_SIMPLEX = auto()
    FONT_FACE_TRIPLEX = auto()
    FONT_FACE_DUPLEX = auto()
    FONT_FACE_COMPLEX = auto()
    FONT_FACE_SCRIPT_SIMPLEX = auto()
    FONT_FACE_SCRIPT_COMPLEX = auto()
    FONT_FACE_COMPLEX_SMALL = auto()


FONT_FACE_MAP = {
    FontFace.FONT_FACE_PLAIN: cv2.FONT_HERSHEY_PLAIN,
    FontFace.FONT_FACE_ITALIC: cv2.FONT_ITALIC,
    FontFace.FONT_FACE_SIMPLEX: cv2.FONT_HERSHEY_SIMPLEX,
    FontFace.FONT_FACE_DUPLEX: cv2.FONT_HERSHEY_DUPLEX,
    FontFace.FONT_FACE_TRIPLEX: cv2.FONT_HERSHEY_TRIPLEX,
    FontFace.FONT_FACE_COMPLEX: cv2.FONT_HERSHEY_COMPLEX,
    FontFace.FONT_FACE_COMPLEX_SMALL: cv2.FONT_HERSHEY_COMPLEX_SMALL,
    FontFace.FONT_FACE_SCRIPT_SIMPLEX: cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    FontFace.FONT_FACE_SCRIPT_COMPLEX: cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
}


class LineType(Enum):
    LINE_TYPE_4 = auto()
    LINE_TYPE_8 = auto()
    LINE_TYPE_AA = auto()


LINE_TYPE_MAP = {
    LineType.LINE_TYPE_4: cv2.LINE_4,
    LineType.LINE_TYPE_8: cv2.LINE_8,
    LineType.LINE_TYPE_AA: cv2.LINE_AA,
}


class MarkerType(Enum):
    MARKER_TYPE_CROSS = auto()
    MARKER_TYPE_TILTED_CROSS = auto()
    MARKER_TYPE_STAR = auto()
    MARKER_TYPE_DIAMOND = auto()
    MARKER_TYPE_SQUARE = auto()
    MARKER_TYPE_TRIANGLE_UP = auto()
    MARKER_TYPE_TRIANGLE_DOWN = auto()


MARKER_TYPE_MAP = {
    MarkerType.MARKER_TYPE_CROSS: cv2.MARKER_CROSS,
    MarkerType.MARKER_TYPE_TILTED_CROSS: cv2.MARKER_TILTED_CROSS,
    MarkerType.MARKER_TYPE_STAR: cv2.MARKER_STAR,
    MarkerType.MARKER_TYPE_DIAMOND: cv2.MARKER_DIAMOND,
    MarkerType.MARKER_TYPE_SQUARE: cv2.MARKER_SQUARE,
    MarkerType.MARKER_TYPE_TRIANGLE_UP: cv2.MARKER_TRIANGLE_UP,
    MarkerType.MARKER_TYPE_TRIANGLE_DOWN: cv2.MARKER_TRIANGLE_DOWN,
}


class Rect:
    def __init__(self, x: int, y: int, w: int, h: int):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    @property
    def loc_x(self) -> int:
        return self._x

    @property
    def loc_y(self) -> int:
        return self._y

    @property
    def width(self) -> int:
        return self._w

    @property
    def height(self) -> int:
        return self._h

    def as_tuple(self) -> Tuple[int, int, int, int]:
        return (self._x, self._y, self._w, self._h)


class BGRA:
    def __init__(self, b: int, g: int, r: int, a: Optional[int] = None):
        self._b = b
        self._g = g
        self._r = r
        self._a = a

    @property
    def blue(self) -> int:
        return self._b

    @property
    def green(self) -> int:
        return self._g

    @property
    def red(self) -> int:
        return self._r

    @property
    def alpha(self) -> int:
        return self._a

    def to_tuple_bgr(self) -> Tuple[int, int, int]:
        return (self.blue, self.green, self.red)


class HSVColorSchema:

    def __init__(self, h: int, s: int, v: int):
        self._h = h
        self._s = s
        self._v = v

    @property
    def hue(self) -> int:
        return self._h

    @property
    def saturation(self) -> int:
        return self._s

    @property
    def value(self) -> int:
        return self._v

    def as_tuple(self) -> Tuple[int, int, int]:
        return (self._h, self._s, self._v)

    def as_mat(self) -> MatLike:
        return np.array([self._h, self._s, self._v])


GAMMA_CORRECTION_TOO_DARKER = 0.1
GAMMA_CORRECTION_REASONABLY_DARKER = 0.5
GAMMA_CORRECTION_REASONABLY_BRIGHTER = 2.0
GAMMA_CORRECTION_TOO_BRIGHTER = 3.0
GAMMA_CORRECTION_ALMOST_WHITE = 4.0


def imread_wrapper(fpath: str, flags: int = cv2.IMREAD_UNCHANGED) -> MatLike:
    if not exists(fpath):
        raise Exception(f"file {fpath} doesn't exist")
    return cv2.imread(fpath, flags)


def resize_img(
        src_path: str,
        dest_path: str,
        new_width: int,
        new_height: int
) -> bool:
    buf = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(buf, [new_width, new_height])
    prefix = dest_path.split('.')[-1].lower()
    cfg = _TLIG_W_FLG_MAP[prefix]
    return cv2.imwrite(dest_path, resized, cfg)


def resize_all_imgs(
        src_path: str,
        dest_path: str,
        new_width: int,
        new_height: int) -> int:
    if not (isdir(src_path) and isdir(dest_path)):
        raise Exception(f"{src_path} and {dest_path} must be directory")
    cnt = 0
    for file in listdir(src_path):
        src_file = f"{src_path}/{file}"
        dest_file = f"{dest_path}/{file}"
        cnt += 1 if resize_img(
            src_file,
            dest_file,
            new_width,
            new_height
        ) else 0

    return cnt


def copy_img(src_path: str, dest_path) -> bool:
    buf = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    prefix = dest_path.split('.')[-1].lower()
    cfg = _TLIG_W_FLG_MAP[prefix]
    return cv2.imwrite(dest_path, buf, cfg)


def from_bgr_to_gray_scale(img: MatLike) -> MatLike:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def persist_as_gray_image(src_path: str, dest_path: str) -> bool:
    buf = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
    return cv2.imwrite(dest_path, buf)


def is_grayscale(img: MatLike) -> bool:
    return len(img.shape) == 2


def invert_grayscale(img: MatLike) -> MatLike:
    return cv2.bitwise_not(img)


def affine_transform(src: MatLike, scale: int, angle: int) -> MatLike:
    h, w = src.shape[:2]
    center = (w // 2, h // 2)
    # M is affin trans matrix
    M = cv2.getRotationMatrix2D(center, angle, scale)
    # M = [a    b   c]
    #     [d    e   f]
    # a .. scale up/down against X axis. scale * cos(angle)
    # e .. scale up/down against Y axis. scale * sin(angle)
    # b .. shear/rotate against x axis
    # d .. shear/rotate against y axis
    # c .. parallel move against x axis. (1-a)*center.x - b*center.y
    # f .. parallel move against y axis. b*center.x - (1-a)*center.y
    cos_theta = np.abs(M[0, 0])
    sin_theta = np.abs(M[0, 1])
    dest_w = int(w * cos_theta + h * sin_theta)
    dest_h = int(w * sin_theta + h * cos_theta)

    # adjust gap before/after move
    M[0, 2] += (dest_w - w) / 2.0
    M[1, 2] += (dest_h - h) / 2.0

    return cv2.warpAffine(src, M, (dest_w, dest_h))


def persist_img(src: MatLike, dest_path: str) -> bool:
    return cv2.imwrite(dest_path, src)


def is_shift_invarient_for_grayscale_imgs(a: MatLike, b: MatLike) -> bool:

    if not (is_grayscale(a) and is_grayscale(b)):
        raise Exception("both a and b must be gray scale")

    a_hist = cv2.calcHist([a], [0], None, [256], [0, 256])
    b_hist = cv2.calcHist([b], [0], None, [256], [0, 256])
    return np.array_equal(a_hist, b_hist)


def conv_from_bgr_to_hsv(src: MatLike) -> MatLike:
    return cv2.cvtColor(src, cv2.COLOR_BGR2HSV)


def gen_white_canvas(w: int, h: int) -> MatLike:
    return np.full(shape=[h, w, 3], fill_value=255, dtype=np.uint8)


def gen_black_canvas(w: int, h: int) -> MatLike:
    return np.zeros(shape=[h, w, 3], dtype=np.uint8)


def draw_rect(
        a: MatLike,
        st: Tuple[int, int],
        end: Tuple[int, int],
        color: BGRA = BGRA(0, 0, 0, None),
        line_type: LineType = LineType.LINE_TYPE_8,
        line_thickness: int = 1) -> None:
    cv2.rectangle(
        a,
        pt1=st,
        pt2=end,
        color=color.to_tuple_bgr(),
        thickness=line_thickness,
        lineType=LINE_TYPE_MAP[line_type])


def fill_rect(
        a: MatLike,
        st: Tuple[int, int],
        end: Tuple[int, int],
        color: BGRA = BGRA(0, 0, 0, None),
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.rectangle(
        a,
        pt1=st,
        pt2=end,
        color=color.to_tuple_bgr(),
        thickness=-1,
        lineType=LINE_TYPE_MAP[line_type])


def draw_line(
        a: MatLike,
        st: Tuple[int, int],
        end: Tuple[int, int],
        color: BGRA = BGRA(0, 0, 0, None),
        line_thickness: int = 1,
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.line(
        a,
        pt1=st,
        pt2=end,
        color=color.to_tuple_bgr(),
        thickness=line_thickness,
        lineType=LINE_TYPE_MAP[line_type])


def draw_polylines(
        a: MatLike,
        coordinates: List[Tuple[int, int]],
        color: BGRA = BGRA(0, 0, 0, None),
        is_closed: bool = True,
        line_thickness: int = 1,
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.polylines(
        img=a,
        pts=[np.array(coordinates, np.int32).reshape((-1, 1, 2))],
        isClosed=is_closed,
        color=color.to_tuple_bgr(),
        thickness=line_thickness,
        lineType=LINE_TYPE_MAP[line_type])


def fill_polylines(
        a: MatLike,
        coordinates: List[Tuple[int, int]],
        color: BGRA = BGRA(0, 0, 0, None),
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.fillPoly(
        img=a,
        pts=[np.array(coordinates, np.int32).reshape((-1, 1, 2))],
        color=color.to_tuple_bgr(),
        lineType=LINE_TYPE_MAP[line_type])


def draw_text(
        a: MatLike,
        text: str,
        loc: Tuple[int, int],
        color: BGRA = BGRA(0, 0, 0, None),
        line_thickness: int = 1,
        line_type: LineType = LineType.LINE_TYPE_8,
        font_scale: float = 1.0,
        font_face: FontFace = FontFace.FONT_FACE_PLAIN) -> None:
    cv2.putText(a,
                text=text,
                org=loc,
                fontFace=FONT_FACE_MAP[font_face],
                fontScale=font_scale,
                color=color.to_tuple_bgr(),
                thickness=line_thickness,
                lineType=LINE_TYPE_MAP[line_type])


def draw_circle(a: MatLike,
                center_coordinate: Tuple[int, int],
                radius: int,
                color: BGRA = BGRA(0, 0, 0, None),
                line_thickness=0,
                line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.circle(
        img=a,
        center=center_coordinate,
        radius=radius,
        color=color.to_tuple_bgr(),
        thickness=line_thickness,
        lineType=LINE_TYPE_MAP[line_type])


def fill_circle(a: MatLike,
                center_coordinate: Tuple[int, int],
                radius: int,
                color: BGRA = BGRA(0, 0, 0, None),
                line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.circle(
        img=a,
        center=center_coordinate,
        radius=radius,
        color=color.to_tuple_bgr(),
        thickness=-1,
        lineType=LINE_TYPE_MAP[line_type])


def draw_ellipse(
        a: MatLike,
        center_coordinate: Tuple[int, int],
        axes: Tuple[int, int],
        angle: float = 0,
        color: BGRA = BGRA(0, 0, 0, None),
        line_thickness: int = 1,
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.ellipse(img=a,
                center=center_coordinate,
                axes=axes,
                angle=angle,
                startAngle=0,
                endAngle=360,
                color=color.to_tuple_bgr(),
                thickness=line_thickness,
                lineType=LINE_TYPE_MAP[line_type])


def fill_ellipse(
        a: MatLike,
        center_coordinate: Tuple[int, int],
        axes: Tuple[int, int],
        angle: float = 0,
        color: BGRA = BGRA(0, 0, 0, None),
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.ellipse(img=a,
                center=center_coordinate,
                axes=axes,
                angle=angle,
                startAngle=0,
                endAngle=360,
                color=color.to_tuple_bgr(),
                thickness=-1,
                lineType=LINE_TYPE_MAP[line_type])


def draw_arc(
        a: MatLike,
        center_coordinate: Tuple[int, int],
        axes: Tuple[int, int],
        angle: float = 0,
        start_angle: float = 0,
        end_angle: float = 45,
        color: BGRA = BGRA(0, 0, 0, None),
        line_thickness: int = 1,
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.ellipse(img=a,
                center=center_coordinate,
                axes=axes,
                angle=angle,
                startAngle=start_angle,
                endAngle=end_angle,
                color=color.to_tuple_bgr(),
                thickness=line_thickness,
                lineType=LINE_TYPE_MAP[line_type])


def fill_arc(
        a: MatLike,
        center_coordinate: Tuple[int, int],
        axes: Tuple[int, int],
        angle: float = 0,
        start_angle: float = 0,
        end_angle: float = 45,
        color: BGRA = BGRA(0, 0, 0, None),
        line_type: LineType = LineType.LINE_TYPE_8) -> None:
    cv2.ellipse(img=a,
                center=center_coordinate,
                axes=axes,
                angle=angle,
                startAngle=start_angle,
                endAngle=end_angle,
                color=color.to_tuple_bgr(),
                thickness=-1,
                lineType=LINE_TYPE_MAP[line_type])


def put_marker(
        a: MatLike,
        loc: Tuple[int, int],
        marker_type: MarkerType,
        color: BGRA = BGRA(0, 0, 0, None),
        line_thickness: int = 1,
        line_type: LineType = LineType.LINE_TYPE_8,
        marker_size: int = 20) -> None:
    cv2.drawMarker(
        img=a,
        position=loc,
        color=color.to_tuple_bgr(),
        markerType=MARKER_TYPE_MAP[marker_type],
        markerSize=marker_size,
        thickness=line_thickness,
        line_type=LINE_TYPE_MAP[line_type])


def get_minmax_pix_loc(img: MatLike) -> Tuple[List[int], List[int]]:
    minposs = np.where(img == np.min(img))
    maxposs = np.where(img == np.max(img))
    minposs = list(zip(minposs[0], minposs[1]))
    maxposs = list(zip(maxposs[0], maxposs[1]))

    return (minposs, maxposs)


def apply_gamma_correction(
        img: MatLike,
        gamma: float = 2.0,
) -> MatLike:
    lookup_tbl = np.zeros(shape=[256,], dtype=np.uint8)
    for i in range(256):
        lookup_tbl[i] = 255.0 * (float(i) / 255.) ** (1. / gamma)
    return cv2.LUT(img, lookup_tbl)


def is_high_contract(
    col1: Tuple[int, int, int],
    col2: Tuple[int, int, int],
    verbose: bool = False
) -> bool:
    # brightness diff test formula
    # abs((299 * R1 + 587 * G1 + 114 * B1) / 1000) -
    # (299 * R2 + 587 * G2 + 114 * B2) / 1000) > 125
    # hue diff test formula
    # abs(R1 - R2) + abs(G1 - G2) + abs(B1 - B2) > 500
    b1, g1, r1 = col1
    b2, g2, r2 = col2
    # brightness test
    bd1 = (r1 * 299 + g1 * 587 + b1 * 114) // 1000
    bd2 = (r2 * 299 + g2 * 587 + b2 * 114) // 1000
    brightness_diff = abs(bd1 - bd2)
    if verbose:
        print(f"bd1={bd1},bd2={bd2},brightness_diff={brightness_diff}")
    if brightness_diff <= 125:
        if verbose:
            print("brightness check failed - not high contract")
        return False
    hue_diff = abs(b1 - b2) + abs(g1 - g2) + abs(r1 - r2)
    if verbose:
        print(f"hue_diff={hue_diff}")
    if hue_diff <= 500:
        if verbose:
            print("hue check failed - not high contract")
            return False
    print("both brightness and hue check passed. High contract")
    return True


def add_watermark(
    base_img: MatLike,
    watermark_img: MatLike,
    watermark_ratio: float,
    gamma: float,
) -> MatLike:
    if watermark_ratio < 0 or watermark_ratio > 1.:
        raise ValueError(
            f"watermark_ratio must be between 0 and \
                1 but it was {watermark_ratio}")

    base_ratio = 1. - watermark_ratio
    return cv2.addWeighted(
        src1=base_img,
        alpha=base_ratio,
        src2=watermark_img,
        beta=watermark_ratio,
        gamma=gamma)


def flip_image(
        img: MatLike,
        flip_direction: FlipDirection
) -> MatLike:
    return cv2.flip(img, flip_direction.value)


def equalize_hist(
        img: MatLike
) -> MatLike:
    channels = cv2.split(img)
    eqhs = []
    if len(channels) != 3:
        raise Exception("input must have 3 channels")
    for i in range(len(channels)):
        eqhs.append(cv2.equalizeHist(channels[i]))
    return cv2.merge(eqhs)


def detect_corner_by_harris(
        img: MatLike,
        block_size: int = 2,
        sobel_aperture: int = 3,
        k: float = 0.04,
        threshold: float = 0.01,
        marker_color: BGRA = BGRA(0, 255, 0)
) -> MatLike:
    gray = from_bgr_to_gray_scale(img)
    dst = cv2.cornerHarris(
        src=gray,
        blockSize=block_size,
        ksize=sobel_aperture,
        k=k
    )
    retbuf = img.copy()
    retbuf[dst > threshold * dst.max()] = marker_color.to_tuple_bgr()

    return retbuf
