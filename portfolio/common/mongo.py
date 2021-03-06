'''Database setup'''
import pymongo
import portfolio


class Mongo(object):
    URI = 'mongodb://username:password@127.0.0.1:27017/name'
    DATABASE = None

    @staticmethod
    def init():
        client = pymongo.MongoClient(portfolio.app.config['MONGO_DATABASE_URI'])
        Mongo.DATABASE = client[portfolio.app.config['MONGO_DATABASE_NAME']]

    @staticmethod
    def insert(collection, json):
        Mongo.DATABASE[collection].insert(json)

    @staticmethod
    def find(collection, query):
        return Mongo.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Mongo.DATABASE[collection].find_one(query)
