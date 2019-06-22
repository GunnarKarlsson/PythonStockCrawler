def save_details(soup, collection):
    #Add logic to skip if certain fields are empty
    ts = time.time()
    t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    dict = {}
    dict.update({"time":t})

    #name and company code
    print("A")
    s = soup.find_all("span",class_="qtxt_m_blue")
    s = s[0].text.encode("ascii", errors="ignore").decode()
    s = ''.join(char for char in s if char in printable)
    s = s.strip()
    print(s)
    try:
        code = int(s[s.find("(")+1 : s.find(")")])
    except:
        return#e.g. if code == HSI
    print("C")

    i = s.rfind('(')
    name = s[:i].strip()
    if code < 0 or code > end:
        return
    dict.update({"Code":code,"Name":name})
    print(name)
    print(code)

    #print("Code: ", code)

    #Other attributes
    labels = soup.find_all('span',class_='qtxt_s_blue')
    labels = [label.text.strip().replace(".","-") for label in labels]
    try:
        idxMkt = labels.index("Mkt Cap")
    except:
        return
    labels = labels[idxMkt:]
    values = soup.find_all('span',class_='qtxt_s_blue_b')
    values = [value.text.strip() for value in values]
    for label, value in zip(labels, values):
        k = label
        v = value

        if k == "1m H/L" or k == "3m H/L" or k == "Spread" or k == "Beta" or k == "HSCEI YTD" or k == "Capital Activity" or k == "HSI YTD" or k == "Volatility" or k == "A- Turnover (5d)" or k == "A. Turnover (5d)":
            continue

        if k == "Board Lot" or k == "Transactions" or k == "EPS" or k == "YTD" or k == "NAV":
            continue

        if k == "Yield":
            v = v.replace("%","")
            #print("Yield: ", v)
        if k == "Yield" or k == "Board Lot" or k == "P/E" or k == "P/B" or k == "Yield" or k == "EPS" or k == "NAV":
            try:
                v = float(v)
            except:
                pass
        if k == "Mkt Cap":
            if value.endswith("M"):
                value = value.replace("M","")
                head, point, tail = value.partition('.')
                value = head
            elif value.endswith("B"):
                value = value.replace("B","")
                value = value.replace(".",",")
                value = value + "0"
            v = value

        dict.update({k:v})

    collection.insert_one(dict)
    print("inserted into collection")

#python -m pip install pymongo
import pymongo
import urllib
import requests
from bs4 import BeautifulSoup
import datetime
import time
from random import randint
import re
from string import printable
#import pprint

#pp = pprint.PrettyPrinter(indent=4)

start = 129
end = 131

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
    url = "http://www.quamnet.com/Quote.action?request_locale=en_US&stockCode={}".format(stockCode)
    page = requests.get(
        url,
        headers=headers
    )
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        print("starting parse for ", stockCode)
        save_details(soup, collection)
    except Exception as e:
        print("exception parsing", stockCode, e)
        pass
