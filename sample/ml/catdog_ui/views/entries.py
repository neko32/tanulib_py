from catdog_ui import app, db_conn
from catdog_ui.views.views import login_required
from flask import render_template

@app.route('/')
@login_required
def show_entries():
    rez = db_conn.execute("select * from Prediction")
    fetched_rows = rez.fetchall()
    return render_template("entries/index.html", predict_hist = fetched_rows)
