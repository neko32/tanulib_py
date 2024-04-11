from catdog_ui import app
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
        image_name = request.form["ImageName"]
        print(f"model_name:{model_name},image_name:{image_name}")
        return redirect(url_for('show_entries'))
