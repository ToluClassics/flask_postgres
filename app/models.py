from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    company = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)