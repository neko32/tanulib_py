import os
from os import mkdir
from os.path import exists
from pathlib import Path
from tlib.ml.dataset import load_text_dataset
from tlib.ml.base import (
    make_model_VE_2FC_GAP_2FC,
    generate_weight_vocab_files_as_tsv
)
import tensorflow as tf
from tf_keras.layers import TextVectorization
from tf_keras.metrics import BinaryAccuracy
from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.optimizers import Adam
from keras.losses import BinaryCrossentropy
import re
import string
import shutil


def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
    return tf.strings.regex_replace(
        stripped_html,
        '[%s]' % re.escape(string.punctuation),
        ''
    )


def main():

    model_store_loc = os.path.join(
        os.environ["TANUAPP_ML_DIR"], "word_embedding")
    if not exists(model_store_loc):
        mkdir(model_store_loc)

    tmp_dir = os.environ["HOME_TMP_DIR"]
    log_path = Path(tmp_dir).joinpath("word_embedding")
    if log_path.exists():
        shutil.rmtree(str(log_path))

    dataset_name = "imdb"
    category = str(Path("aclImdb").joinpath("train"))

    train_ds, val_ds = load_text_dataset(
        dataset_name=dataset_name,
        category=category,
        to_remove_dirs=["unsup"]
    )

    # just show a bit of data..
    for text_batch, label_batch in train_ds.take(1):
        for i in range(5):
            # print(text_batch.numpy().shape)
            # print(label_batch)
            print(label_batch[i].numpy(), text_batch.numpy()[i])

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    train_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    vocab_size = 10000
    seq_len = 100

    vec_layer = TextVectorization(
        standardize=custom_standardization,
        max_tokens=vocab_size,
        output_mode='int',
        output_sequence_length=seq_len
    )

    # prep text-only (no label) dataset to build vocabulary
    text_ds = train_ds.map(lambda x, _: x)
    vec_layer.adapt(text_ds)

    model = make_model_VE_2FC_GAP_2FC(
        tv=vec_layer,
        vocab_size=vocab_size,
        embedding_dim=16
    )
    tb_callback = TensorBoard(log_dir=str(log_path))
    model_checkpoint = ModelCheckpoint(model_store_loc)

    model.compile(
        optimizer=Adam(),
        loss=BinaryCrossentropy(from_logits=True),
        metrics=BinaryAccuracy(threshold=0.0)
    )

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=15,
        callbacks=[tb_callback, model_checkpoint]
    )

    model.summary()

    print("### NEXT STEP is to generate vectors & metadata.tsv..")
    generate_weight_vocab_files_as_tsv(
        model=model,
        vec_layer=vec_layer,
        emb_layer_name="emb",
        file_loc=model_store_loc
    )

    print("all done.")


if __name__ == "__main__":
    main()
