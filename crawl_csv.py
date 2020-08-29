def save_details(page, stockCode):
    global writer
    #Add logic to skip if certain fields are empty
    ts = time.time()
    t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    #name and company code
    print("company info:", page)
    company_info = json.loads(page)
    quote = company_info[str(stockCode)]['quote']
    fin_info = company_info[str(stockCode)]['fin_info']
    name = str(quote['short_name_en_us']).replace(",","+")
    name = name.replace(" ","-")
    
    if name == "None":
        print("No name")
        return

    with open('stocks.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([stockCode, name, fin_info['pe'], fin_info['pb'], fin_info['yield'], t])
     
import csv
import requests
import json
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

start = 1
end = 9999

writer = None

with open('stocks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['code', 'name', 'pe', 'pb', 'yield', 'time'])

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
headers = {
    'User-Agent': USER_AGENT
}
for stockCode in range(start, end+1):
    time.sleep(randint(1, 3))
    url="https://www.quamnet.com/api/v1/quote/stock_quote_with_fin_info?stock_code[]={}&realtime=false".format(stockCode)
    print(url)
    page = requests.get(
        url,
        headers=headers
    )
    #soup = BeautifulSoup(page.content, 'html.parser')
    try:
        print("starting parse for ", stockCode)
        save_details(page.content, stockCode)
    except Exception as e:
        print("exception parsing", stockCode, e)
        pass