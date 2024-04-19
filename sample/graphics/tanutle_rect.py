from tlib.graphics.tanutle import Tanutle
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

    t.save(fpath)


if __name__ == "__main__":
    main()
