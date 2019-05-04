import requests

stockCode  = 1928
url = "http://www.quamnet.com/Quote.action?request_locale=en_US&stockCode={}".format(stockCode)
proxy_host = "proxy.crawlera.com"
proxy_port = "8010"
proxy_auth = "bf900c1ca92b40c5ad928549b82eb82b:" # Make sure to include ':' at the end
proxies = {"https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
      "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

r = requests.get(url, proxies=proxies,
                 verify=False)

print("""
Requesting [{}]
through proxy [{}]

Request Headers:
{}

Response Time: {}
Response Code: {}
Response Headers:
{}

""".format(url, proxy_host, r.request.headers, r.elapsed.total_seconds(),
           r.status_code, r.headers, r.text))
