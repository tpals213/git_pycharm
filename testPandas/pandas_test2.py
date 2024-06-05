# pandas_test2.py

import pandas as pd
import numpy as np

# 1. Series 클래스
s = pd.Series([9904312, 3448737, 2890451, 2466052], index=['서울', '부산', '인천', '대구'])
print(s)

# Series.index 속성 : 인덱스라벨 확인
print(s.index)

# Series.values 속성 : data 확인
print(s.values)

# Series.name 속성 : 시리즈에 이름 붙일 수 있음
# index.name 속성 : 시리즈의 인덱스에도 이름을 붙일 수 있음
s.name = '인구'
s.index.name = '도시'
print(s)

# 시리즈 연산
# numpy의 배열 백터화연산을 Series에도 사용할 수 있음
# 단, 시리즈의 값에만 연산이 허용됨

# 예 : 인구 숫자를 백만단위로 만들기 위해, 시리즈 객체에 100만을 나누기함
print(s / 1000000)

# 시리즈 인덱싱 : numpy 의 배열처럼 인덱싱 가능함
# 슬라이싱 시에도 인덱스 라벨을 사용 가능
# 인덱싱하면 값이 반환
# print(s[1], s['부산'])    # FutureWarning 발생 => 사용 변경됨
print(s.iloc[3], s.loc['대구'], s.대구) # 사용 권장

# 배열 인덱싱으로 데이터 순서를 바꾸거나, 특정 데이터만 선택 가능
# 시리즈변수.iloc[[순서 나열 리스트]], 시리즈변수.loc[[라벨 나열 리스트]]
print(s.iloc[[0, 3, 1]])
print(s.loc[['서울', '대구', '부산']])

# 인구가 250만 초과, 500만 미만인 경우의 값만 출력
print(s[(250e4 < s) & (s <500e4)])

# 슬라이싱
print(s[1:3])
print(s['부산':'대구']) # 부산부터 대구까지 (대구 포함)

# 시리즈와 딕셔너리 자료형
# 시리즈의 인덱스 라벨이 딕셔너리의 키(key)에 해당됨
# 딕셔너리에서 in 과 item() 함수를 시리즈에도 사용할 수 있음
print('서울' in s)    # 인덱스 라벨 중에 있느냐?
print('대전' in s)    # False

for k, v in s.items():
    print('%s = %d' % (k, v))

# 딕셔너리 객체를 시리즈로 변환할 수 있음
dict = {'서울' : 9654123, '부산' : 3345678, '인천' : 2658741, '대전' : 2431568}
print(dict)
s2 = pd.Series(dict)
print(s2)
s2.name = '2020년 인구'
s2.index.name = '도시'
print(s2)

# 딕셔너리의 값들을 원하는 순서대로 시리즈로 생성되게 하려면, index 속성을 이용함
# 키에 대한 재배치 용도로 속성을 이용할 수 있음
s3 = pd.Series(dict, index=['부산', '대전', '인천','서울'])
print(s3)

# 인덱스 기반 연산
s4 = s - s2     # 같은 인덱스 라벨 값들끼리만 계산됨
print(s4)   # 두 시리즈에 라벨이 일치하지 않는 값은 NaN 처리

print(s.values - s2.values) # s[0] - s2[0], s[1] - s2[1], ...

# Series.notnull
# 대구와 대전은 두 시리즈에 모두 존재하지 않기 때문에 계산이 불가능해서 NaN (Not A Number) 이라는 결과
# NaN 값은 float 자료형에서만 표현 가능함
# 계산 결과에서 NaN 이 아닌 값들만 구하려면 notnull() 메소드 사용
print(s4.notnull()) # True | False 로 표현
print(s4[s4.notnull()]) # NaN이 아닌 값만 출력

# 인구 증가율(%)을 계산
s5 = (s - s2) / s2 * 100
s5 = s5[s5.notnull()]
print(s5)

# 시리즈의 데이터 갱신(update), 추가(add), 제거(delete) 가능
# 인덱싱을 이용하면 딕셔너리처럼 데이터를 추가, 갱신할 수 있음
s5['부산'] = 1.63 # 인덱스 라벨이 존재하면 갱신
print(s5)
s5['대구'] = 1.45 # 인덱스 라벨이 존재하지 않으면 추가
print(s5)

# 시리즈의 데이터를 삭제할 때는 del 명령 사용
del s5['서울']
print(s5)