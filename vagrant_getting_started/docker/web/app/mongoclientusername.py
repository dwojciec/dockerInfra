import pymongo
from pymongo import MongoClient
from datetime import datetime

# Connection to Mongo DB
def mongodb_conn():
 try:
#    conn=MongoClient("mongodb://reloca:reloca123@db01:27017/relocaDB")
    conn=MongoClient("mongodb://db01:27017")
    print "Connected successfully!!!"
 except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
 return conn

conn1=mongodb_conn()
my_db=conn1.relocaDB

print my_db
print "hello"
result = my_db.restaurants.insert(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704621"
    }
)

