import requests
import datetime


url = "https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw"
resp = requests.get(url)
xrp = resp.json()

timestamp = xrp['timestamp']
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)







