'''Setup for application testing'''
import os
import unittest
import tempfile
import sys
sys.path.append('../portfolio')
from portfolio import app
from portfolio.auth_mod import models
from portfolio.common import database

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        database.Database.init()
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        database.Database.DATABASE.users.drop()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
        database.Database.DATABASE.users.drop()


### User testing ###

    def test_registering_user(self):
        '''Register user'''
        result = models.User.register(
            email='test@test.com',
            password='1234',
            name='Test test')
        self.assertTrue(result, "Failed to register new user")


    def test_register_existing_email(self):
        '''Register multiple users with same email'''
        result1 = models.User.register(
            email='test@test.com',
            password='1234',
            name='Test1 test1')
        result2 = models.User.register(
            email='test@test.com',
            password='5678',
            name='Test2 test2')
        print result1, result2
        assert result1, result2
        self.assertFalse(result2, "Registered user with existing email")


if __name__ == '__main__':
    unittest.main()
    