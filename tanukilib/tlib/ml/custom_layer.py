import tensorflow as tf
from tf_keras import layers, regularizers, backend


class ArcFaceLayer(layers.Layer):
    """Arc Face Layer"""

    def __init__(
            self,
            n_classes: int = 10,
            scale: int = 30.,
            margin: float = 0.50,
            regularizer=None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.n_classes = n_classes
        self.scale = scale
        self.margin = margin
        self.regularlizer = regularizers.get(regularizer)

    def build(self, input_shape):
        """Build the arc face layer"""
        super().build(input_shape[0])
        self.W = self.add_weight(
            name='W',
            shape=(input_shape[0][-1], self.n_classes),
            initializer='glorot_uniform',
            trainable=True,
            regularizer=self.regularlizer
        )

    def call(self, inputs):
        """defines actual behavior of the arc face layer"""
        x, y = inputs
        x = tf.nn.l2_normalize(x, axis=1)
        W = tf.nn.l2_normalize(self.W, axis=0)
        # cosine sim
        logits = x @ W
        # epsilon gives very tiny floating number
        # value range should be -1 < x < 1
        clipped_logits = backend.clip(
            logits,
            -1. + backend.epsilon(),
            1. - backend.epsilon()
        )
        theta = tf.acos(clipped_logits)
        target_logits = tf.cos(theta + self.margin)
        # y is one-hot vector, only truth label with 1 uses target_logits
        # else (0) uses logits as is
        logits = logits * (1 - y) + target_logits * y
        # to avoid too small num, scale up by scaler
        logits *= self.scale
        return tf.nn.softmax(logits)

    def compute_output_shape(self, _):
        return (None, self.n_classes)
