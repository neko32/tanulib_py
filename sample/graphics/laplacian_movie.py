
from tlib.graphics.movie import *
from tlib.graphics.conv_filter import LaplacianEffecter
from tlib.graphics.graphics import ImageDepthType
from tlib.graphics.ext_effects import GrayImageEffecter
import cv2


def main():
    effecters = [
        GrayImageEffecter(),
        LaplacianEffecter(
            output_img_depth=ImageDepthType.IMG_DEPTH_8UINT,
            kernel_size=3,
            scale=1.1
        )]
    movie = MoviePlay(0, cv2.CAP_ANY)
    movie.play("../mov/test_movie.mp4", "tlib::movie play", effecters)


if __name__ == "__main__":
    main()
