import pybithumb
import datetime
import time


# 빗썸 객체 생성
with open("bitkey.txt") as f:
    lines = f.readlines()
    con = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(con, secret)

# 타겟가격 함수
def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

# 오늘 자정 설정
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

ma5 = get_yesterday_ma5("BTC")
target_price = get_target_price(“BTC”)

def buy_crypto_currency(ticker, unit):
    # krw = bithumb.get_balance(ticker)[2]
    # orderbook = pybithumb.get_orderbook(ticker)
    # sell_price = orderbook['asks'][0]['price']
    # unit = krw / float(sell_price)
    bithumb.buy_market_order(ticker, unit)

def sell_crypto_currency(ticker, unit):
    # unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

# 변동성 돌파 매도/매
while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10):
            sell_crypto_currency("BTC")

            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            target_price = get_target_price("BTC")
            ma5 = get_yesterday_ma5("BTC")

        current_price = pybithumb.get_current_price("BTC")
        if (current_price > target_price) and (current_price > ma5):
            buy_crypto_currency("BTC")
    except:
        print("에러 발생")
        time.sleep(1)