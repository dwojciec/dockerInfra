import pymongo
from pymongo import MongoClient
# Connection to Mongo DB
try:
    conn=pymongo.MongoClient("mongodb://db01:27017")
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
conn
