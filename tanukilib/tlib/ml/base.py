import keras
from keras.models import Model
from keras.layers import Input, Dense, RandomRotation, RandomFlip
from keras.optimizers import SGD
import tensorflow as tf
from typing import List, Any, Optional, Tuple
import os
from pathlib import Path
from enum import Enum
from os.path import exists

PREFERRED_IMG_SIZE_CATDOG = (180, 180)
# PREFERRED_BATCH_SIZE_CATDOG = 128
PREFERRED_BATCH_SIZE_CATDOG = 16


class FlipMode(Enum):
    """
    DA Flip mode
    """
    FLIP_HORIZONTAL = "vertical"
    FLIP_VERTICAL = "horizontal"
    FLIP_HORIZONTAL_AND_VERTICAL = "horizontal_and_vertical"


class LabelMode(Enum):
    """
    Label mode
    """
    LABELMODE_INT_FOR_SPARSE_CAT_CROSSENTROPY = "int"
    LABELMODE_CAT_FOR_CAT_CROSSENTROPY = "categorical"
    LABELMODE_BIN_FOR_BIN_CROSSENTROPY = "binary"


class ModelBuilder:
    """
    Build model
    """

    def __init__(self, ipt_shape: List[Any]):
        """
        Take shape for input
        """
        self.input = Input(shape=ipt_shape)
        self.output = None
        self.model_buf = self.input

    def set_output(self, units: int, activation: str) -> None:
        """
        Set output layer
        """
        self.output = Dense(units=units, activation=activation)(self.model_buf)

    def build(self) -> Model:
        """
        Build a model with given input and output def
        """
        return Model(inputs=self.input, outputs=self.output)


class DataAugumentation:
    """
    Manages DA
    """

    def __init__(self):
        self.da_layers = []

    def add_rotation(self, factor: float = 0.1) -> None:
        """
        Add rotation with rotation factor
        """
        self.da_layers.append(RandomRotation(factor=factor))

    def add_flip(
        self,
        direction: FlipMode = FlipMode.FLIP_HORIZONTAL
    ) -> None:
        self.da_layers.append(RandomFlip(mode=direction.value))
        """
        add flip with given flip mode direction
        """

    def apply(self, images):
        """
        Apply filters
        """
        for layer in self.da_layers:
            images = layer(images)
        return images


class InputDataPreprocessor:
    """
    Preprocessor for input data
    """

    def __init__(self, dataset_name: str) -> None:
        """
        Data set is set.
        Data set is assumed to be located in TLIB_MLD_DATA_DIR
        """
        if os.environ['TLIB_ML_DATA_DIR'] is None:
            raise Exception("TLIB_ML_DATA_DIR must be set")
        dataset_path = str(
            Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath(dataset_name))
        if not exists(dataset_path):
            raise Exception(f"{dataset_path} doesn't exist")
        self.dataset_path = dataset_path

    def load(
        self,
        image_size: Tuple[int, int],
        batch_size: int = 30,
        label_mode: LabelMode = LabelMode.LABELMODE_INT_FOR_SPARSE_CAT_CROSSENTROPY,
        validation_split: float = 0.2,
        seed: Optional[Any] = None,
    ):
        """
        Load data for training and validation
        """
        tr_ds, val_ds = keras.utils.image_dataset_from_directory(
            directory=self.dataset_path,
            label_mode=label_mode.value,
            subset='both',
            validation_split=validation_split,
            seed=seed,
            image_size=image_size,
            batch_size=batch_size
        )
        return (tr_ds, val_ds)


def make_model_with_scalar_input_single_hidden_fc(
        input_shape: Tuple[int],
        num_neurons_in_hidden_layer: int,
        num_output: int,
        hidden_layer_activation: str = 'sigmoid',
        output_layer_activiation: str = 'sigmoid'
) -> keras.Model:
    """
    Build model which is the simplest structure to solve non-linear problem.
    Input - Hidden -> Output
    """
    input = Input(shape=input_shape)
    x = Dense(
        num_neurons_in_hidden_layer,
        activation=hidden_layer_activation)(input)
    output = Dense(units=num_output, activation=output_layer_activiation)(x)
    return keras.Model(input, output)


def make_model_CBA_with_MP_GAP_plus_residual(
        input_shape_without_channel: Tuple[int, int],
        num_channels: int,
        num_classes: int,
        kernel_size: int,
        residual_kernel_size: int = 1,
        strides: int = 2,
        dropout_at_fc: float = 0.2,
        per_phase_filter: List[int] = [128, 256, 512, 728, 1024],
        activation_fn: str = 'relu',
        normalize_pix: bool = True
) -> keras.Model:
    """
    Build a model with the following specs:
    - Input data is rescaled with 1. / 255 if normalize_pix is True
    - Post entry is repetative CBA (Seperable Conv2D, BatchNorm, Activation)
    - Conv-Conv is connected with MP
    - Skip Connection is installed
    - Conv-FC is connected with GAP
    - padding mode is 'same'
    """
    input_shape = input_shape_without_channel + (num_channels,)
    inputs = Input(shape=input_shape)

    # entry
    if normalize_pix:
        x = keras.layers.Rescaling(1. / 255)(inputs)
        x = keras.layers.Conv2D(
            filters=per_phase_filter[0],
            kernel_size=kernel_size,
            strides=strides,
            padding='same')(x)
    else:
        x = keras.layers.Conv2D(
            filters=per_phase_filter[0],
            kernel_size=kernel_size,
            strides=strides,
            padding='same')(inputs)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation(activation_fn)(x)

    # for residual
    prev_block_activation = x

    for filt_size in per_phase_filter[1:-1]:
        x = keras.layers.Activation(activation_fn)(x)
        x = keras.layers.SeparableConv2D(
            filters=filt_size,
            kernel_size=kernel_size,
            padding='same'
        )(x)
        x = keras.layers.BatchNormalization()(x)

        x = keras.layers.Activation(activation_fn)(x)
        x = keras.layers.SeparableConv2D(
            filters=filt_size,
            kernel_size=kernel_size,
            padding='same'
        )(x)
        x = keras.layers.BatchNormalization()(x)

        x = keras.layers.MaxPooling2D(
            pool_size=kernel_size,
            strides=strides,
            padding='same'
        )(x)

        residual = keras.layers.Conv2D(
            filters=filt_size,
            kernel_size=residual_kernel_size,
            strides=strides,
            padding='same'
        )(prev_block_activation)

        x = keras.layers.add([x, residual])
        prev_block_activation = x

        # end of per filter CBA+MP loop

    # last CBA then GAP to FC
    x = keras.layers.SeparableConv2D(
        filters=per_phase_filter[-1],
        kernel_size=kernel_size,
        padding='same'
    )(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation(activation_fn)(x)

    # to FC via GBP
    x = keras.layers.GlobalAveragePooling2D()(x)
    units = 1 if num_classes == 2 else num_classes
    x = keras.layers.Dropout(dropout_at_fc)(x)
    outputs = keras.layers.Dense(units=units, activation=None)(x)
    return keras.Model(inputs, outputs)


def get_available_gpu_devices() -> bool:
    return tf.config.list_physical_devices('GPU')


def gen_default_SGD(lr: float = 0.01) -> SGD:
    return SGD(learning_rate=lr)
