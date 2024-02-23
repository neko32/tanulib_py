
from tlib.graphics.movie import *
import cv2


def main():
    effecters = [NoOpEffect()]
    movie = MoviePlay(0, cv2.CAP_ANY)
    movie.play("../mov/test_movie.mp4", "tlib::movie play", effecters)


if __name__ == "__main__":
    main()
