import pybithumb
import time

# #에러 처리
# while True:
#      price = pybithumb.get_current_price("BTC")
#      try:
#          print(price/10)
#      except:
#          print("에러 발생", price)
#      time.sleep(0.2)
#
#
# # 일봉데이터 가져오기 (날짜별 시가, 고가, 저가, 종가, 거래량 (OHLCV)이 저장된 Pandas DataFrame 객체)
# btc = pybithumb.get_ohlcv("BTC")

# # 이동평균선(가상화폐 종류, 평균할 날자수)
# def move_average_day(ticker, num):
#     dayData = pybithumb.get_ohlcv(ticker)
#     ma = dayData["close"].rolling(num).mean()
#     return ma

# 5일이동평균선을 현재가가 돌파하는지 확인하는 함수
def bull_market(ticker, num):
    dayData = pybithumb.get_ohlcv(ticker)
    ma = dayData["close"].rolling(num).mean()
    last_ma = ma[-2]
    price = pybithumb.get_current_price(ticker)
    if price > last_ma:
        return True
    else:
        return False

tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker, 5)
    if is_bull: print(ticker, " 상승장")
    else: print(ticker, " 하락장")
