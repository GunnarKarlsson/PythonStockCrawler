import pymongo
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)

lower_than = 0.3
try:
    arg = sys.argv[1]
    lower_than = float(arg)
except:
    lower_than = 0.3

print("Matches for P/B lower than: ", lower_than,":")

client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.stocks
count = 0;
for x in collection.find({ "P/B": { "$lt": lower_than }}):
    pp.pprint(str(x['Code'])  + " " + x['Name'] + " P/B: " + str(x['P/B']))
    count = count + 1
print("Count: ", count)
