'''Setup for application testing'''
__author__ = 'dturner'

import unittest
import sys
import json
sys.path.append('../portfolio')
from portfolio import app

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()


    def tearDown(self):
        pass


### Route testing ###

    def test_register_get(self):
        response = self.app.get('/auth/register')
        assert b'' in response.data, 'Get request failed'

    def test_register_post(self):
        email = 'test@test.com'
        password = 'pass123'
        response = self.app.post('/auth/register', data=dict(
            email=email, 
            password=password), follow_redirects=True)
        assert response.data, 'Post request failed'

    def test_login(self):
        response = self.app.get('/auth/login')
        assert b'Hello World!' in response.data, 'Login request failed'

    def test_forgot_password(self):
        response = self.app.post('/auth/forgot')
        assert b'Hello World!' in response.data, 'Forgot request failed'


if __name__ == '__main__':
    unittest.main()
    