import pymongo
import urllib
import requests
from bs4 import BeautifulSoup
import datetime
import time
import re
#import pprint

#pp = pprint.PrettyPrinter(indent=4)

def save_details(soup, collection):
        ts = time.time()
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        dict = {}
        dict.update({"time":t})

        find_elements("Closing Date")
        try:
            r = soup.find_all(text=re.compile("Current Ratio(.*)"));
            print(r);
        except:
            pass

        try:
            find_elements("\rCurrent Ratio (X)\r")
        except:
            pass

        #r = soup.find_all(text=re.compile("Current Ratio(.*)"));
        #print(r);

def find_elements(name):
    t = soup.find("td", text=name);
    print("t: ", t)
    t = t.find_next_siblings("td")
    #print("name: ", t)
    for n in t:
        print(n.text)

start = 1
end = 10
#client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
client = pymongo.MongoClient("mongodb://localhost:27017/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.fundamentals

for stockCode in range(start, end+1):
    url = "http://www.aastocks.com/en/stocks/analysis/company-fundamental/financial-ratios?symbol={}".format(stockCode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    save_details(soup, collection)
