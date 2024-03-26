from catdog_ui import app
from flask import render_template, request, redirect


@app.route('/')
def show_entries():
    return render_template("entries/index.html")


@app.route("/healthcheck")
def show_healthcheck():
    return render_template("healthcheck/index.html")


@app.route("/login", methods=["GET", "POST"])
def show_login():

    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            print("wrong user name")
        elif request.form["password"] != app.config["PASSWORD"]:
            print("wrong password")
        else:
            return redirect("/")
    return render_template("login/index.html")
        

@app.route("/logout")
def show_logout():
    return redirect("/")
