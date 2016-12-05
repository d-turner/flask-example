'''models auth interacts with'''
__author__ = 'dturner'

from portfolio.common.database import Database
from flask import session
import uuid 

# Define a User model
class User(object):
    '''User model {username, password, pass}'''

    def __init__(self, name, email, password, _id=None):
        self.name = name
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'_id': _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            # need to add in the salt algorithm here
            return user.password == password
        return False


    @staticmethod
    def login(user_email):
        # Login valid 
        session['email'] = user_email


    @staticmethod
    def register(self):
        pass
