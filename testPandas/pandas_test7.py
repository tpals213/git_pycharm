# pandas_test7.py

import pandas as pd
import numpy as np

# 시계열 데이터 다루기
# 시간과 날짜 데이터를 시계열 데이터라고 함
# pandas 는 시계열 데이터를 다루려면, 인덱스 자료형을 DatetimeIndex 로 지정해야 함
# DatetimeIndex : 타임스탬프(timestamp) 형식의 특정 시간을 기록하는 시계열 데이터를 다루기 위한 인덱스임
# 타임스탬프 인덱스 라벨은 일정한 간격을 유지할 필요는 없음
# DatetimeIndex 생성함수 : pd.to_datetime(), pd.date_range() 함수 사용함

# pd.to_datetime() 함수
# 날짜, 시간을 나타내는 문자열을 자동으로 datetime 자료형을 바꾼 다음,
# DatetimeIndex 를 생성하는 함수임
date_str = ['2018. 1. 4', '2018. 1. 5', '2018. 1. 6']
idx = pd.to_datetime(date_str)
print(idx)
# DatetimeIndex(['2018-01-04', '2018-01-05', '2018-01-06'], dtype= 'datetime64[ns]', freq=None)

# pd.date_range() 함수
# 모든 날짜, 시간을 일일히 입력하지 않고, 시작일과 종료일 또는 시작일과 간격을 입력하면
# 해당 범위 내의 시계열 인덱스를 생성해주는 함수
print(pd.date_range('2018-4-1', '2018-4-30'))
'''
DatetimeIndex(['2018-04-01', '2018-04-02', '2018-04-03', '2018-04-04',
               '2018-04-05', '2018-04-06', '2018-04-07', '2018-04-08',
               '2018-04-09', '2018-04-10', '2018-04-11', '2018-04-12',
               '2018-04-13', '2018-04-14', '2018-04-15', '2018-04-16',
               '2018-04-17', '2018-04-18', '2018-04-19', '2018-04-20',
               '2018-04-21', '2018-04-22', '2018-04-23', '2018-04-24',
               '2018-04-25', '2018-04-26', '2018-04-27', '2018-04-28',
               '2018-04-29', '2018-04-30'],
              dtype='datetime64[ns]', freq='D')
'''
print(pd.date_range('2021-12-1', periods= 30))

# freq 인수로 특정 날짜만 생성되도록 할 수도 있음
# s : 초, T : 분, H : 시간
# D : 일(day), B : 주말이 아닌 평일,  W : 주(일요일), W-MON : 주(월요일)
# M : 각 달(month) 의 마지막 날, MS : 각 달의 첫날
# BM : 주말이 아닌 평일 중에서 각 달의 마지막 날
# BMS : 주말이 아닌 평일중에서 각 달의 첫날
# WOM-2THU : 각 달의 두번째 목요일
# Q-JAN : 각 분기의 첫 달의 마지막 날
# Q-DEC : 각 분기의 마지막 달의 마지막 말
# # 아래 웹사이트 참조 :
# # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects

print(pd.date_range('2019-4-1', '2019-4-30', freq='B'))  # 평일로만 만들기
print(pd.date_range('2019-4-1', '2019-4-30', freq='W'))  # 주 단위로 만들기 (일요일로)
print(pd.date_range('2019-4-1', '2019-4-30', freq='W-MON'))  # 주 단위로 만들기 (월요일로)
print(pd.date_range('2019-4-1', '2019-4-30', freq='MS'))  # 그 달의 첫날
print(pd.date_range('2019-4-1', '2019-4-30', freq='MS'))  # 그 달의 시작 날
print(pd.date_range('2019-4-1', '2019-4-30', freq='ME'))  # 그 달의 마지막 날
print(pd.date_range('2019-4-1', '2019-4-30', freq='BMS'))  # 주말이 아닌 평일중에서 각 달의 첫날
print(pd.date_range('2019-4-1', '2019-4-30', freq='WOM-2THU'))  # 각 달의 두번째 목요일
print(pd.date_range('2019-4-1', '2019-4-30', freq='QE-JAN'))  # 각 분기의 첫 달의 마지막 날

# shift 연산
# 시계열 데이터 인덱스는 날짜 이동에 대한 연산이 가능함
# shift 연산을 이용하면 인덱스는 그대로 두고, 데이터만 이동할 수 있음
np.random.seed(0)
ts = pd.Series(np.random.randn(4), index = pd.date_range('2023-1-1', periods=4, freq='ME'))
print(ts)
#print(ts.shift(1))  # 아래로 1칸 이동
#print(ts.shift(-1)) # 위로 1칸 이동
print(ts.shift(1, freq='ME')) # 인덱스라벨도 같이 이동, 1달씩 뒤로 밀림
print(ts.shift(1, freq='W')) # 각 달의 첫 주의 일요일 날짜로 이동됨(변경됨)

# resample 연산
# 시간 간격을 재조정할 때 사용함
# 업샘플링(up-sampling) : 시간 구간을 줄이면 데이터 양이 증가함
# 다운샘플링(down-sampling) : 시간 구간을 늘리면 데이터 양이 감소함
ts = pd.Series(np.random.randn(100), index=pd.date_range('2018-1-1', periods=100, freq= 'D'))
print(ts.tail(20))

# 다운 샘플링의 경우, 원래 데이터가 그룹으로 묶이기 때문에 groupby 와 같은 그룹연산을 해서 대표값을 구해야 함
print(ts.resample('W').mean())  # 7일의 데이터로 합쳐서 평균을 냄
print(ts.resample('MS').first())

# 날짜가 아닌 시/분 단위에서는 구간위 왼쪽 한계값(가장 빠른 값) 은 포함됨
# 오른쪽 한계값(가장 늦은값)은 포함 안 됨
# 예, 10분간격으로 구간을 만들면 10의 배수가 되는 시각은 다음 구간을 시작점이 됨
ts = pd.Series(np.random.randn(60), index=pd.date_range('2024-1-1', periods=60, freq='min'))
print(ts.head(20))
# 10분 간격으로 구간을 만들어서 계산한다면
print(ts.resample('10min').sum())  # 0분 ~ 9분까지 합계

# 왼쪽(시작값)이 아니라 오른쪽(끝값)을 구간에 포함하려면
# closed = 'right' 인수 사용하면 됨 (기본은 'left')
print(ts.resample('10min', closed='right').sum())  # 0분 ~ 10분까지 합계

# ohlc() 함수 : 구간의 시고저종(open, high, low, close) 값을 구함
print(ts.resample('5min').ohlc())  # 5분단위로 시작값 높은값 낮은값 마지막값

# 업샘플링의 경우에는 존재하지 않는 데이터를 만들어야 함
# 앞 데이터를 뒤 데이터로 그대로 쓰는 forward filling 방식과
# 뒤 데이터를 앞에서 미리 쓰는 backward filling 방식
# bfill(), ffill() 제공됨
print(ts.resample('30s').ffill().head(20))
print(ts.resample('30s').bfill().head(20))

# dt 접근자
# datetime 자료형 시리즈에 dt 접근자 제공, 속서오가 메소드도 제공
s = pd.Series(pd.date_range('2023-12-25', periods=100, freq='D'))

# year, month, day, weekday 등의 속성을 이용하면, 년, 월, 일, 요일 정보를 추출할 수 있음
print(s.dt.year)
print(s.dt.weekday) # 요일, 1(일요일)

# strfime() 함수 : 포맷(format)을 이용해서 문자열 형태로 변환하는 함수
print(s.dt.strftime('%Y년 %m월 %d일'))














