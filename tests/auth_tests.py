'''Setup for application testing'''
import os
import unittest
import tempfile
import sys
sys.path.append('../portfolio')
import portfolio

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, portfolio.app.config['DATABASE'] = tempfile.mkstemp()
        portfolio.app.config['TESTING'] = True
        self.app = portfolio.app.test_client()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(portfolio.app.config['DATABASE'])


    # Route testing 

    def test_register(self):
        response = self.app.get('/auth/register')
        assert b'Hello World!' in response.data

    def test_login(self):
        response = self.app.get('/auth/login')
        assert b'Hello World!' in response.data

    def test_forgot_password(self):
        response = self.app.post('/auth/forgot')
        assert b'Hello World!' in response.data


if __name__ == '__main__':
    unittest.main()
    