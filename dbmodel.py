from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30),  nullable=False)
    lastname = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Store hashed password, make sure it's long enough

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return self.active


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True)
    isbn = db.Column(db.String(11), unique=True)
    year = db.Column(db.String(4),)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number1 = db.Column(db.String(15), unique=True)
    phone_number2 = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(200),)


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), unique=True)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    