from catdog_ui import app
from flask import render_template

@app.route('/')
def show_entries():
    return render_template("entries/index.html")

@app.route("/healthcheck")
def show_healthcheck():
    return render_template("healthcheck/index.html")

@app.route("/login")
def show_login():
    return render_template("login/index.html")

