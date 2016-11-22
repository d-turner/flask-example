'''home routes '''
from portfolio import app
from flask import render_template

@app.route('/')
def index():
    '''Index route'''
    return 'Index page'


@app.route('/home')
def home():
    '''Home route'''
    #return 'Home page'
    return render_template('template.html')
