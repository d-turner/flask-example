''' Flask controller'''
from flask import Flask, render_template

# Import a module / component using its Blueprint handler variable (index_mod)
from portfolio.index_mod.controllers import index_mod as index_module

app = Flask(__name__)

# External configuration file
app.config.from_object('config')

## setup db here

# Register Blueprints
app.register_blueprint(index_module)
## pass

# setup 404 handler
@app.errorhandler(404)
def not_found(error):
    '''Doc String'''
    error_str = str(error.code) + " : Sorry will be up shortly"
    return render_template('404.html', error=error_str), 404


if __name__ == '__main__':
    app.secret_key = '\x07YH\xea\x93hr\xa0\xf3r\x9b4e\xa0\xce\x1a?\xe2<\xf5\xb77\x91Q'
    app.run()
    