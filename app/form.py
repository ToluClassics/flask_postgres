from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.fields.html5 import TelField,EmailField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Registration

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    company = StringField('Company', validators = [DataRequired()])
    email = EmailField('Email', validators = [DataRequired(),Email()])
    contact_no = TelField('Contact No.', validators = [DataRequired()])
    submit = SubmitField('Register')
    
    def validate_email(self, email):
        user = Registration.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')