'''home routes '''
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# Define the blueprint: 'index', set its url prefix: app.url/
index_mod = Blueprint('index', __name__,
                      template_folder='templates/index')

@index_mod.route('/')
def index():
    try:
        return render_template('index/home.html')
    except TemplateNotFound:
        abort(404)


@index_mod.route('/home')
def home():
    try:
        return render_template('index/home.html')
    except TemplateNotFound:
        abort(404)
