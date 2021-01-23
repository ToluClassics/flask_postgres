from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Registration

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    company = StringField('Company', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(),Email()])
    submit = SubmitField('Register')
    
    def validate_email(self, email):
        user = Registration.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')