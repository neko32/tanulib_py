
from tlib.graphics.movie import *
from tlib.graphics import Rect
import cv2


def main():
    mse = MeanShiftEffect(
        Rect(270, 140, 100, 100),
        boundingbox_color=BGRA(255, 255, 0),
        boundingbox_line_type=LineType.LINE_TYPE_AA,
        boundingbox_thickness=2)
    effecters = [(mse)]
    movie = MoviePlay(0, cv2.CAP_ANY)
    movie.play("../mov/test_movie.mp4", "tlib::movie play", effecters)


if __name__ == "__main__":
    main()
