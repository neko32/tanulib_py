from tlib.ml.base import *
import tensorflow as tf
# from os import remove


def main():

    model_name = "catdog"

    preprocessor = InputDataPreprocessor("cat_and_dog/PetImages")
    tr_ds, val_ds = preprocessor.load(
        image_size=PREFERRED_IMG_SIZE_CATDOG,
        batch_size=PREFERRED_BATCH_SIZE_CATDOG,
        label_mode=LabelMode.LABELMODE_INT_FOR_SPARSE_CAT_CROSSENTROPY,
        seed=1337,
        validation_split=0.2
    )
    print(f"tr ds - {tr_ds}, val ds - {val_ds}")
    print(f"tr ds siz - {len(tr_ds)}, val ds siz - {len(val_ds)}")

    da = DataAugumentation()
    da.add_flip()
    da.add_rotation()

    # apply da
    tr_ds = tr_ds.map(
        lambda img, label: (da.apply(img), label),
        num_parallel_calls=tf.data.AUTOTUNE,
    )
    print(f"tr ds (after DA) - {tr_ds}")
    print(f"tr ds siz (after DA) - {len(tr_ds)}")

    tr_ds = tr_ds.prefetch(tf.data.AUTOTUNE)
    val_ds = val_ds.prefetch(tf.data.AUTOTUNE)

    model = make_model_CBA_with_MP_GAP_plus_residual(
        input_shape_without_channel=PREFERRED_IMG_SIZE_CATDOG,
        num_channels=3,
        num_classes=2,
        kernel_size=3,
        residual_kernel_size=1,
        strides=2,
        dropout_at_fc=0.25,
        per_phase_filter=[128, 256, 512, 728, 1024],
        activation_fn='relu',
        normalize_pix=True
    )

    # if exists("./model.png"):
    #    remove("./model.png")
    # keras.utils.plot_model(model, show_shapes = True)

    epochs = 30
    callbacks = [
        model_auto_saver(model_name)
    ]
    adam = keras.optimizers.Adam(learning_rate=3e-4)
    model.compile(
        optimizer=adam,
        loss=keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=[keras.metrics.BinaryAccuracy(name='acc')]
    )
    model.fit(
        tr_ds,
        epochs=epochs,
        validation_data=val_ds,
        callbacks=callbacks
    )


if __name__ == "__main__":
    main()
