'''Database setup'''
import pymongo
import portfolio


class Database(object):
    URI = 'mongodb://dturner:password@192.168.1.17:27017/test' # replace with raspi
    DATABASE = None

    @staticmethod
    def init():
        '''Setup the mongo database'''
        client = pymongo.MongoClient(portfolio.app.config['MONGO_DATABASE_URI'])
        Database.DATABASE = client[portfolio.app.config['MONGO_DATABASE_NAME']]

    @staticmethod
    def insert(collection, json):
        Database.DATABASE[collection].insert(json)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
