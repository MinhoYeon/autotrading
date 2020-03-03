import pandas_datareader.data as web
import datetime

#판다스의 데이터리더를 이용한 일봉데이터 가져오기
# start = datetime.datetime(2016, 2, 19)
# end = datetime.datetime(2016, 3, 4)
# gs = web.DataReader("078930.KS", "yahoo", start, end)

gs = web.DataReader("078930.KS", "yahoo")
gs.info()
    # <class 'pandas.core.frame.DataFrame'>
    # DatetimeIndex: 1222 entries, 2015-03-04 to 2020-03-02
    # Data columns (total 6 columns):
    # High         1222 non-null float64
    # Low          1222 non-null float64
    # Open         1222 non-null float64
    # Close        1222 non-null float64
    # Volume       1222 non-null float64
    # Adj Close    1222 non-null float64
    # dtypes: float64(6)
    # memory usage: 66.8 KB

#그래프 그리기
import matplotlib.pyplot as plt
plt.plot(gs.index, gs['Adj Close']) #x축/y축
plt.show()