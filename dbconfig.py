from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dbdata import *
uri = 'mongodb://localhost:27017/'

client = MongoClient(uri,server_api=ServerApi('1'))


db = client[DB_NAME]

collections = {collection: db[collection] for collection in COLLECTIONS}


