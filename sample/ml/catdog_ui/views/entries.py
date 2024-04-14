from catdog_ui import app, db_conn
from flask import (
    render_template, 
    redirect,
    session,
    url_for
)

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('show_login'))
    else:

        rez = db_conn.execute("select * from Prediction")
        fetched_rows = rez.fetchall()
        return render_template("entries/index.html", predict_hist = fetched_rows)
