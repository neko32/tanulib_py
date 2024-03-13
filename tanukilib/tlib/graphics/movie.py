import cv2
from cv2.typing import MatLike
from abc import ABC, abstractmethod
from os.path import exists
from typing import List


class Effecter(ABC):
    @abstractmethod
    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
        pass


class NoOpEffect(Effecter):
    def process(self, img: MatLike, device: cv2.VideoCapture) -> MatLike:
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
