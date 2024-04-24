from catdog_ui import app, model, db_conn
from catdog_ui.views.views import login_required
from tlib.ml.base import *
from tlib.ml.img import *
from tlib.math import sigmoid
from tlib.sql import insert_to_table
from tlib.dateutil import cur_datetime_as_std_fmt_str
from typing import Tuple
from flask import (
    render_template, 
    redirect,
    url_for,
    request,
)

@app.route('/predict')
@login_required
def show_predict():
    return render_template("predict/index.html")

@app.route('/precict_model', methods = ['POST'])
@login_required
def predict_model():
    model_name = request.form["ModelName"]
    category_name = request.form["Category"]
    image_name = request.form["ImageName"]
    if not image_name.endswith(".jpg"):
        image_name += ".jpg"

    print(f"model_name:{model_name},image_name:{image_name}")
    try:
        cat_per, dog_per = predict(model_name, category_name, image_name)
    except Exception as e:
        print(e)
        # TODO return error page
    print(f"cat_per:{cat_per}%, dog_per:{dog_per}")
    return redirect(url_for('show_entries'))


def predict(model_name:str, category_name:str, image_name:str) -> Tuple[str, str]:
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
    result_str = f"{100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog"
    cur_datestr = cur_datetime_as_std_fmt_str()

    print(f"score - {score}, raw score - {raw_score}")
    print(result_str)

    ins_rez = insert_to_table(
        conn = db_conn,
        table_name = "Prediction",
        col_names = ["input_name", "model_name", "result_summary", "result_path", "created_at"],
        recs = [[image_name, "catdog", result_str, None, cur_datestr]]
    )
    if not ins_rez:
        raise Exception("inserting prediction result failed")

    return (cat_per, dog_per)