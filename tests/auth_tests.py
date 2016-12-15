'''Setup for application testing'''
__author__ = 'dturner'

import unittest
import sys
sys.path.append('../portfolio')
from portfolio.common.mongo import Mongo
from portfolio import app

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        Mongo.init()
        app.config['TESTING'] = True
        self.app = app.test_client()
        Mongo.DATABASE.users.drop()


    def tearDown(self):
        Mongo.DATABASE.users.drop()


### Route testing ###

    def test_register_get(self):
        response = self.app.get('/auth/register')
        self.assertEqual(response.status_code, 200, 'Failed to get the register page')

    def test_register_post(self):
        email = 'test@test.com'
        password = 'pass123'
        response = self.app.post('/auth/register', data=dict(
            email=email,
            password=password,
            name="Test test"), follow_redirects=False)
        self.assertEqual(response.status_code, 302, 'Register post request failed, no redirect')

    def test_register_post_redirect(self):
        email = 'test@test.com'
        password = 'pass123'
        response = self.app.post('/auth/register', data=dict(
            email=email,
            password=password,
            name="Test test"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, 'Register post request failed, redirect failed')

    def test_register_post_existing(self):
        email = 'test@test.com'
        password = 'pass123'
        response1 = self.app.post('/auth/register', data=dict(
            email=email,
            password=password,
            name="Test test"), follow_redirects=False)
        self.assertEqual(response1.status_code, 302,
                         'First register post request failed, no redirect')
        response2 = self.app.post('/auth/register', data=dict(
            email=email,
            password=password,
            name="Test test"), follow_redirects=False)
        self.assertIn('Email already in use', response2.data,
                      'Error message not in response')

    def test_login_get(self):
        response = self.app.get('/auth/login')
        self.assertEqual(response.status_code, 200, 'Failed to get the login page')

    def test_login_post(self):
        email = 'test@test.com'
        password = 'pass123'
        response = self.app.post('/auth/logon', data=dict(
            email=email,
            password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 201, 'Login post request failed')

    def test_forgot_password(self):
        email = 'test@test.com'
        response = self.app.post('/auth/forgot', data=dict(
            email=email), follow_redirects=True)
        self.assertEqual(response.status_code, 201, 'Forgot password request failed')


if __name__ == '__main__':
    unittest.main()
    