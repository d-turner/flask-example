'''Register form'''
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Required


class LoginForm(FlaskForm):
    email = TextField('Email Address', [
        Email(),
        Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
        Required(message='Must provide a password.')])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(FlaskForm):
    email = EmailField('Email Address', [DataRequired(), Email()])
    password = PasswordField('Password', [
        Required(message='Must provide a password.')])
