import pybithumb
import numpy as np
from pandas import DataFrame

def get_ror(ticker, year, target_k, mo_ve_n):
    try:
        df = pybithumb.get_ohlcv(ticker)
        df = df[year]
        # 목표가 설정
        df['range'] = (df['high'] - df['low']) * target_k
        df['target'] = df['open'] + df['range'].shift(1)
        # 이동평균선
        df['ma5'] = df['close'].rolling(mo_ve_n).mean().shift(1)
        df['bull'] = df['open'] > df['ma5']
        fee = 0.0032
        df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                             (df['close'] / df['target']) - fee,
                           1)
        # 기간 수익률
        df['hpr'] = df['ror'].cumprod()
        # 최대 낙폭
        df['dd'] = ((df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax()) * 100
        return df['hpr'][-2]
    except:
        return 1

tickers = pybithumb.get_tickers()
# hprs = []
for year in range(2016, 2020, 1):
    raw_data = {'ticker' : [],
                'hpr': []}
    for ticker in tickers:
        hpr = get_ror(ticker, year, 0.5, 5)
        raw_data['ticker'].append(ticker)
        raw_data['hpr'].append(hpr)

    data = DataFrame(raw_data)
    data.to_excel(str(year) + "_ticker_hpr.xlsx")

    # hprs.append((ticker, hpr))

# sorted_hrps = sorted(hprs, key=lambda x:x[1], reverse=True)
# print(sorted_hrps[:5])

# for k in np.arange(0.1, 1,0, 0.1):
#    ror = get_ror(k)
#    print("%.1f %f" %(k, ror))


