import tensorflow_hub as tfhub
import tensorflow as tf
from tlib.ml import load_img_as_1d
from typing import Tuple

def perform_style_transfer_with_AISV1(
    dataset_name: str,
    category: str,
    base_file_name: str,
    base_size: Tuple[int, int],
    style_file_name: str,
    style_size: Tuple[int, int],
    normalize_with_0_1:bool = True,
    verbose:bool = False,
):
    model = tfhub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2")
    base_img = load_img_as_1d(dataset_name, category, base_file_name, base_size)
    style_img = load_img_as_1d(dataset_name, category, style_file_name, style_size)
    if normalize_with_0_1:
        base_img = base_img / 255.
        style_img = style_img / 255.
    if verbose:
        print(base_img)
        print(type(base_img).__name__)
        print(style_img)
        print(type(style_img).__name__)

    outputs = model(tf.constant(base_img), tf.constant(style_img))
    return outputs
