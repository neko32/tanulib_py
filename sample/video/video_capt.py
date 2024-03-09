
from tlib.graphics.movie import *
from tlib.graphics.video import *
import cv2


def main():
    # effecters = [MovieInfoOverlayEffect(20, 20)]
    effecters = [NoOpEffect()]
    vt = VideoCapturer(0, cv2.CAP_ANY)
    vt.capture("tlib::movie play", effecters)


if __name__ == "__main__":
    main()
