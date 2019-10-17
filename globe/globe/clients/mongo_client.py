import json, os, sys
import pprint

from pymongo import MongoClient


class MongoDB:
    """
    we need to create a single persistent connection to database.

    Everytime a client calls us, we can simply return the connection instead of creating
    it again and again.
    """
    def __init__(self):
        self.db = MongoClient("mongodb://localhost:27017/")
    
    def get_database(self):
        return self.db

    def get_client(self, db_name):
        return self.db[db_name]


M = MongoDB()
client = M.get_client('scraped')
#collection = client[sys.argv[1]]

#cursor = collection.find({})
#for document in cursor:
#    print(document)