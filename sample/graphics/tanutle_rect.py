from tlib.graphics.tanutle import Tanutle
from tlib.graphics.graphics import BGRA
import os
from pathlib import Path


def main():

    tmp_path = os.environ["HOME_TMP_DIR"]
    fpath = str(Path(tmp_path).joinpath("tanutle_rect.jpg"))
    t = Tanutle(500, 500)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.home()
    t.pen_color(BGRA(255, 255, 0))
    t.pen_size(3)
    t.forward(100)
    t.right(90)
    t.pen_up()
    t.forward(100)
    t.right(90)
    t.pen_down()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(45)
    t.pen_color(BGRA(0, 255, 0))
    t.forward(250)
    t.pen_color(BGRA(0, 0, 255))
    t.backward(125)
    t.set_x(0)
    t.set_y(0)
    t.pen_size(1)
    t.pen_color(BGRA(128, 128, 128))
    t.reset_angle()
    t.right(45)
    t.forward(220)

    t.save(fpath)


if __name__ == "__main__":
    main()
