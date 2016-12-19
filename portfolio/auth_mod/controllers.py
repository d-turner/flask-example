'''Authentication and Session routes'''
from flask import Blueprint, abort, redirect, render_template, request, url_for
from jinja2 import TemplateNotFound

import portfolio.constants as constants
from portfolio.auth_mod.forms import LoginForm, RegisterForm
from portfolio.auth_mod.models import User

auth_mod = Blueprint('auth', __name__,
                     template_folder='templates/auth')

@auth_mod.route('/auth/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        if register_form.validate_on_submit():
            email = request.form['email']
            password = request.form['password']
            if User.register_user(email, password):
                return redirect(url_for('index.home'))
        return render_template(
            'auth/register.html', form=register_form,
            error=constants.EMAIL_IN_USE_ERROR)
    return render_template('auth/register.html', form=register_form)


@auth_mod.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        try:
            return render_template('auth/login.html')
        except TemplateNotFound:
            abort(404)
    else:
        raise NotImplementedError('Implement login POST')


@auth_mod.route('/auth/forgot', methods=['POST'])
def forgot_password():
    try:
        #return render_template('auth/forgot.html')
        raise NotImplementedError('Implement forgot POST')
    except TemplateNotFound:
        abort(404)
