from catdog_ui import app
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
        return render_template("entries/index.html")