import pybithumb
import time
import datetime


# 티커를 리스트로 받음
tickers = pybithumb.get_tickers()

#BTC의 현재가
price = pybithumb.get_current_price("BTC")
# 모든 티커의 현재가
all = pybithumb.get_current_price("ALL")
for ticker, data in all.items():
    print(ticker, data['closing_price'])

#한 종목의 정보
detail = pybithumb.get_market_detail("BTC") # 저가, 고가, 평균 거래 금액, 거래량

#호가창의 정보
orderbook = pybithumb.get_orderbook("BTC")
ms = int(orderbook["timestamp"])
dt = datetime.datetime.fromtimestamp(ms/1000) #현재 시간

