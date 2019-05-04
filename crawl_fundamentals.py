import pymongo
import urllib
import requests
from bs4 import BeautifulSoup
import datetime
import time
#import pprint

#pp = pprint.PrettyPrinter(indent=4)

def save_details(soup, collection):
        ts = time.time()
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        dict = {}
        dict.update({"time":t})

        #date_headers = soup.find_all(attrs={"ref" : "FR_Field_NB_1"})

        closing_dates = soup.find("td", text="Closing Date").find_next_siblings("td")

        print("closing dates: ",closing_dates)
        for n in closing_dates:
            print(n.text)

start = 1
end = 1
#client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
client = pymongo.MongoClient("mongodb://localhost:27017/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.fundamentals

for stockCode in range(start, end+1):
    url = "http://www.aastocks.com/en/stocks/analysis/company-fundamental/financial-ratios?symbol={}".format(stockCode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    save_details(soup, collection)
