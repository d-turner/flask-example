'''Auth routes'''
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth_mod = Blueprint('auth', __name__,
                     template_folder='templates/auth')

@auth_mod.route('/auth/register', methods=['GET', 'POST'])
def register():
    '''Register route'''
    try:
        return render_template('signup.html')
    except TemplateNotFound:
        abort(404)


@auth_mod.route('/auth/login', methods=['GET', 'POST'])
def login():
    '''Login route'''
    try:
        return render_template('signin.html')
    except TemplateNotFound:
        abort(404)


@auth_mod.route('/auth/forgot', method=['POST'])
def forgot_password():
    '''Forgot password route'''
    try:
        return render_template('forgot.html')
    except TemplateNotFound:
        abort(404)
