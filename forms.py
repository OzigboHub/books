from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from dbmodel import User


class Register(FlaskForm):

    def validate_firstname(self, firstname_to_check):
        firstname = User.query.filter_by(firstname=firstname_to_check.data).first()
        if firstname:
            raise ValidationError('User already exists! please try a different username.')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists! try a different email.')

    firstname = StringField(label="FirstName", validators=[Length(min=3, max=15), DataRequired()])
    lastname = StringField(label="LastName", validators=[Length(min=3, max=15), DataRequired()])
    username = StringField(label="Username", validators=[Length(min=4, max=10), DataRequired()])
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=5), DataRequired()])
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")


class Login(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')
