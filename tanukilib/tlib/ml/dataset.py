from tf_keras.utils import text_dataset_from_directory
from pathlib import Path
import os
from os.path import exists
import shutil
from typing import List, Optional

def load_text_dataset(
    dataset_name:str,
    category:str,
    batch_size:int = 128,
    seed:int = 123,
    validation_split:float = 0.2,
    to_remove_dirs:Optional[List[str]] = None
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
        batch_size = batch_size,
        seed = seed,
        subset = 'training',
        validation_split = validation_split
    )

    val_ds = text_dataset_from_directory(
        dataset_path,
        batch_size = batch_size,
        seed = seed,
        subset = 'validation',
        validation_split = validation_split
    )
    return (train_ds, val_ds)
