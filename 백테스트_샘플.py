import pybithumb
import numpy as np
import pandas as pd
from pandas import DataFrame
import time


class CoinBackTest:
    def __init__(self):
        self.df = pd.read_csv("BTCUSDT_1hour.csv")
        self.df['buy'] = 0
        self.df['sell'] = 0
        self.df['signal'] = 0
        self.indicator = pd.DataFrame()
        self.indicator['data'] = self.df['TotalTime']

    # 지표 계산하기
    def cal_indicator(self):
        start_time = time.time()
        self.indicator['sma3'] = # 1h봉의 3개로 이격도 계산
        self.indicator['3dis'] = self.df['priceClose'] - self.indicator['sma3'] #3시간 이격도
        print(time.time()-start_time, "지표 계산 시간")

    # 매수 시그널
    def buy_signal(self):
        start_time = time.time()
        for i in range(0, len(self.indicator)):
            if self.indicator['3dis'][i] >= 0: #이격도 위+미보유시 매수
                print(i, "매수")
                self.df['buy'][i] = 1 # 매수 조건 성립시 1로 설정
        print(time.time()- start_time, "매수 시그널 발생")

    # 매도 시그널
    def sell_signal(self):
        start_time = time.time()
        for i in range(0, len(self.indicator)):
            if self.indicator['3dis'][i] < 0:
                print(i, "매도")
                self.df['sell'][i] = 1 #매도 조건 성립시 1로 설정
        print(time.time()-start_time, "매도 시그널 발생")

#백테스트
def badktest(self, df):
    print("백테스트 시작")
    start_time = time.time()
    fee = 0.1 / 100  #슬리피+수수료
    money = 1000 #초기 원금
    slot = 0  #미보유시 0, 보유시 1

    buy_date_list = []
    buy_price_list = []
    amount_list = []
    sell_date_list = []
    sell_price_list = []
    money_list = []
    result_list = []

    for i in range(0, len(self.df)-1):
        if self.df['buy'][i] == 1 and slot == 0: #매수시그널&미보유
            print("매수 진입")
            slot = 1 #보유 상태로 변경

            buy_date = df['TotalTime'][i+1]
            buy_price = df['priceOpen'][i+1] #매수시그널 다음 봉 시가에서 매수
            amount = (money/buy_price)/(1+fee) #매수수량: 시가/보유수량에서 수수료 고려
            buy_date_list.append(buy_date)
            buy_price_list.append(buy_price)
            amount_list.append(amount)

        if self.df['sell'][i] == 1 and slot == 1: #매도시그널&보유
            print("매도 청산")
            slot = 0 #미보유 상태로 변경
            sell_date = df['TotalTime'][i+1]
            sell_price = df['priceOpen'][i+1] #매도시그널 다음 봉 시가에서 매도
            result = sell_price/buy_price #수익률
            # money = money*result/(1+fee) #기존 현금*수익률/수수료
            money = amount*sell_price/(1+fee)
            sell_date_list.append(sell_date)
            sell_price_list.append(sell_price)
            money_list.append(money)
            result_list.append(result)
        if len(buy_date_list) > len(sell_date_list): # 마지막 매수
            del buy_date_list[-1]
            del buy_price[-1]
            del amount_list[-1]




