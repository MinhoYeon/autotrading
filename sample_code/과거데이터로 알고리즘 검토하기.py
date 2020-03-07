import pybithumb
import datetime
import time
import numpy as np


# 빗썸 객체 생성
with open("bitkey.txt") as f:
    lines = f.readlines()
    con = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(con, secret)

def get_ror(k):
    df = pybithumb.get_ohlcv("BTC")
    # df = df['2019']
    df['range'] = (df['high']-df['low'])*k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032

    # 최고가가 타겟가 보다 높은 건 매수가 일어난 것이고, 일어난 매수의 수익률은 종가/타겟가의 비율. 매수가 안일어나면 1
    df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target']-fee, 1)
    # df.to_excel('btc.xlsx')

    #각 거래의 수익 비율들의 곱은 전체 수익률이 됨.
    ror = df['ror'].cumprod()[-2]
    return ror


for i in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(i)
    print("%0.1f : %f" %(i, ror))
