'''Database setup'''
import pymongo


class Database(object):
    URI = 'mongodb://127.0.0.1:27017' # replace with raspi
    DATABASE = None

    @staticmethod
    def init():
        '''Setup the mongo database'''
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, json):
        Database.DATABASE[collection].insert(json)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
