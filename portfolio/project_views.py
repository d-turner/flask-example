'''projects routes '''
from portfolio import app
from flask import render_template

@app.route('/projects/')
def projects():
    '''Projects Page'''
    return 'Projects List'

@app.route('/projects/<int:project_id>')
def project(project_id):
    '''Project_id page'''
    return 'Project id : %d' % project_id


@app.route('/template/')
@app.route('/template/<test>')
def template(test=None):
    '''Template'''
    return render_template('template.html', test=test)
    