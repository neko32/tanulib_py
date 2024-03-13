
from tlib.graphics.movie import *
from tlib.graphics.ext_effects import MovieInfoOverlayEffect
import cv2


def main():
    effecters = [MovieInfoOverlayEffect(20, 20)]
    #effecters = [NoOpEffect()]
    movie = MoviePlay(0, cv2.CAP_ANY)
    movie.play("../mov/test_movie.mp4", "tlib::movie play", effecters)


if __name__ == "__main__":
    main()
