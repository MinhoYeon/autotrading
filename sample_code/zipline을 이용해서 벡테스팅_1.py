import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

# data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)
data = web.DataReader("AAPL", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

#초기값 설정
def initialize(context):
    pass
#알고리즘 함수
def handle_data(context, data):
    order(symbol('AAPL'), 1)

#초기값과 알고리즘으로 객체생성후 객체에 데이터 넣어서 시뮬레이션
algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

#시뮬레이션된 값 그래프 그리기
plt.plot(result.index, result.portfolio_value)
plt.show()