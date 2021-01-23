from app import app
from app.form import RegistrationForm
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    form = RegistrationForm()
    return render_template('index.html',form=form)