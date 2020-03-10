from sample_code.pandas import Series, DataFrame

#시리즈 생성, 인덱스 지정 시리즈 생성
kakao = Series([92600, 92400, 92100, 94300, 92300])
kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
#인덱스 보기, 시리즈 값 보기
for index_date in kakao2.index:
    print(index_date)
for value in kakao2.values:
    print(value)

#데이터 프레임 생성
daeshin = {'open': [11650, 11100, 11200, 11100, 11000],
           'high': [12100, 11800, 11200, 11100, 11150],
           'low': [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}
daeshin_day = DataFrame(daeshin)
#컬럼 순서 지정
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])
#인덱스 지정
index_date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=index_date)
#컬럼 인덱스 확인
print(daeshin_day.columns)
print(daeshin_day.index)
#컬럼 선택, 행 선택
print(daeshin_day['close'])
print(daeshin_day.loc['16.02.29'])