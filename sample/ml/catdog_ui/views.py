from catdog_ui import app
from flask import render_template

@app.route('/')
def show_entries():
    return render_template("healthcheck/index.html")

