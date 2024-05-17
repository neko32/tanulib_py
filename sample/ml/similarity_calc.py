from tlib.ml.annotated import *
from tlib.ml.dataset import get_data_dir
from pathlib import Path


def main():
    datadir = get_data_dir()
    path = str(Path(datadir).joinpath("faces_pexels", "human"))

    imgs = Viewer(path, "humanfaces")
    imgs.start_as_plain_img_viewer()
    # may SEGFAULT
    imgs.compute_similarity()
    imgs.wait()


if __name__ == "__main__":
    main()
