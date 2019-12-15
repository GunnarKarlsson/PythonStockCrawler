import pymongo
import urllib
import requests
from bs4 import BeautifulSoup
import datetime
import time
from random import randint

def save_details(soup, collection, keyword, stockCode):
    bizSummary = soup.find_all("td",class_="mcFont")[11]
    bizSummary = bizSummary.text.strip()
    print(bizSummary)
    print(keyword)
    if keyword in bizSummary:
        print("keyword found")
        dict = {}
        ts = time.time()
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        dict.update({"time":t})
        dict.update({"profile":bizSummary})
        dict.update({"keywordCount":bizSummary.count(keyword)})
        dict.update({"stockCode":stockCode})
        dict.update({"keyword":keyword})
        collection.insert_one(dict)
        print("inserted into collection")
    else:
        print("keyword is not found")

keyword = "Macau";
startCode = 1
endCode = 9999

client = pymongo.MongoClient("mongodb://localhost:27017/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.macau

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
headers = {
    'User-Agent': USER_AGENT
}

for stockCode in range(startCode, endCode+1):
    time.sleep(randint(1, 3))
    url = "http://www.aastocks.com/en/stocks/analysis/company-fundamental/?symbol={0}".format(stockCode)
    page = requests.get(
        url,
        headers=headers
    )
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        print("starting parse for ", stockCode)
        save_details(soup, collection, keyword, stockCode)
    except Exception as e:
        print("exception parsing", stockCode, e)
        pass
