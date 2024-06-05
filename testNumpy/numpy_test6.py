# numpy_test6.py

import numpy as np

# 배열 생성과 초기화 처리 함수 사용
# 초기값 : 변수 공간에 첫번째로 기록되는 값
# 변수 공간 만들면서 바로 초기값 기록하는 것을 초기화라고 함
# np.array([,,,,,])  => 리스트 값들로 초기화됨

# zeros() : 배열 생성시 0으로 초기화함
# 사용 : 배열변수 = np.zeros(배열할당갯수)  => 1차원배열 생성하고, 0으로 초기화함
# 사용 : 배열변수 = np.zeros((행의 갯수, 열의 갯수))  => 2차원배열 생성하고, 0으로 초기화함
# 사용 : 배열변수 = np.zeros((면갯수, 행갯수, 열갯수))  => 3차원배열 생성하고, 0으로 초기화함


ar = np.zeros(5)   # 5개의 값을 기록할 수 있는 1차원배열 생성하고, 모두 0으로 초기화함
print(ar)
print(ar.dtype)     # float64

br = np.zeros((2,3))
print(br)

# array() 함수와 마찬가지로 zeros() 함수도 dtype 매개변수 사용할 수 있음
cr = np.zeros((5,2), dtype='i4')
print(cr)
print(cr.dtype)

# zeros() 함수로 문자배열로 초기화할 수도 있음
# 문자열은 빈 문자열('')로 초기화됨
dr = np.zeros(5, dtype='U4')
print(dr)
print(dr.dtype)     #  <U4 : 유니코드문자 4글자

# 각 인덱스에 값 기록
dr[0] = 'abc'
dr[1] = 'abcd'
dr[2] = 'ABCDE'     # U4 이므로, 마지막 'E' 는 기록되지 않는다.
print(dr)

# ones() 함수
# 배열 생성하면서, 1로 초기화함
ear = np.ones((2, 3, 4), dtype='i8')    # 2면3행4열 3차원배열 생성, 정수 1로 초기화
print(ear)

# zeros_like() 함수, ones_like() 함수
# 다른 배열과 같은 크기의 배열을 생성하면서 초기화할 때 사용함
# 예 : 2행3열의 2차원배열인 br 과 같은 크기의 배열을 생성하려면
far = np.ones_like(br, dtype='f')
print(far)

# empty() 함수
# 값이 기록되지 않은 빈 배열 생성시 사용함 : 배열 생성 시간이 짧아짐 (초기화 시간이 제외됨)
gar = np.empty((4,3))
print(gar)  # 메모리에 배열공간을 만듬. 메모리에 이전에 기록되어있던 값들이 남아있음.(쓰레기값) 그것이 출력됨. 자바는 변수선언을 할 때 무조건 기본값이 들어감. ?? 근데 왜 바뀌지
# 해당 인덱스에 값을 가록하면, 쓰레기값은 삭제됨

# arange() 함수
# 파이썬의 range() 함수와 같음
# 배열 생성시에 지정한 범위의 값들을 초기값으로  기록해 넣을 때 사용함
# 초기값, 종료값, 증가치 로 설정하면, 규칙에 따라 증가하는 수열을 만듦
har = np.arange(10)   # 10개를 가진 1차원배열 생성,  0 ~ 9 까지의 값들로 초기화함
print(har)

har2 = np.arange(3, 21, 2)
print(har2)

# linspace(), logspace() 함수
# linspace(시작값, 끝값, 구간갯수) : 나누어진 구간을 초기값으로 해서 배열생성
# logspace(시작값, 끝값, 구간갯수) : 구간 갯수만큼의 로그구간값을 초기값으로 해서 배열 생성
iar = np.linspace(0, 100, 5) # 0부터 100까지를 5구간으로 나눈 값
print(iar)

iar2 = np.logspace(0.1, 1, 10)
print(iar2)









