# pandas_test6.py

import pandas as pd
import numpy as np
import seaborn as sns   # 패키지 추가 설치

# 데이터프레임 데이터 조작

# 데이터 갯수 세기 : count()
# NaN 은 세지 않음
s = pd.Series(range(10))
print(s)
s[3] = np.nan # index 3에 NaN을 기록함 (값 변경)
# 데이터 프레임에 값이 누락된 부분을 찾을 때 유용하게 이용함
np.random.seed(2)
df = pd.DataFrame(np.random.randint(5, size=(4,4)), dtype=float)
print(df)
df.iloc[2,3] = np.nan
print(df)
print(df.count()) # 각 열별 값 갯수

# 타이타닉호 승객 데이터를 데이터프레임을 만들기 위해 seaborn 패키지 사용함
titanic = sns.load_dataset('titanic')
#print(titanic.head())
#print(titanic)

# 카테고리 갯수 세기 : value_counts() 함수 사용
# 시리즈의 값이 정수, 문자열로 된 카테고리 갯수를 반환함
# 값을 종류별로 구분한 것 : 카테고리
np.random.seed(1)
s2 = pd.Series(np.random.randint(6, size=100))
print(s2.tail())       # 마지막 다섯 개 출력
print(s2.value_counts())    # 발생값별로 카운트한 결과가 출력됨

# 데이터프레임에는 value_counts() 함수가 없음
# 각열(하나의 시리즈임)마다 별도로 적용해야 함
#print(df)
#print(df[0].value_counts())

# 정렬 : sort_index(), sort_values() 함수
# sort_index() 함수 : 값을 정렬하고 난 다음에 index 배치를 확인
# sort_values() 함수 : 정렬하고 난 값들의 확인

# s2 시리즈의 값 데이터 값에 따른 데이터 갯수를 인덱스에 따라 정렬한다면
#print(s2.value_counts())
#print(s2.value_counts().sort_index()) # 인덱스 순으로 정렬

# NaN 값이 있는 경우에는 정렬하면 NaN 이 가장 나중에 배치됨
#print(s)
#print(s.sort_values())  # 값으로 정렬

# 내림차순정렬하려면, ascending=False 로 지정하면 됨
# print(s.sort_values(ascending=False))   # NaN 은 마지막에 위치함

# 데이터프레임처럼 여러 컬럼(열 : 시리즈)을 가진 경우에는
# sort_values() 로 정렬시에 by 인수로 정렬 기준이 될 컬럼(열)을 지정할 수 있음
# print(df)
# print(df.sort_values(by=3))

# 첫 번째 열 기준으로 정렬하고 나서, 첫번째 기준열의 값은 값들에 대해 두번째 열 기준으로 다시 정렬되게 하려면
# by 인수에 리스트를 사용해서 순서대로 열을 나열하면 됨
print(df.sort_values(by=[1, 2]))

# 행, 열 합계 : sum() 함수
# 행과 열의 합계를 구할 때 sum(axis=숫자) 사용
# axis 인수에는 합계로 없어지는 방향축을 지정함 : 0-행, 1-열
np.random.seed(1)
df2 = pd.DataFrame(np.random.randint(10, size=(4,8)))   # 4행8열로 0 ~ 9 사이의 정수로 초기화(랜덤)
print(df2)

# 행방향으로 합계를 구할 때는 sum(axis=1) 로 지정함
print(df2.sum(axis=1))      # 행별 합계

# 행방향으로 합계를 구할 때, 컬럼을 하나 추가하면서 합계를 구한다면
df2['RowSum'] = df2.sum(axis=1)
print(df2)  # 열이 없어지지 않음

# 열별 합계를 출력할 행을 추가하면서, 열방향(세로) 합계를 구한다면
print(df2.sum())        # axis 인수가 생략되면, 기본값은 0임
df2.loc['colTotal', :] = df2.sum()
print(df2)

# 합계 : sum(), 평균 : mean(), 갯수 : count() 사용하면 됨
# apply() 함수
# 행이나 열 단위로 좀 더 복잡한 계산을 적용하고자 할 때 사용함
# 복잡한 계산식 처리를 위해 람다함수를 사용함
df3 = pd.DataFrame({
    'A' : [1, 3, 4, 3, 4],
    'B' : [2, 5, 3, 1, 8],
    'C' : [4, 1, 3, 9, 7]
})
print(df3)

# 예 : 각 열의 최대값과 최소값의 차이를 구한다면
print(df3.apply(lambda x : x.max() - x.min()))  # 각 열의 최대값 - 최소값

# 예 : 각 행의 최대값과 최소값의 차이를 구한다면
print(df3.apply(lambda x : x.max() - x.min(), axis=1)) # 각 행의 최대값 - 최소값

# 각 열에 대해 어떤 값이 얼마나 사용되는지를 확인하려 한다면
print(df3.apply(lambda x: x.value_counts(), axis=0))

# 타이타닉호의 승객 중 나이 20살을 기준으로
# 20살 이상이면 성인 (adult), 20살 미만이면 미성년자(child)로 구별하고
# 라벨링된 컬럼을 추가해서 표시되게 한다면
titanic['adult | child'] = titanic.apply(lambda r: 'adult' if r.age >=20 else 'child', axis=1)
print(titanic.tail(10))

# fillna() 함수
# NaN 을 원하는 값으로 바꿀 때 사용
print(df3.apply(lambda x : x.value_counts(), axis=0).fillna(0.0).astype(int))
# astype() 함수 : 전체 데이터의 자료형을 바꿀 때 사용

# 실수값을 카테고리 값(컬럼단위)으로 변환
# cut() 함수 : 실수값을 경계선으로 지정하는 경우
# qcut() 함수 : 갯수가 똑같은 구간으로 분류하는 경우

# 예 : 나이 데이터를 가진 리스트의 경우
ages = [0, 2, 10, 21, 23, 37, 31, 39, 64, 20, 5, 101]
# cut() 을 사용해서 카테고리(열) 값으로 변경할 수 있음
# bins 인수로 분류하는 기준값을 지정함, 기준을 넘는 값은 NaN 이 됨
bins = [1, 20, 30, 50, 70, 100]
labels = ['미성년자', '청년', '중년', '장년', '노년']
result = pd.cut(ages, bins=bins, labels=labels)
print(result)   # 분류된 결과 확인
print(type(result))  # <class 'pandas.core.arrays.categorical.Categorical'>

# cut() 의 반환 자료형이 Categorical 클래스 객체임
# 이 객체는 categories 속성으로 라벨 문자열을 , codes 속성으로 정수로 인코딩한 값을 가지게 됨
print(result.categories)  # Index(['미성년자', '청년', '중년', '장년', '노년'], dtype='object')  => 라벨이 나옴
print(result.codes)     # [-1  0  0  1  1  2  2  2  3  0  0 -1] => 인코딩된 값 , 어느 카테고리에 속하는지?, -1 => NaN

# 위 결과를 데이터프레임에 적용한다면
df4 = pd.DataFrame(ages, columns=['ages'])
print(df4)
df4['age_category'] = pd.cut(df4.ages, bins= bins, labels=labels)
print(df4)
print(df4['age_category'])
print(type(df4['age_category']))    # <class 'pandas.core.series.Series'>

# 데이터프레임의 age_category 열의 값은 문자열이 아님 => 문자열로 바꾸려면
print(df4.age_category.astype(str))
# 확인 : 문자열 + 문자열 => 문자열 , 'a' + 'b" => 'ab'
print(df4.age_category.astype(str) + df4.age_category.astype(str))

# qcut() 함수
# 구간 경계선을 지정하지 않고, 데이터 갯수가 같도록 갯수로 구간을 나누는 함수임
# 예 : 100개의 데이터를 4개의 구간으로 나눈다면, 각각 250개씩 나누어짐
data = np.random.randn(1000)
data_qcut = pd.qcut(data, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(data_qcut)
# Length: 1000
# Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']
# print(type(data_qcut)) # <class 'pandas.core.arrays.categorical.Categorical'>
print(pd.Series(data_qcut).value_counts())
'''
Q1    250
Q2    250
Q3    250
Q4    250
Name: count, dtype: int64
'''

