from tlib.nlp.indexer import Indice
from tlib.ml.base import early_stopping
from keras.models import Sequential, Model
from keras.layers import (
    Embedding,
    Flatten,
    Dense,
    Activation,
)
from keras.initializers import random_uniform, glorot_uniform
import numpy as np
import tensorflow as tf
import string
import re


class Word2Vec:
    """
    Perform word2vec model fitting and prediction.
    This is a skip gram with given neighbor size.
    So input to model is each word and output is neighbor size * 2
    (before the word and after the word)
    """

    def __init__(
            self,
            input_path: str,
            neighbor_size: int = 5):

        self.indice = Indice(input_path, 0, neighbor_size, verbose=True)
        print(self.indice.summary())
        print(self.indice.x_train.shape)
        print(self.indice.y_train.shape)
        self.input_dim = self.indice.words_len
        self.output_dim = neighbor_size * 2
        print(self.output_dim)
        self.neighbor_size = neighbor_size

    def build_model(self) -> None:
        """Build a model with skipgram"""
        m: Model = Sequential()
        m.add(
            Embedding(
                self.input_dim,
                self.output_dim,
                input_length=1,
                embeddings_initializer=random_uniform(seed=20170719)
            )
        )
        m.add(Flatten())
        # m.add(Dense(self.input_dim))
        # m.add(Dense(units = self.output_dim, kernel_initializer=glorot_uniform(seed=20170719)))
        m.add(
            Dense(
                units=self.input_dim,
                use_bias=False,
                kernel_initializer=glorot_uniform(seed=20170719)
            )
        )
        m.add(Activation("softmax"))

        self.model = m
        self.model.compile(
            optimizer='RMSprop',
            loss='categorical_crossentropy',
            metrics=['categorical_accuracy']
        )
        self.model.summary()

    def fit(self, batch_size: int = 200, epochs=10) -> None:

        # TODO - one hot for y_train
        r = self.indice.y_train.shape[0]
        y_train_oh = np.zeros((r, self.input_dim), dtype='int8')
        for i in range(r):
            for j in range(0, self.neighbor_size * 2):
                y_train_oh[i, self.indice.y_train[i, j]] = 1

        x_train = self.indice.x_train.reshape(r, 1)
        es = early_stopping(monitor="categorical_accuracy", patience=1)
        self.model.fit(
            x_train,
            y_train_oh,
            batch_size=batch_size,
            epochs=epochs,
            shuffle=True,
            callbacks=[es],
            validation_split=0.0
        )


def standardize_strinput_remove_html_tags(input_data):
    """Standardize input by removing HTML tags"""
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, '<br[ ]*/>', ' ')
    return tf.strings.regex_replace(
        stripped_html,
        '[%s]' % re.escape(string.punctuation),
        ''
    )
