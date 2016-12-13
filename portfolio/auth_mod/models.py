'''models auth interacts with'''
__author__ = 'dturner'

import uuid
from portfolio.common.mongo import Mongo
from flask import session

# Define a User model
class User(object):
    '''User model {email, password, name, _id}'''

    def __init__(self, email, password, name=None, _id=None):
        self.name = name
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    @classmethod
    def get_by_email(cls, email):
        data = Mongo.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)


    @classmethod
    def get_by_id(cls, _id):
        data = Mongo.find_one('users', {'_id': _id})
        if data is not None:
            return cls(**data)


    @staticmethod
    def validate_login(email, password):
        '''Check whether a user's email and password are correct'''
        user = User.get_by_email(email)
        if user is not None:
            # need to add in the salt algorithm here
            return user.password == password
        return False


    @staticmethod
    def login(email, password):
        '''Attempt to login a user'''
        if User.validate_login(email, password) is True:
            session['email'] = email
        else:
            # do something else
            session['email'] = None


    @staticmethod
    def logout():
        session['email'] = None


    @classmethod
    def register(cls, email, password, name=None):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password, name)
            new_user.save_to_mongo()
            # need to redirect to login page
            return True
        else:
            return False


    def json(self):
        return {'name' : self.name,
                'password' : self.password,
                'email' : self.email,
                '_id' : self._id}


    @classmethod
    def from_mongo(cls, _id):
        user = Mongo.find_one(collection='users',
                              query={'_id': _id})
        # cls(** object) is the same as
        # name=user['name'],
        # password=user['password'],
        # email=user['email'],
        # _id=user['_id']
        return cls(**user)


    def save_to_mongo(self):
        Mongo.insert(collection='users',
                     json=self.json())
