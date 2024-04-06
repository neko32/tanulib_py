from catdog_ui import app
from flask import (
    render_template, 
    request, 
    redirect,
    session,
    flash,
    url_for
)


@app.route("/healthcheck")
def show_healthcheck():
    return render_template("healthcheck/index.html")


@app.route("/login", methods=["GET", "POST"])
def show_login():

    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("wrong user name.")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("wrong password.")
        else:
            session['logged_in'] = True
            flash("successfully logged in.")
            return redirect(url_for('show_entries'))
    return render_template("login/index.html")
        

@app.route("/logout")
def show_logout():
    session.pop('logged_in', None)
    flash('logged out.')
    return redirect(url_for('show_entries'))
