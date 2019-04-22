def save_details(soup, collection):
    #Add logic to skip if certain fields are empty
    ts = time.time()
    t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    dict = {}
    dict.update({"time":t})
    #name and company code
    s = soup.find_all('span',class_='qtxt_m_blue')
    s = s[0].text.strip()
    code = s[s.find("(")+1:s.find(")")]
    i = s.rfind('(')
    name = s[:i].strip()
    dict.update({"Code":code,"Name":name})
    print("Code: ", code)

    #Other attributes
    labels = soup.find_all('span',class_='qtxt_s_blue')
    labels2 = [label.text.strip().replace(".","-") for label in labels]
    try:
        idxMkt = labels2.index("Mkt Cap")
    except:
        return
    labels2 = labels2[idxMkt:]
    values = soup.find_all('span',class_='qtxt_s_blue_b')
    values2 = [value.text.strip() for value in values]
    labels = labels[2:]
    for label, value in zip(labels2, values2):
        k = label
        v = value
        if k == "Yield":
            print("Yield: ", v)
        dict.update({k:v})

    collection.insert_one(dict)

#python -m pip install pymongo
import pymongo
import urllib
import requests
from bs4 import BeautifulSoup
import datetime
import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

start = 1
end = 9999
client = pymongo.MongoClient("mongodb+srv://user0:asdfasdf@cluster0-813m4.mongodb.net/hkstocks?retryWrites=true")
db = client.hkstocks
collection = db.stocks
#collection.delete_many({}) #delete all

for stockCode in range(start, end+1):
    url = "http://www.quamnet.com/Quote.action?request_locale=en_US&stockCode={}".format(stockCode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    save_details(soup, collection)
