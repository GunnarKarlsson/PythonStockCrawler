import pymongo
import pprint
import sys
import argparse

parser = argparse.ArgumentParser(description='Find data for a certain code.  Example: python code.py -c 999')
parser.add_argument('-c', type=float,help='Company code')
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

code = 0
try:
    code = int(args.c)
except:
    print("Invalid code")
    quit()

client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.stocks
count = 0;
for x in collection.find({ "Code": code }):
    pp.pprint(x)
