from catdog_ui import app
from flask import render_template

@app.route("/healthcheck")
def show_healthcheck():
    return render_template("healthcheck/index.html")
