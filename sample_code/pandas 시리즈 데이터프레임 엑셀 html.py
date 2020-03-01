from pandas import Series
##시리즈
#생성
date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
xrp_close = [512, 508, 512, 507, 500]
s = Series(xrp_close, index=date)
print(s)
#시프트
s = Series([100, 200, 300])
s1 = s.shift(1)
s2 = s.shift(-1)
print(s)
print(s1)
print(s2)

##데이터프레임
from pandas import DataFrame
#생성
data = {'open': [100, 200], 'high': [110, 210]}
df = DataFrame(data, index=['18-02-01', '18-02-03'] )
print(df)
#인덱싱
print(df['open'])
print(df.loc['18-02-01'])
print(df.iloc[0])
#추가
s = Series([300, 400], index=['18-02-01', '18-02-03'])
df['volume'] = s
print(df)
df.loc['18-02-04'] = (100, 200, 300)
print(df)
#연산후 추가
upper = df['open']*2
df['upper'] = upper
print(df)

import pandas as pd
#엑셀
df = pd.read_excel('pandas_excel.xlsx')
print(df)
df = df.set_index("date")
print(df)
df.to_excel('pandas_excel_1.xlsx')
#html
url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
df = pd.read_html(url)
print(df[0].dropna(axis=0)) #axis=0은 행 삭제,
