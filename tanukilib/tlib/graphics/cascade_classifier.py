from tlib.graphics.video import Effecter
from tlib.graphics.graphics import (
    from_bgr_to_gray_scale,
    draw_rect,
    BGRA,
    roi,
    persist_img
)
import cv2
from cv2.typing import MatLike
from typing import Tuple
from enum import Enum
from pathlib import Path
import os


class CascadeClassifierFilter(Enum):
    HUMAN_FRONT_FACE = "frontface"
    CAT = "cat"
    CAT_EXT = "cat_ext"


class CascadeClassifier(Effecter):

    def __init__(
        self,
        classifier_name: CascadeClassifierFilter,
        min_posible_obj_size=Tuple[int, int],
        max_possible_obj_size=Tuple[int, int],
        scale_factor: float = 1.1,
        min_neighbors: int = 3,
        convert_to_gray: bool = True,
        roi_color: BGRA = BGRA(255, 0, 0),
        roi_thickness: int = 1,
        narrow_down_by_eye_check: bool = True,
        persist_found_roi=True
    ):
        """Specifies settings for filter and filter name"""
        conf_dir = os.environ["TANULIB_CONF_DIR"]
        if conf_dir is None:
            raise Exception("TANULIB_CONF_DIR env value must be set")

        filter_name = f"{classifier_name.value}.xml"
        filter_file_path = Path(conf_dir).joinpath(
            "tlib", "cascade_classifier", filter_name)
        if not filter_file_path.exists():
            raise Exception(f"cc filter {str(filter_file_path)} doesn't exist")
        self.filter_file_path = str(filter_file_path)
        self.eyefilter_file_path = str(
            filter_file_path.parent.joinpath("eye.xml"))
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.min_possible_obj_size = min_posible_obj_size
        self.max_possible_obj_size = max_possible_obj_size
        self.convert_to_gray = convert_to_gray
        self.roi_thickness = roi_thickness
        self.roi_color = roi_color
        self.narrow_down_by_eye_check = narrow_down_by_eye_check
        self.persist_found_roi = persist_found_roi

    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        """apply cascade classifier with given filter file"""
        cc = cv2.CascadeClassifier(self.filter_file_path)
        target = from_bgr_to_gray_scale(img) if self.convert_to_gray else img
        found = cc.detectMultiScale(
            image=target,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_possible_obj_size,
            maxSize=self.max_possible_obj_size
        )
        idx = 0
        for (x, y, w, h) in found:
            if self.narrow_down_by_eye_check:
                cc_eye = cv2.CascadeClassifier(self.eyefilter_file_path)
                # print(f"x={x},y={y},w={w},h={h}")
                # print(roi_img.shape)
                roi_img = roi(img, x, w, y, h)

                if self.persist_found_roi:
                    roi_save_path = Path(
                        os.environ["HOME_TMP_DIR"]).joinpath(f"roi_{idx}.jpg")
                    persist_img(roi_img, str(roi_save_path))
                idx += 1

                eye_found = cc_eye.detectMultiScale(
                    image=roi_img,
                    scaleFactor=self.scale_factor,
                    minNeighbors=3,
                    minSize=[1, 1],
                    maxSize=[w, h]
                )
                if len(eye_found) > 0:
                    print("eyes found in the ROI..")
                    draw_rect(
                        a=img,
                        st=[x, y],
                        end=[x + w, y + h],
                        color=self.roi_color,
                        line_thickness=self.roi_thickness
                    )
            else:
                draw_rect(
                    a=img,
                    st=[x, y],
                    end=[x + w, y + h],
                    color=self.roi_color,
                    line_thickness=self.roi_thickness
                )
        return img
