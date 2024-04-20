from tlib.graphics.tanutle import Tanutle
from tlib.math import Coordinate
import os
from pathlib import Path


def main():

    tmp_path = os.environ["HOME_TMP_DIR"]
    fpath = str(Path(tmp_path).joinpath("tanutle_poly.jpg"))
    t = Tanutle(500, 500)
    t.draw_poly(Coordinate(250, 350), 100, 9)

    t.save(fpath)


if __name__ == "__main__":
    main()
