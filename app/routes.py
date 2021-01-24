from app import app,db
from app.form import RegistrationForm
from app.models import Registration
from flask import render_template,flash, redirect, url_for


@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit(): 
        regForm = Registration(username=form.username.data,email=form.email.data,\
                                    first_name=form.first_name.data,last_name=form.last_name.data,\
                                    company=form.company.data,contact_no=form.contact_no.data)
        db.session.add(regForm)
        db.session.commit()
        flash('Successfully submitted your user')
        return redirect(render_template('home.html'))
    return render_template('home.html',form=form)