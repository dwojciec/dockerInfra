import pymongo
from pymongo import MongoClient
# Connection to Mongo DB
try:
    conn=pymongo.MongoClient("mongodb://reloca3:reloca123@db:27017/relocaDB")
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 

conn
db=conn
print db
db.users.find()
