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
# 08: krw = bithumb.get_balance("BTC")[2]
# 09: orderbook = pybithumb.get_orderbook("BTC")
# 10:
# 11: asks = orderbook['asks']
# 12: sell_price = asks[0]['price']
# 13: unit = krw/sell_price
# 14: print(unit)
# 15: order = bithumb.buy_market_order("BTC", unit)
# 16: print(order)
#
#
# # 지정가 매도
# 08: unit = bithumb.get_balance("BTC")[0]
# 09: print(unit)
# 10: order = bithumb.sell_limit_order("BTC", 4000000, unit)
# 11: print(order)
# # 시장가 매도
# 08: unit = bithumb.get_balance("BTC")[0]
# 09: order = bithumb.sell_market_order("BTC", unit)
# 10: print(order)
#
# # 주문 취소
# 09: order = bithumb.buy_limit_order("BTC", 3000000, 0.001 )
# 10: print(order)
# 11:
# 12: time.sleep(10)
# 13: cancel = bithumb.cancel_order(order)
# 14: print(cancel)


import pybithumb
import time
import datetime

#보안 처리
with open("__bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(key, secret)

#금일 매수 목표가 설정: 목표가 = (전일 최고 - 전일 최대) * 0.5
def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

# 시장가 매수 코드(주의: 계좌 모든 원화를 이용해 매수함)
def buy_crypto_currency(ticker, buy_won):
    # krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    # unit = krw / float(sell_price)
    unit = buy_won / float(sell_price)
    bithumb.buy_market_order(ticker, unit)

# 시장가 매도 코드(주의: 해당 화폐의 모든 수량을 매도)
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

# 변동성 돌파(5(n)일 이동평균선)
def get_yesterday_ma5(ticker, n):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(n).mean()
    return ma[-2]

# 매도/매수
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")

while True: # 1초 주기로 계속 실행
    try:
        # 매도 (장마감 or 목표가 20% 손절)
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10) or (current_price < target_price*0.8):
            sell_crypto_currency("BTC")
            if mid < now < mid + datetime.delta(seconds=10):
                target_price = get_target_price("BTC")
                mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                ma5 = get_yesterday_ma5("BTC", 5)
        # 매수 (5일 이동평균 돌파, 목표가 돌파, 하루 한번)
        buy_count = 0
        current_price = pybithumb.get_current_price("BTC")
        if (current_price > ma5) and (current_price > target_price) and (buy_count < 1):
            buy_crypto_currency("BTC")
            buy_count = buy_count + 1
            if mid < now < mid + datetime.delta(seconds=10):
                buy_count = 0
    except:
        print("에러 발생")
    time.sleep(1)




