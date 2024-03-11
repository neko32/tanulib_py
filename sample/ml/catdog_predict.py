from tlib.ml.base import *
from tlib.ml.img import *
from tlib.math import sigmoid
from os.path import exists
from keras.models import load_model


def main():
    model_store_loc = os.path.join(os.environ["TANUAPP_ML_DIR"], "catdog")
    if not exists(model_store_loc):
        raise Exception("model dir doesn't exist")

    model: keras.Model = load_model(model_store_loc)
    model.summary()
    img_siz = PREFERRED_IMG_SIZE_CATDOG

    img = load_img_as_1d(
        dataset_name="cat_and_dog/PetImages",
        category="Cat",
        file_name="6779.jpg",
        size=img_siz
    )

    pred = model.predict(img)
    print(pred)
    raw_score = float(pred[0][0])
    score = sigmoid(raw_score)
    print(f"score - {score}, raw score - {raw_score}")
    print(f"{100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog")


if __name__ == "__main__":
    main()
