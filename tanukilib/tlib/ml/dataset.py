from tf_keras.utils import text_dataset_from_directory
from keras.preprocessing.image import load_img
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
import PIL.Image as pilimg
from PIL.Image import Image


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


def extract_imagebytes_from_1darray(
        images: NDArray,
        height_hint: int,
        width_hint: int,
        dim_hint: int,
        index: int
) -> NDArray:
    """
    Extract image bytes from image 1D array from given index.
    Stride is derived from given height, width and dimension hint.
    """
    stride = height_hint * width_hint * dim_hint
    st = stride * index
    end = st + stride
    return images[st:end]


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


def show_PIL_image(img: Image) -> None:
    """Show PIL image"""
    img.show()


def show_NDArray_image(ndimg: NDArray) -> None:
    """Show NDArray image"""
    n = np.array(ndimg, dtype='uint8')
    img = pilimg.fromarray(n)
    show_PIL_image(img)


def show_multiple_images_as_rank(
        indices_to_show,
        scores,
        images: NDArray,
        image_size_to_show: Tuple[int, int],
        begin_rank_num: int = 0,
        figure_size: Tuple[int, int] = (20, 20),
        feature_image_idx: Optional[int] = None
) -> None:
    """
    Show multiple images specified in indices_to_show from images
    """

    rank = begin_rank_num
    plt.subplot(4, 3, rank + 1)
    plt.figure(figsize=figure_size)

    if feature_image_idx is not None:
        featured_img = load_img(
            images[feature_image_idx], target_size=image_size_to_show)
        plt.title(f"feature img {images[feature_image_idx].name}")
        plt.imshow(featured_img)
    for idx, score in zip(indices_to_show, scores):
        plt.subplot(4, 3, rank + 1)
        fpath = images[idx]
        subject = f"rank: {rank}, idx: {idx}, score: {score},\npath: {fpath.name}"
        plt.title(subject)
        img = load_img(fpath, target_size=image_size_to_show)
        plt.imshow(img)
        rank += 1

    plt.show()


def derive_path_for_dataset(
        dataset: str,
        category: Optional[str],
        existance_check: bool = True
) -> str:
    """Derive path given data set and optionally category"""
    ml_data_path = Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(dataset)
    if category is not None:
        ml_data_path = ml_data_path.joinpath(category)
    if existance_check:
        if not ml_data_path.exists():
            raise Exception(f"{str(ml_data_path)} doesn't exist")
    return str(ml_data_path)


def get_data_dir() -> str:
    """Get ML data dir registered"""
    path = Path(os.environ["TLIB_ML_DATA_DIR"])
    if not path.exists():
        raise Exception("TLIB_ML_DATA_DIR env variable must be set")
    return str(path)
