import keras
import numpy as np
import os
from pathlib import Path
from os.path import exists
from typing import Tuple


def load_img_as_1d(
    dataset_name: str,
    category: str,
    file_name: str,
    size: Tuple[int, int]
) -> np.ndarray:
    """
    load an image as 1st tensor
    """
    if os.environ['TLIB_ML_DATA_DIR'] is None:
        raise Exception("TLIB_ML_DATA_DIR must be set")
    dataset_path = str(Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(
        dataset_name, category, file_name))
    if not exists(dataset_path):
        raise Exception(f"{dataset_path} doesn't exist")
    raw_img = keras.utils.load_img(dataset_path, target_size=size)
    img = keras.utils.img_to_array(raw_img)
    return np.expand_dims(img, axis=0)
