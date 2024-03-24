import os
from pathlib import Path
from tlib.ml import load_dataset_from_npz, make_model_with_scalar_input_single_hidden_fc
import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from keras.utils import to_categorical
from keras.models import Model
from keras.optimizers import Adam

def main():
    datapath = Path(os.environ["TLIB_ML_DATA_DIR"]).joinpath("MNIST10", "mnist.npz")
    ((x_train, y_train), (x_val, y_val)) = _prep_data(str(datapath))

    m:Model = make_model_with_scalar_input_single_hidden_fc(
        input_shape = [28 * 28,],
        num_neurons_in_hidden_layer=256,
        num_output=10,
        hidden_layer_activation='relu',
        output_layer_activiation='softmax'
    )
    opt = Adam()
    m.compile(optimizer = opt, loss = "categorical_crossentropy", metrics = ["accuracy"])
    m.summary()

    m.fit(x_train, y_train, batch_size = 128, validation_split=0.2, epochs = 30)
    score = m.evaluate(x_val, y_val)
    print(score)
    


def _prep_data(datapath:str) -> Tuple[Tuple[NDArray, NDArray], Tuple[NDArray, NDArray]]:
    d = load_dataset_from_npz(str(datapath))
    #for k, d in d.items():
    #    print(f"{k}:{d}")

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

    return ((x_train, y_train), (x_test, y_test))

if __name__ == "__main__":
    main()
