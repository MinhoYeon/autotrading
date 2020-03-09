import sqlite3

#DB 생성 및 cursor 객체 생성, table 생성 및 데이터 삽입
con = sqlite3.connect("C:/Users/user/Google 드라이브/sample/kospi.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, close int, Volum int)")
cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")
cursor.execute("INSERT INTO kakao VALUES('16.06.02', 99000, 99300, 96300, 97500, 556790)")
con.commit()
con.close()

# DB 연결 및 cursor 객체 생성, table 선택 및 데이터 찾기
con = sqlite3.connect("C:/Users/user/Google 드라이브/sample/kospi.db")
cursor = con.cursor()
cursor.execute("SELECT * FROM kakao")
cursor.fetchone() # 로우 한줄만
cursor.execute("SELECT * FROM kakao")
cursor.fetchall() # 모든 로우
kakao = cursor.fetchall() #리스트 데이터
kakao[0] #로우 한개 튜플 데이터
kakao[0][1] #로우 한개의 인덱스 1의 데이터

## DataFrame 객체를 DB에 저장하기
import pandas as pd
from pandas import Series, DataFrame
import sqlite3
# 데이터프레임 객체 만들기
raw_data = {'col0': [1, 2, 3, 4], 'col1': [10, 20, 30, 40], 'col2': [100, 200, 300, 400]}
df = DataFrame(raw_data)
# DB에 연결해서 저장하고, 저장확인
con = sqlite3.connect("C:/Users/user/Google 드라이브/sample/kospi.db")
df.to_sql('dfToDB', con) #테이블 이름, 연결된 DB
pf1 = pd.read_sql("SELECT * FROM dfToDB", con, index_col = 'index') #sql구문, 열결된 DB

## DB에서 데이터 읽어와서 데이터 프레임 만들기
con = sqlite3.connect("C:/Users/user/Google 드라이브/sample/kospi.db")
df3 = pd.read_sql("SELECT * FROM kakao", con, index_col='Date')

## Pandas를 이용한 주가 데이터 저장
import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3
#데이터리더로 주식 데이터 가져오기
start = datetime.datetime(2010,1,1)
end = datetime.datetime(2016,12,31)
df = web.DataReader("078930.KS", "yahoo", start, end)
# df.head()
# DB에 저장하기
con = sqlite3.connect("C:/Users/user/Google 드라이브/sample/kospi.db")
df.to_sql('078930', con, if_exists = 'replace')
df_readed = pd.read_sql("SELECT * FROM '078930'", con, index_col='Date')
# df_readed.head()

