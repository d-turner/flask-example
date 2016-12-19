'''Setup for application testing'''
__author__ = 'dturner'

import sys
import unittest

sys.path.append('../portfolio')

from flask import session

from portfolio import app
from portfolio.auth_mod import models
from portfolio.common.mongo import Mongo

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        Mongo.init()
        app.config['TESTING'] = True
        self.app = app.test_client()
        Mongo.DATABASE.users.drop()


    def tearDown(self):
        Mongo.DATABASE.users.drop()


### User testing ###

    def test_registering_user(self):
        '''Register user'''
        result = models.User.register_user(
            email='test@test.com',
            password='1234',
            name='Test test')
        self.assertTrue(result, "Failed to register new user")


    def test_register_existing_email(self):
        '''Register multiple users with same email'''
        result1 = models.User.register_user(
            email='test@test.com',
            password='1234',
            name='Test1 test1')
        self.assertTrue(result1, "Could not register first user")
        result2 = models.User.register_user(
            email='test@test.com',
            password='5678',
            name='Test2 test2')
        self.assertNotEqual(result1, result2, "Registered user with existing email")
        self.assertFalse(result2, "Registered user with existing email")

    def test_login_existing_user(self):
        '''Register user and attempt to login that user'''
        with app.test_request_context():
            result1 = models.User.register_user(
                email='test@test.com',
                password='1234',
                name='Test test')
            self.assertTrue(result1, 'Could not register user')
            models.User.login_user(
                email='test@test.com',
                password='1234')
            self.assertEqual(session['email'], 'test@test.com', 'Failed to add user to the session')

    def test_login_non_user(self):
        '''Attempt to login non-registered user'''
        with app.test_request_context():
            models.User.login_user(
                email='test@test.com',
                password='1234')
            self.assertEqual(session['email'], None, 'User was added to the session')

    def test_login_bad_password(self):
        '''Register user and attempt to login that user'''
        with app.test_request_context():
            result1 = models.User.register_user(
                email='test@test.com',
                password='1234',
                name='Test test')
            self.assertTrue(result1, 'Could not register initial user')
            models.User.login_user(
                email='test@test.com',
                password='12345')
            self.assertEqual(session['email'], None, 'User was added to the session')

if __name__ == '__main__':
    unittest.main()
