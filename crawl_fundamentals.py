import pymongo
import urllib
import requests
from bs4 import BeautifulSoup
import datetime
import time
import re
from random import randint
#import pprint
from pprint import pprint

#pp = pprint.PrettyPrinter(indent=4)

def save_details(stockCode, soup, collection):
        ts = time.time()
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        dict = {}
        dict.update({"time":t})

        find_elements(stockCode, "Closing Date","Closing Date")

        ratios = [  "Current Ratio (X)","Quick Ratio (X)","Long Term Debt/Equity (%)"]

        for ratio in ratios:
            try:
                find_elements(stockCode, "\r"+ratio+"\r",ratio)
            except:
                pass

        cursor = collection.find({"Code":stockCode})
        for document in cursor:
            pprint(document)

def find_elements(stockCode, name, label):
    t = soup.find("td", text=name);
    print("label: ", label)
    t = t.find_next_siblings("td")
    datalist = []
    for n in t:
        datalist.append(n.text)
        #print(n.text)
    #save t list with label as key
    collection.update_one( {"Code":stockCode} , {"$set": {label:datalist} } )



start = 1
end = 9999
#client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
client = pymongo.MongoClient("mongodb://localhost:27017/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.stocks

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
headers = {
    'User-Agent': USER_AGENT
}
for stockCode in range(start, end+1):
    time.sleep(randint(2, 7))
    url = "http://www.aastocks.com/en/stocks/analysis/company-fundamental/financial-ratios?symbol={}".format(stockCode)
    page = requests.get(
        url,
        headers=headers
    )
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        print("starting parse for ", stockCode)
        save_details(stockCode, soup, collection)
    except Exception as e:
        print("exception parsing", stockCode, e)
        pass
