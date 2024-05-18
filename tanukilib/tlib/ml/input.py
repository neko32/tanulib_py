from abc import ABC, abstractmethod
import os
from pathlib import Path
from tlib.ml import load_dataset_from_npz
from keras.utils import to_categorical


class InputManager(ABC):
    """Manages input data loading & prepcoessing"""

    def __init__(self):
        self.x_train = None
        self.y_trian = None
        self.x_test = None
        self.y_test = None

    @abstractmethod
    def load_data(self) -> None:
        """Load data"""
        pass

    @abstractmethod
    def name(self) -> str:
        """get data set name"""
        pass

    @abstractmethod
    def do_preprocessing(self) -> None:
        """Perform preprocessing"""
        pass

    def process(self) -> None:
        """Perform input prep processing"""
        print(
            f"performing input data loading & preprocessing for {self.name()}")
        print(
            f"each input shape - {self.input_shape()}, number of category - {self.num_category()}")

        print("STEP1: [BEGIN] starting loading data ..")
        self.load_data()
        print("STEP1: [DONE] loading data done.")
        print("STEP2: [BEGIN] starting preprocessing .. ")
        self.do_preprocessing()
        print("STEP2: [DONE] preprocessing complete. ")
        print("All input data loading & preprocessing complete.")

    @abstractmethod
    def input_shape(self) -> list[int]:
        """get input shape"""
        pass

    @abstractmethod
    def num_category(self) -> int:
        """num of category"""
        pass


class MNIST10Input(InputManager):
    """Input Loading & Preprocessing for MNIST10"""

    def load_data(self) -> None:
        """Load data DMZ"""
        self.datapath = str(
            Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath("MNIST10", "mnist.npz"))

    def do_preprocessing(self) -> None:
        """
        perform preprocessing.
        MNIST10 data consists of 1 channel 28*28 and category 10
        """
        d = load_dataset_from_npz(str(self.datapath))

        print("x_train, x_test's value range is 0..=255")
        print("for the training and validation, apply /.255 ..")

        # redact tensor from 2D to scalar
        x_train = d["x_train"].reshape(-1, 28 * 28)
        x_train = x_train / 255
        y_train = to_categorical(d["y_train"], 10)

        # redact tensor from 2D to scalar
        x_test = d["x_test"].reshape(-1, 28 * 28)
        x_test = x_test / 255
        y_test = to_categorical(d["y_test"], 10)

        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def name(self) -> str:
        return "MNIST10"

    def input_shape(self) -> list[int]:
        """get input image shape"""
        return [28, 28, 1]

    def num_category(self) -> int:
        """num of category"""
        return 10
