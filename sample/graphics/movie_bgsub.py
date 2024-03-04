
from tlib.graphics.movie import *
from tlib.graphics.color_filter import BackgroundSubtractionEffects
import cv2


def main():
    bge = BackgroundSubtractionEffects(
        frame_width=500,
        frame_height=282,
        alpha=1.
    )
    effecters = [(bge)]
    movie = MoviePlay(0, cv2.CAP_ANY)
    movie.play("../mov/test_movie.mp4", "tlib::movie play", effecters)


if __name__ == "__main__":
    main()
