from catdog_ui import app
from tlib.ml.base import *
from tlib.ml.img import *
from tlib.math import sigmoid
from os.path import exists
from keras.models import load_model
from typing import Tuple




from flask import (
    render_template, 
    redirect,
    session,
    url_for,
    request,
)

@app.route('/predict')
def show_predict():
    if not session.get('logged_in'):
        return redirect(url_for('show_login'))
    else:
        return render_template("predict/index.html")

@app.route('/precict_model', methods = ['POST'])
def predict_model():
    if not session.get('logged_in'):
        return redirect(url_for('show_login'))
    else:
        model_name = request.form["ModelName"]
        category_name = request.form["Category"]
        image_name = request.form["ImageName"]
        print(f"model_name:{model_name},image_name:{image_name}")
        cat_per, dog_per = predict(model_name, category_name, image_name)
        print(f"cat_per:{cat_per}%, dog_per:{dog_per}")
        return redirect(url_for('show_entries'))


def predict(model_name:str, category_name:str, image_name:str) -> Tuple[str, str]:
    model_store_loc = os.path.join(os.environ["TANUAPP_ML_DIR"], model_name)
    if not exists(model_store_loc):
        raise Exception("model dir doesn't exist")

    model: keras.Model = load_model(model_store_loc)
    model.summary()
    img_siz = PREFERRED_IMG_SIZE_CATDOG

    img = load_img_as_1d(
        dataset_name="cat_and_dog/PetImages",
        category=category_name,
        file_name=image_name,
        size=img_siz
    )

    pred = model.predict(img)
    print(pred)
    raw_score = float(pred[0][0])
    score = sigmoid(raw_score)
    cat_per = f"{100 * (1 - score):.2f}"
    dog_per = f"{100 * score:.2f}% dog"
    print(f"score - {score}, raw score - {raw_score}")
    print(f"{100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog")

    return (cat_per, dog_per)