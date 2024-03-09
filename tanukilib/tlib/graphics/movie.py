import cv2
from cv2.typing import MatLike
from abc import ABC, abstractmethod
from os.path import exists
from typing import List
from tlib.graphics import draw_text, from_bgr_to_gray_scale, BGRA
from collections import OrderedDict


class Effecter(ABC):
    @abstractmethod
    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        pass


class NoOpEffect(Effecter):
    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        return img

class GrayImageEffecter(Effecter):
    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        return from_bgr_to_gray_scale(img)

class MovieInfoOverlayEffect(Effecter):

    def __init__(self, loc_x: int, loc_y: int):
        self.cache = OrderedDict()
        self.loc_x = loc_x
        self.loc_y = loc_y

    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        if len(self.cache) == 0:
            self.cache["FRAME_WIDTH"] = device.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.cache["FRAME_HEIGHT"] = device.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.cache["FPS"] = device.get(cv2.CAP_PROP_FPS)
            self.cache["FOURCC"] = device.get(cv2.CAP_PROP_FOURCC)
            self.cache["FORMAT"] = device.get(cv2.CAP_PROP_FORMAT)
            self.cache["TOTAL_FRAME_COUNT"] = device.get(
                cv2.CAP_PROP_FRAME_COUNT)
            print(self.cache)
        cur_loc = device.get(cv2.CAP_PROP_POS_FRAMES)

        loc_y = self.loc_y
        loc_x = self.loc_x

        for k, v in self.cache.items():
            draw_text(
                a=img,
                text=f"{k}:{v}",
                line_thickness=1,
                color=BGRA(255, 255, 255),
                font_scale=1,
                loc=(loc_x, loc_y)
            )
            loc_y += 20
        draw_text(
            a=img,
            text=f"CURRENT_FRAME:{cur_loc}",
            line_thickness=1,
            color=BGRA(255, 255, 255),
            font_scale=1,
            loc=(loc_x, loc_y)
        )
        return img


class MoviePlay:

    def __init__(self, index: int, api_pref: int):
        self.index = index
        self.api_pref = api_pref

    def play(
            self,
            movie_file_path: str,
            wnd_name: str,
            effects: List[Effecter]) -> None:
        if not exists(movie_file_path):
            raise Exception(f"file {movie_file_path} not found")
        vt = cv2.VideoCapture(self.index, self.api_pref)
        if not vt.open(movie_file_path):
            raise Exception(f"movie {movie_file_path} failed to play")

        while True:
            read_success, r = vt.read()
            if not read_success:
                break

            for effect in effects:
                r = effect.process(r, vt)

            cv2.imshow(wnd_name, r)

            key = cv2.waitKey(30) & 0xFF
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
        vt.release()
