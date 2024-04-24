from catdog_ui import app
from catdog_ui.views.views import login_required
from pathlib import Path
from tlib.graphics import imread_wrapper
import cv2
import os
from flask import (
    render_template,
    make_response,
)

@app.route('/images/<string:category>/<int:id>', methods=["GET"])
@login_required
def get_image(category:str, id:int):
    print(f"@get_image() for /images/{category}/{id}")
    img_store_path = os.environ["TLIB_ML_DATA_DIR"]
    img_path = Path(img_store_path).joinpath(
        "cat_and_dog", "PetImages", category, f"{id}.jpg"
    )
    try:
        img = imread_wrapper(str(img_path))
        _, mat = cv2.imencode(".jpg", img)
        mat_bytes = mat.tobytes()
        resp = make_response(mat_bytes)
        resp.headers.set("Content-Type", "image/jpeg")
        return resp

    except Exception as e:
        return render_template("error/index.html", err_msg = str(e))

