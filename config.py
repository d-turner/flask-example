'''Configuration file for application, imported in __init__,
 Only values in uppercase are actually stored in the config object
 This file should be hidden from the github project'''

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = True

# Secret key for signing cookies
SECRET_KEY = '\x07YH\xea\x93hr\xa0\xf3r\x9b4e\xa0\xce\x1a?\xe2<\xf5\xb77\x91Q'

# Use a secure, unique and absolutely secret key for
# signing the data. 
##CSRF_SESSION_KEY = "secret"

# Define the database - we are working with
# MongoDB for this project
MONGO_DATABASE_URI = 'mongodb://dturner:password@192.168.1.17:27017/test'
MONGO_DATABASE_NAME = 'test'
##DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
##THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
##CSRF_ENABLED     = True