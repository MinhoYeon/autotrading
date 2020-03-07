import pybithumb
import time

con_key = ""
sec_key = ""

#객체 생성
bithumb = pybithumb.Bithumb(con_key, sec_key)

#티커의 잔고 얻기
for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)


## 매수
#지정가 매수
order = bithumb.buy_limit_order("BTC", 3900000, 개수)
print(order)
#비트코인은 최소 0.001개를 주문해야 함. 빗썸은 소수점 넷째 자리까지의 주문만 가능
#'호가 단위' 1,000원 단위로 비트코인의 가격이 결정


#시장가 매수
order = bithumb.buy_market_order("BTC", 개수)
print(order)


#본인 계좌의 보유 원화를 조회하고, 최우선 매도 호가 금액을 얻어와 매수할 수 있는 비트코인 개수를 계산
krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/sell_price

print(unit)


#주문할 비트코인의 개수를 계산 후 시장가 주문을 발행하는 코드
krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/float(sell_price)

order = bithumb.buy_market_order("BTC", unit(총개수))
print(order)


##매도
#지정가매도
order = bithumb.sell_limit_order("BTC", 4000000, 개수)
print(order)

#시장가매도
order = bithumb.sell_market_order("BTC", 개수)
print(order)

##주문취소
cancel = bithumb.cancel_order(order)
print(cancel)