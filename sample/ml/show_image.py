from tlib.ml.dataset import pick_image_file
from pathlib import Path


def main():
    pathv = str(Path("arnaud_landscape_pictures").joinpath("archive"))
    pick_image_file(pathv, None, "00000002.jpg", True, True)


if __name__ == "__main__":
    main()
