from tlib.ml.dataset import (
    cifar_pickle_load,
    extract_imagebytes_from_1darray
)
import numpy as np
import os
from tlib.graphics import persist_img
from pathlib import Path


def main():
    img_file = Path(os.environ["HOME_TMP_DIR"]).joinpath("cifar10_extract.jpg")
    if img_file.exists():
        img_file.unlink()

    (tr_x, _), (_, _) = cifar_pickle_load(
        "CIFAR10",
        "cifar-10-batches-py"
    )
    img = tr_x[32]
    persist_img(img, str(img_file))


if __name__ == "__main__":
    main()
