
from tlib.graphics.movie import MoviePlay
from tlib.graphics.morph_filter import SkeltonizationEffect
import cv2


def main():
    ske = SkeltonizationEffect()
    effecters = [(ske)]
    movie = MoviePlay(0, cv2.CAP_ANY)
    movie.play("../mov/test_movie.mp4", "tlib::movie play", effecters)


if __name__ == "__main__":
    main()
