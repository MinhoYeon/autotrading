import requests
from datetime import datetime
import pandas as pd
import time

starting = time.time()

ep = 'https://api.binance.com'
candle = '/api/v3/klines'

start_date = []
start_time = []
openn = []
high = []
low = []
close = []
volume = []
total_datetime = []
start = 1504224000000  # 17년 9월 1일 09:00:00 최초날짜

# start = 1582748490000 # 테스트를 위해 최근만 받아옴 (20년 2월 27일~)
first_params_candle = {'symbol': 'BTCUSDT', 'interval': '1h', 'startTime': start, 'limit': 1}  # 초기세팅
r1 = requests.get(ep + candle, params=first_params_candle)

while len(r1.json()) > 0:
    first_params_candle = {'symbol': 'BTCUSDT', 'interval': '1h', 'startTime': start, 'limit': 1000}
    r1 = requests.get(ep + candle, params=first_params_candle)  # use parameter
    req = r1.json()
    for i in range(0, len(req)):
        if float(req[i][5]) > 0:  # 거래가 있을 경우만 추가해줌
            total_datetime.append(int(datetime.fromtimestamp(req[i][0] / 1000).strftime('%Y%m%d%H%M')))
            start_date.append(int(datetime.fromtimestamp(req[i][0] / 1000).strftime('%Y%m%d')))
            start_time.append(int(datetime.fromtimestamp(req[i][0] / 1000).strftime('%H%M')))
            openn.append(float(req[i][1]))
            high.append(float(req[i][2]))
            low.append(float(req[i][3]))
            close.append(float(req[i][4]))
            volume.append(float(req[i][5]))
    if len(req) > 0:  # 받아온 데이터가 있을 경우 => 다음 루프 시작
        start = req[-1][6] + 1
        print(datetime.fromtimestamp(req[-1][6] / 1000).strftime('%Y%m%d'), "데이터 다운로드 완료...")
    else:
        print("다운로드 완료")
    # time.sleep(0.25) # 횟수제한을 위해 추가

ticker = ['BTCUSDT'] * len(start_date)

chartData = {'Ticker': ticker, 'TotalTime': total_datetime, 'logDate': start_date, 'logTime': start_time,
             'priceOpen': openn, 'priceHigh': high,
             'priceLow': low, 'priceClose': close, 'amount': volume}
df = pd.DataFrame(chartData,
                  columns=['Ticker', 'TotalTime', 'logDate', 'logTime', 'priceOpen', 'priceHigh', 'priceLow',
                           'priceClose', 'amount'])

df = df.sort_values(by=['TotalTime'], ascending=True)
df.to_csv("C:/coding/coin/data/BTCUSDT_1hour.csv", header=True, index=False)  # csv파일로 저장