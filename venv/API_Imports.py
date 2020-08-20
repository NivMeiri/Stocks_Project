import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "ef9004ce3fmsh5276f7f8914de91p1b22ebjsnf005b4087869"
    }
names = ["TSLA","BAC","WMT","NAV"]

for name in names:
    string = "/query?symbol=" + name + "&function=GLOBAL_QUOTE"
    conn.request("GET", string, headers=headers)


    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))