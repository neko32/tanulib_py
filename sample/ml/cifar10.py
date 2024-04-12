from tlib.ml.dataset import cifar_pickle_load
from tlib.ml.base import make_model_CAMDCAMD_2FC_F_2FC
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
import os
from os import mkdir
from os.path import exists


def main():

    model_store_loc = os.path.join(os.environ["TANUAPP_ML_DIR"], "cifar10")
    if not exists(model_store_loc):
        mkdir(model_store_loc)

    (tr_x, tr_y), (val_x, val_y) = cifar_pickle_load(
        "CIFAR10", "cifar-10-batches-py")
    tr_x = tr_x.astype('float32')
    tr_x = tr_x / 255.
    val_x = val_x.astype('float32')
    val_x = val_x / 255.

    print(tr_y.size)
    tr_y = to_categorical(tr_y, 10)
    val_y = to_categorical(val_y, 10)

    m = make_model_CAMDCAMD_2FC_F_2FC(
        input_shape=[32, 32, 3]
    )
    m.summary()

    adam = Adam(learning_rate=0.001)
    m.compile(
        optimizer=adam, 
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    red = ReduceLROnPlateau(
        monitor='val_accuracy',
        factor=0.5,
        patience=5,
        mode='max',
        min_lr=0.0001
    )
    chkpt = ModelCheckpoint(model_store_loc)

    batch_size = 512
    epochs = 50

    m.fit(
        tr_x,
        tr_y,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.2,
        shuffle=True,
        callbacks=[red, chkpt]
    )

    r = m.evaluate(val_x, val_y)
    print(r)


if __name__ == "__main__":
    main()
