'''Database setup'''
import pymongo
from portfolio import app


class Mongo(object):
    URI = 'mongodb://username:password@127.0.0.1:27017/name'
    DATABASE = None

    @staticmethod
    def init():
        '''Setup the mongo database'''
        client = pymongo.MongoClient(app.config['MONGO_DATABASE_URI'])
        Mongo.DATABASE = client[app.config['MONGO_DATABASE_NAME']]

    @staticmethod
    def insert(collection, json):
        Mongo.DATABASE[collection].insert(json)

    @staticmethod
    def find(collection, query):
        return Mongo.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Mongo.DATABASE[collection].find_one(query)
