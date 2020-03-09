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
def get_target_price(ticker, k):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * k
    return target

# 매수 코드(주의: 계좌 모든 원화를 이용해 매수함)
def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    bithumb.buy_market_order(ticker, unit)

# 매도 코드(주의: 해당 화폐의 모든 수량을 매도)
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

# 변동성 돌파(5일 이동평균선)
def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

# 매도/매수
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")

while True: # 1초 주기로 계속 실행
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10):
            target_price = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            sell_crypto_currency("BTC")

            ma5 = get_yesterday_ma5("BTC")

        current_price = pybithumb.get_current_price("BTC")
        if (current_price > ma5) and (current_price > target_price):
            buy_crypto_currency("BTC")
    except:
        print("에러 발생")
    time.sleep(1)




