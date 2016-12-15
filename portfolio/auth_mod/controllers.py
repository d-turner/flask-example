'''Auth routes'''
import portfolio.constants as constants
from flask import Blueprint, render_template, request, abort, url_for, redirect
from jinja2 import TemplateNotFound
from portfolio.auth_mod.models import User

auth_mod = Blueprint('auth', __name__,
                     template_folder='templates/auth')

@auth_mod.route('/auth/register', methods=['GET', 'POST'])
def register():
    '''Register route'''
    if request.method == 'GET':
        return render_template('auth/signup.html')
    else:
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        if User.register(email, password, name):
            return redirect(url_for('auth.login'))
        return render_template(
            'auth/signup.html',
            error=constants.EMAIL_IN_USE_ERROR)


@auth_mod.route('/auth/login', methods=['GET', 'POST'])
def login():
    '''Login route'''
    if request.method == 'GET':
        try:
            return render_template('auth/signin.html')
        except TemplateNotFound:
            abort(404)
    else:
        raise NotImplementedError('Implement login POST')


@auth_mod.route('/auth/forgot', methods=['POST'])
def forgot_password():
    '''Forgot password route'''
    try:
        return render_template('auth/forgot.html')
    except TemplateNotFound:
        abort(404)
