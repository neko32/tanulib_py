import keras
import numpy as np
import os
from pathlib import Path
from os.path import exists
from typing import Tuple, Dict, Optional
from numpy.typing import NDArray
from keras.preprocessing.image import load_img, img_to_array


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


def load_dataset_from_npz(file_path: str) -> Dict[str, NDArray]:
    if not exists(file_path):
        raise Exception(f"{file_path} doesn't exist.")
    loaded = np.load(file_path)
    dict = {}
    for file in loaded.files:
        dict[file] = loaded[file]
    return dict


def load_images_from_dir(
        dir_name: str,
        target_size: Tuple[int, int],
        glob_exp: str = "*.jpg",
        do_sort: bool = True,
        max_num_to_load: Optional[int] = None
) -> Tuple[NDArray, NDArray]:
    """
    load multiple images from specified dir with resizing.
    Return values are tuple of (image path list, loaded images)
    """
    img_paths = []
    for img_path in Path(dir_name).glob(glob_exp):
        img_paths.append(img_path)
    if do_sort:
        img_paths.sort()
    imgs = []
    siz = len(img_paths) if max_num_to_load is None else min(
        max_num_to_load, len(img_paths))
    for idx, img_path in enumerate(img_paths):
        if idx % 100 == 0:
            print(f"processed {idx}/{siz} so far..")
        img = load_img(img_path, target_size=target_size)
        nd_img = img_to_array(img)
        imgs.append(nd_img)
        if max_num_to_load is not None and idx == max_num_to_load - 1:
            break
    print(f"loaded {siz} records.")

    return (np.array(img_paths), np.array(imgs))
