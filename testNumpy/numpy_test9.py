# numpy_test9.py

import numpy as np

# 배열 간의 연산 : 백터화 연산
# 백터화 연산을 사용하면, 반복문을 쓰지 않고 배열 각 원소에 대한 연산 가능함
# 또 다른 장점은 선형대수 공식과 동일한 연산을 간단하게 작성할 수 있음

x = np.arange(1, 10001)  # 1만개 ( 1 ~ 10000 초기화 )
y = np.arange(10001, 20001) # 1만개 ( 10001 ~ 20000 초기화 )
z = np.zeros_like(x)  # 1만개 , 0으로 초기화

# 배열에 대한 백터화 연산을 사용하지 않으면 반복문으로 각 원소에 대한 연산 처리해야 함
z[0] = x[0] + y[0]  # 1만번 반복 실행
for i in range(10000):  # i : 0 ~ 9999
    z[i] = x[i] + y[i]

print(z[:10])       # 슬라이싱 : 0 ~ 9 까지 10개의 결과 출력

# 산술연산, 비교연산, 논리연산 모두 백터화연산 가능함
ar = np.array([1,2,3,4])
br = np.array([4,2,2,4])
print(ar + br)
print(ar - br)
print(ar * br)
print(ar / br)
print(ar == br)   # ar[0] == br[0] => 결과값 : True, False => [False True False True]
print(ar >= br)   # ar[0] == br[0] => 결과값 : True, False => [False True True True]

# 만약, 배열 각 인덱스 값끼리 하나씩 비교한 결과가 아니라,
# 배열의 모든 요소가 다 같은지 알고 싶다면 all() 을 사용하면 됨
cr = np.array([1,2,3,4])

print(np.all(ar == br))     # False
print(np.all(ar == cr))     # True

# 지수함수(exp), 로그함수(log) 등 수학 함수들도 백터화 연산을 지원함
dr = np.arange(5)
print(dr)
print(np.exp(dr))   # exp 함수 : 지수 e의 x제곱을 구하는 함수

print(10 ** dr) # 10 의 제곱
print(np.log(dr + 1))

# 스칼라와 백터 / 행렬의 곱셈
x = np.array(10)
print(x)
print(100 * x)

y = np.arange(12).reshape(3, 4)
print(y)
print(100 * y)

# 브로드 캐스팅 (broadcasting)
# 백터(행렬, 2차원배열)끼리 덧셈, 또는 뺄셈을 하려면 행과 열의 갯수가 같아야 함 (원칙)
# numpy에서 행과 열이 다른 백터끼리도 연산이 가능하도록 지원 => 이 기능을 브로드캐스팅
# 크기가 작은 백터가 자동으로 크기가 큰 백터의 행과 열 갯수와 맞춰짐

# 확인 1 :
x = np.arange(5)
print(x)
y = np.ones_like(x)
print(y)

print(x + y)
print(x + 1)

# 다차원에도 적용
dx = np.vstack([range(7)[i:i + 3] for i in range(5)])  # 리스트 내포
print(dx)
dy = np.arange(5)[:, np.newaxis]    # 열이 행이 됨, 차원 1증가 처리
print(dy)

# 행과 열 갯수가 다른 경우
print(dx + dy)  # 열 갯수가 다른 2차원 배열 더하기 연산 : 브로드 캐스팅 적용

# 차원 축소 연산
# 배열의 가로 행(줄) 또는 세로 열(칸) 전체를 하나의 값으로 보고 연산해서
# 하나의 결과를 만드는 것을 축소 연산(demension reduction)
# 1차원 배열은 축소연산의 결과는 값 1개
# 2차원 배열은 축소연산의 결과가 1차원 배열이 됨
# 사용되는 함수 : max(최대값), min(최소값), argmax(최대값의 index), argmin(최소값의 index)
# sum(합계), mean(평균), median(중간값), std(표준편차), var(분산)
# boolean 값 : all, any

x = np.array([1, 2, 3, 4])
print(x)
print(np.sum(x))    # 10
print(x.sum())    # 10

x2 = np.array([1, 3, 2])
print(x2.min()) # 1
print(x2.max()) # 3
print(x2.argmin()) # 최소값의 위치 : 0
print(x2.argmax()) # 최대값의 위치 : 1

x3 = np.array([1, 2, 3, 1])
print(x3.mean())    # 평균 : 1.75
print(np.median(x3))  # 중위값 : 1.5   (최소와 최대의 중간값)

print(np.all([True, True, False]))  # False
print(np.any([True, True, False]))  # True

ar = np.zeros((100, 100), dtype=np.int_)
print(ar)
print(np.any(ar != 0))  # False, 배열 안에 0이 아닌 값이 하나라도 있느냐?
print(np.all(ar == ar)) # True, 배열의 각 인덱스의 값들이 모두 같느냐?

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])

print(((a <= b) & (b <= c)).all())  # True
# (a <= b) : [True, True, True, True]
# (b <= c) : [True, True, True, True]
# & : [True, True, True, True].all() => True

# 정렬 sort()
# 1차원 배열은 값들의 오름 | 내림차순 정렬
# 2창원 배열은 행별(가로값들)로 정렬, 열별(세로값들)로 정렬을 함(axis 인수 사용)
# axis = 0 : 열별로 정렬, axis=1 | -1 (기본값) : 행별로 정렬
dar = np.array([[4, 3, 5, 7], [1, 12, 11, 9], [2, 15, 1, 14]])
print(dar)
print(np.sort(dar))
print(np.sort(dar, axis=0))

# 정렬하면 해당 배열의 구조를 바꿈 : 사용시 주의 필요
dar.sort(axis=1)
print(dar)

# argsort() 함수
# 데이터를 정렬한 다음, 인덱스를 출력함
ear = np.array([42, 38, 12, 25])
print(ear)
far = np.argsort(ear)   # 정렬한 후의 index 리턴
print(far)
print(ear[far]) # 정렬된 index 를 인덱서로 이용
print(np.sort(ear))




