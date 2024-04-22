from tlib.graphics.tanutle import Tanutle
from tlib.math.math import Coordinate
import os
from pathlib import Path


def main():

    tmp_path = os.environ["HOME_TMP_DIR"]
    fpath = str(Path(tmp_path).joinpath("tanutle_fractal.jpg"))
    t = Tanutle(500, 500)
    t.fractal(Coordinate(250, 250), 200, 2, [120, 120], 5)

    t.save(fpath)


if __name__ == "__main__":
    main()
