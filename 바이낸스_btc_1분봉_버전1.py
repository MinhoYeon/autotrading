import requests
import pprint
from datetime import datetime
import time
from pandas import DataFrame

ep = 'https://api.binance.com'
candle = '/api/v3/klines'

#start = 1504224000000
start = 1582748490000 #(20-02-27 이후)
start_date = []
start_time = []
open = []
high = []
low = []
close = []
volume = []

first_params_candle = {'symbol': 'BTCUSDT', 'interval':'1m', 'startTime' : start,'limit': 1} #초기 세팅
r1 = requests.get(ep+candle, params=first_params_candle)
while len(r1.json()) > 0:
    first_params_candle = {'symbol': 'BTCUSDT', 'interval': '1m', 'startTime': start, 'limit': 1000}
    r1 = requests.get(ep + candle, params=first_params_candle)
    for i in range(0, len(r1.json())):
        start_date.append(datetime.fromtimestamp(r1.json()[i][0]/1000).strftime('%Y%m%d'))
        start_time.append(datetime.fromtimestamp(r1.json()[i][0]/1000).strftime('%H%M'))
        open.append(r1.json()[i][1])
        high.append(r1.json()[i][2])
        low.append(r1.json()[i][3])
        close.append(r1.json()[i][4])
        volume.append(r1.json()[i][5])
    if len(r1.json()) > 0:
        start = r1.json()[-1][6] + 1 # endtime+1sec
        print("중간 다운로드")
    else: 
        print("Download completed")
    time.sleep(0.25)
    
ticker = ['BTCUSDT']*len(start_date)

charData = {'data': start_date, 'time': start_time, 'ticker': ticker, 'open': open, 'high': high, 'low': low, 'close': close, 'volume': volume}
df = DataFrame(charData, columns=['data', 'time', 'ticker', 'open', 'high', 'low', 'close', 'volume'])
df.to_csv('btc_1m.csv', header=True, index=False)

        
        
        

#pprint.pprint(r3.json())
