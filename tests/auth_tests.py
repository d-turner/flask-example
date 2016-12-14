'''Setup for application testing'''
__author__ = 'dturner'

import unittest
import sys
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
        self.assertEqual(response.status_code, 200, 'Failed to get the register page')

    def test_register_post(self):
        email = 'test@test.com'
        password = 'pass123'
        response = self.app.post('/auth/register', data=dict(
            email=email,
            password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 201, 'Register post request failed')

    def test_login_get(self):
        response = self.app.get('/auth/login')
        self.assertEqual(response.status_code, 200, 'Failed to get the login page')

    def test_login_post(self):
        email = 'test@test.com',
        password = 'pass123'
        response = self.app.post('/auth/logon', data=dict(
            email=email,
            password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 201, 'Login post request failed')

    def test_forgot_password(self):
        email = 'test@test.com',
        response = self.app.post('/auth/forgot', data=dict(
            email=email), follow_redirects=True)
        self.assertEqual(response.status_code, 201, 'Forgot password request failed')


if __name__ == '__main__':
    unittest.main()
    