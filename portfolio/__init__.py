''' Flask controller'''
from flask import Flask

app = Flask(__name__)
import portfolio.home_views
import portfolio.project_views

if __name__ == '__main__':
    app.secret_key = '\x07YH\xea\x93hr\xa0\xf3r\x9b4e\xa0\xce\x1a?\xe2<\xf5\xb77\x91Q'
    app.run()
    