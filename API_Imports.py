"""
01. symbol": "TSLA",
        "02. open": "1865.0000",
        "03. high": "1911.0000",
        "04. low": "1841.2100",
        "05. price": "1878.5300",
        "06. volume": "12205331",
        "07. latest trading day": "2020-08-19",
        "08. previous close": "1887.0900",
        "09. change": "-8.5600",
        "10. change percent": "-0.4536%"
"""

import http.client
import csv
from Stock import Stock

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "ef9004ce3fmsh5276f7f8914de91p1b22ebjsnf005b4087869"
}
names = ["TSLA" , "BAC"
         # , "WMT", "NAV"
         ]

# create a csv file object and open
with open('sample.csv', 'wt') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', lineterminator='\n', )
    # Add the header row
    writer.writerow(
        ['Symbol', 'Open', 'High', 'Low', 'Price', 'Volume', 'Latest trading day', 'Previous close', 'change',
         'Change percent %'])
    # for i in range(1,20,2):
    #     # Add the data row
    #     writer.writerow([i, i+1])

    for name in names:
        string = "/query?symbol=" + name + "&function=GLOBAL_QUOTE"
        conn.request("GET", string, headers=headers)

        res = conn.getresponse()
        data = res.read()
        decoded = data.decode("utf-8")
        #print(decoded)

        decoded_splitted = decoded.split('\n')
        stock_info = []
        # print ( decoded_splitted)
        for i in range(2, len(decoded_splitted) - 2):
            split_by_dots = decoded_splitted[i].split(':')
            stock_info.append(split_by_dots[1])
            #print(split_by_dots[1])
        writer.writerow(stock_info)
        new_stock = Stock(stock_info)
        print("*****")
        new_stock.print()

    # print(data.decode("utf-8"))
