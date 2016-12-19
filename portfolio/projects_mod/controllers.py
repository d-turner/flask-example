'''projects routes '''
from portfolio import app
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

@app.route('/projects/')
def projects():
    return 'Projects List'

@app.route('/projects/<int:project_id>')
def project(project_id):
    return 'Project id : %d' % project_id


@app.route('/template/')
@app.route('/template/<test>')
def template(test=None):
    return render_template('template.html', test=test)
    