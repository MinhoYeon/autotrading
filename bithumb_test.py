import pybithumb
import time
import datetime

#보안 처리
with open("_bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(key, secret)


df = pybithumb.get_ohlcv("BTC")
print(df.tail())


# # 티커 및 밸런스
# for ticker in pybithumb.get_tickers() :
#     balance = bithumb.get_balance(ticker)
#     print(ticker, " : ", balance)
#     time.sleep(0.1)
#
# # 지정가 매수
# order = bithumb.buy_limit_order("BTC", 3900000, 0.001)
# print(order)
# # 시장가 매수
# order = bithumb.buy_market_order("BTC", 1)
# print(order)
# # 보유 계좌에서 원화, 호가정보, 시장가 매수
# krw = bithumb.get_balance("BTC")[2]
# orderbook = pybithumb.get_orderbook("BTC")
# asks = orderbook['asks']
# sell_price = asks[0]['price']
# unit = krw/sell_price
# print(unit)
# order = bithumb.buy_market_order("BTC", unit)
# print(order)
#
# # 지정가 매도
# unit = bithumb.get_balance("BTC")[0]
# print(unit)
# order = bithumb.sell_limit_order("BTC", 4000000, unit)
# print(order)
# # 시장가 매도
# unit = bithumb.get_balance("BTC")[0]
# order = bithumb.sell_market_order("BTC", unit)
# print(order)
#
# # 주문 취소
# order = bithumb.buy_limit_order("BTC", 3000000, 0.001 )
# print(order)
# time.sleep(10)
# cancel = bithumb.cancel_order(order)
# print(cancel)
