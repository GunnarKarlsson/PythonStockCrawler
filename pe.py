import pymongo
import pprint
import sys
import argparse

parser = argparse.ArgumentParser(description='Find matches below a certain p/e. Default is 5.0. Example: python pe.py -p 4.0')
parser.add_argument('-p', type=float,help='Max P/E for matching. Example: python pe.py -p 4.2. Default is 5.0.')
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

try:
    pe = float(args.p)
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
