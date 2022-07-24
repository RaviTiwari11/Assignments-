import urllib

import pymongo
client = pymongo.MongoClient("mongodb+srv://test:"+urllib.parse.quote_plus("Ravi@123")+"@cluster0.c7asp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"ravi",
    "email":"ravt6688",
    "last_name":"tiwari"
}

db1=client['mongo_db']
coll=db1['test']
coll.insert_one(d)