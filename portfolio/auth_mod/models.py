'''models auth interacts with'''
__author__ = 'dturner'

# Define a User model
class User(object):
    '''User model {username, password, pass}'''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def get_by_email(self):
        pass

    def get_by_id(self):
        pass

    def login_valid(self):
        pass

    def register(self):
        pass

    def login(self):
        pass
