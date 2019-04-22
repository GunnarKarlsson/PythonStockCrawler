#See: https://docs.mongodb.com/v3.2/reference/method/db.collection.deleteMany/#db.collection.deleteMany
import pymongo

client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.stocks
result = collection.delete_many({}) #delete all
print("deleted all: ",result.acknowledged)
