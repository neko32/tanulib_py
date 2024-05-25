from abc import ABC, abstractmethod
import os
from pathlib import Path
from tlib.datautil.vector import transform_tensor_with_folded_1d_bottom
from tlib.ml import load_dataset_from_npz
from keras.utils import to_categorical


class InputManager(ABC):
    """Manages input data loading & prepcoessing"""

    def __init__(self):
        self.x_train = None
        self.y_trian = None
        self.x_test = None
        self.y_test = None
        self.raw_data = None

    @abstractmethod
    def load_data(self) -> None:
        """Load data"""
        pass

    @abstractmethod
    def preprocess_x_train(self):
        """preprocess x_train"""

    @abstractmethod
    def preprocess_y_train(self):
        """preprocess y_train"""

    @abstractmethod
    def preprocess_x_test(self):
        """preprocess x_test"""

    @abstractmethod
    def preprocess_y_test(self):
        """preprocess y_test"""

    def preprocess_in_bulk(self):
        """If preprocessing needs to be done in one shot for x and y train & val, use this"""
        pass

    @abstractmethod
    def name(self) -> str:
        """get data set name"""
        pass

    def do_preprocessing(self) -> None:
        """Perform preprocessing"""
        try:
            self.show_message_before_preprocess()
            self.preprocess_x_train()
            self.preprocess_y_train()
            self.preprocess_x_test()
            self.preprocess_y_test()
            self.preprocess_in_bulk()
            self.raw_data = None
        except Exception as e:
            print(e)
            raise e

    @abstractmethod
    def show_message_before_preprocess(self):
        """Show some useful info before starting preprocess"""
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
        if self.x_train is None or self.y_train is None or \
                self.x_test is None or self.y_test is None:
            print(self.x_train)
            print(self.y_train)
            print(self.x_test)
            print(self.y_test)
            raise Exception("input data prep is not done fully")

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
        self.raw_data = load_dataset_from_npz(str(self.datapath))

    def show_message_before_preprocess(self):
        print("x_train, x_test's value range is 0..=255")
        print("for the training and validation, apply /.255 ..")


    def preprocess_x_train(self):
        # redact tensor from 2D to scalar
        x_train = transform_tensor_with_folded_1d_bottom(self.raw_data["x_train"], 28 * 28)
        self.x_train = x_train / 255

    def preprocess_y_train(self):
        self.y_train = to_categorical(self.raw_data["y_train"], 10)

    def preprocess_x_test(self):
        x_test = transform_tensor_with_folded_1d_bottom(self.raw_data["x_test"], 28 * 28)
        self.x_test = x_test / 255

    def preprocess_y_test(self):
        self.y_test = to_categorical(self.raw_data["y_test"], 10)

    def name(self) -> str:
        return "MNIST10"

    def input_shape(self) -> list[int]:
        """get input image shape"""
        return [28, 28, 1]

    def num_category(self) -> int:
        """num of category"""
        return 10
