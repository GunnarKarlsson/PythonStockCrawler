# Hong Kong Stock Valuation Ratio Crawler

A tool to gather valuation ratios for companies listed on the Hong Kong Stock Exchange in a csv file, and query the data

## Crawler

To crawl, do:

```$ python crawl.py```

Crawls stock codes 1 to 9999. 

Saves results to a csv file called ```stocks.csv```

## Query

Query ```stocks.csv``` file from command line with basic custom query statements.

Example: 
```$ python query.py "select pe < 3 and pe > 1 and pb < 0.2"```

Supported ratios: 
* "pb" (price-to-book)
* "pe" (price-to-earning)
* "yield" (dividend yield)

Supported operators: 
* ">"
* "<"

Example Result:
```
-----------------------------------------------
QUERY: select pe < 3 and pe > 1 and pb < 0.2
-----------------------------------------------
CODE    NAME                P/E     P/B   YIELD
-----------------------------------------------
70      RICH-GOLDMAN      1.519   0.058       0
89      TAI-SANG-LAND     2.709   0.148   5.353
129     ASIA-STANDARD      1.63   0.065       0
153     CHINA-SAITE       2.311   0.094       0
191     LAI-SUN-INT'L     1.108   0.137   0.922
214     ASIA-ORIENT       1.322    0.06       0
292     ASIA-STD-HOTEL    1.084   0.118       0
342     NEWOCEAN-ENERGY   1.602   0.128       0
488     LAI-SUN-DEV       1.014   0.137   1.333
497     CSI-PROPERTIES    2.017   0.181   2.101
898     MULTIFIELD-INTL   2.126   0.152   4.815
1023    SITOY-GROUP       2.731   0.165  11.268
1155    CENTRON-TELECOM   1.726   0.117       0
1305    WAI-CHI-HOLD      2.515   0.138       0
1623    HILONG            1.675   0.081       0
1668    CHINASOUTHCITY    2.492   0.189   3.704
1676    SHENGHAI-GROUP    1.536   0.099       0
2330    CHINA-UPTOWN        1.6   0.186       0
2907    C-SHENGHAI-OLD    1.739   0.112       0
8080    NAS-HOLDINGS      1.548   0.158       0
8243    DAHE-MEDIA        2.234   0.185       0
-----------------------------------------------
Results: 21
-----------------------------------------------
