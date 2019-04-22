import pymongo
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)

pe = 5.0
try:
    arg = sys.argv[1]
    pe = float(arg)
except:
    pe = 5.0

print("Matches for P/E lower than: ", pe,":")

client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.stocks
count = 0;
for x in collection.find({ "P/E": { "$lt": pe }}):
    pp.pprint(str(x['Code'])  + " " + x['Name'] + " P/E: " + str(x['P/E']))
    count = count + 1
print("Count: ", count)
