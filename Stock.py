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
class Stock:
    def __init__(self, symbol, open, high, low , price, volume, lateset, prev, change, change_rate):
        self.symbol = symbol
        self.price = price
        self. open = open
        self.high = high
        self.low = low
        self. change = change
        self. changeRate = change_rate
        self.volume = volume
        self.latest = lateset
        self.prev = prev

    def __init__(self,lst):
        self.symbol = lst[0]
        self.price = lst[4]
        self. open = lst[1]
        self.high = lst[2]
        self.low = lst[3]
        self. change = lst[8]
        self. changeRate = lst[9]
        self.volume = lst[5]
        self.latest = lst[6]
        self.prev = lst[7]

    def compare_by_price(self,other):
        return self.price >= other.price


    def print(self):
        print("Name: "+ self.symbol)
        print("Price: "+self.price)
        print("Change rate: "+self.changeRate)

