from tf_keras.utils import text_dataset_from_directory
from pathlib import Path
import os
from os.path import exists
import shutil
from typing import List, Optional, Tuple
import pickle
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tlib.graphics.img_info import get_exif_data
from tlib.datautil.map import pprint_with_sort


def load_text_dataset(
    dataset_name: str,
    category: str,
    batch_size: int = 128,
    seed: int = 123,
    validation_split: float = 0.2,
    to_remove_dirs: Optional[List[str]] = None
):
    """
    Load text data set from specified dataset_name and category
    """
    if os.environ['TLIB_ML_DATA_DIR'] is None:
        raise Exception("TLIB_ML_DATA_DIR must be set")
    dataset_path = str(Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(
        dataset_name, category))
    if not exists(dataset_path):
        raise Exception(f"{dataset_path} doesn't exist")

    if to_remove_dirs is not None:
        for rm_dir in to_remove_dirs:
            dpath = Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(
                dataset_name,
                category,
                rm_dir
            )
            if dpath.exists():
                shutil.rmtree(str(dpath))

    train_ds = text_dataset_from_directory(
        dataset_path,
        batch_size=batch_size,
        seed=seed,
        subset='training',
        validation_split=validation_split
    )

    val_ds = text_dataset_from_directory(
        dataset_path,
        batch_size=batch_size,
        seed=seed,
        subset='validation',
        validation_split=validation_split
    )
    return (train_ds, val_ds)


def cifar_pickle_load(
    dataset_name: str,
    category: str
) -> Tuple[Tuple[NDArray, NDArray], Tuple[NDArray, NDArray]]:
    """
    load CIFAR10 which is serialized with pickle.
    CIFAR10 contains 5 batch files and each batch file contain
    10000 images with 32 * 32 * 3.
    Num of categories are 10
    """
    tr_x = []
    tr_y = []
    val_x = []
    val_y = []
    if os.environ['TLIB_ML_DATA_DIR'] is None:
        raise Exception("TLIB_ML_DATA_DIR must be set")

    for i in range(1, 7):
        fname = f"data_batch_{i}" if i != 6 else "test_batch"
        print(f"processing {fname}..")
        dataset_path = str(Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(
            dataset_name, category, fname))
        if not exists(dataset_path):
            raise Exception(f"{dataset_path} doesn't exist")

        with open(dataset_path, 'rb') as fd:
            dict = pickle.load(fd, encoding='bytes')

        if i != 6:
            tr_x.append(dict[b'data'])
            tr_y.append(dict[b'labels'])
        else:
            val_x.append(dict[b'data'])
            val_y.append(dict[b'labels'])

    tr_x = np.reshape(tr_x, newshape=[50000, 32, 32, 3])
    tr_y = np.reshape(tr_y, newshape=[50000])
    val_x = np.reshape(val_x, newshape=[10000, 32, 32, 3])
    val_y = np.reshape(val_y, newshape=[10000])

    return ((tr_x, tr_y), (val_x, val_y))


def pick_image_file(
        dataset: str,
        category: Optional[str],
        file_name: str,
        show_file: bool = False,
        dump_exif_info: bool = False
) -> str:
    """Pick ML training data image file. If show_file is true, the image is displayed"""
    ml_data_file = Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(dataset)
    if category is not None:
        ml_data_file = ml_data_file.joinpath(category)
    ml_data_file = ml_data_file.joinpath(file_name)
    if not ml_data_file.exists():
        raise Exception(f"{str(ml_data_file)} not exist")
    ml_data_file_s = str(ml_data_file)
    img = mpimg.imread(ml_data_file_s)
    if dump_exif_info:
        exif = get_exif_data(ml_data_file_s)
        print("--- EXIF INFO BEGIN ---")
        pprint_with_sort(exif)
        print("--- EXIF INFO END ---")
    _ = plt.imshow(img)
    if show_file:
        plt.show()
    return ml_data_file_s
