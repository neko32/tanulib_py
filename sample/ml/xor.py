from tlib.ml.base import make_model_with_scalar_input_single_hidden_fc
from keras.optimizers import SGD
import numpy as np


def main():
    m = make_model_with_scalar_input_single_hidden_fc(
        input_shape=[2,],
        num_neurons_in_hidden_layer=2,
        num_output=1
    )
    op = SGD(learning_rate=1.0)
    m.compile(optimizer=op, loss='binary_crossentropy')
    m.summary()

    d = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    r = np.array([[0], [1], [1], [0]])

    hist = m.fit(d, r, batch_size=4, epochs=4000)
    print(f"loss: {hist.history['loss'][-1]}")
    rez = m.predict(d)
    print(rez)
    print((rez >= 0.5).astype(np.int32))


if __name__ == "__main__":
    main()
