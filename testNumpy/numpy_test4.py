# numpy_test4

import numpy as np

# 배열 슬라이싱
# 배열이 가진 원소(값)들을 일부 추출하는 것
# 파이썬 슬라이싱과 콤마(, )를 함께 사용하면 됨
ar = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(ar)
print('ar.shape : ', ar.shape)

# 인덱싱 : ar[0][2] == ar[0, 2]
# 슬라이싱 : 부분선택 시 콜론(:) 사용, 시작위치 : 끝위치
# 시작위치 생략은 처음부터를 의미(0), 끝위치 생략은 끝까지를 의미(마지막 인덱스)
# 끝 위치는 -1 한 위치까지를 의미
print(ar[0, :]) # 0행 전체열
print(ar[:, 1]) # 모든 행의 1열 값
print(ar[1, 1:])    # 1행의 1행부터 끝까지
print(ar[:2, :2])   # 0행, 1행의 0열, 1열의 값

# 인덱스 배열(indexed array) : 팬시 인덱싱(fancy indexing)
# 일반적인 값 추출을 위한 배열 인덱싱 : 배열변수[인덱스 숫자]
# numpy 가 제공하는 다른 표현의 배열 인덱싱 방식
# boolean 배열 인덱싱과 정수 배열 인덱싱 방식 2가지가 있음
# 인덱싱을 위한 별도의 배열을 만들어서 사용하는 방식임
# 주의 : 값을 가진 배열과 인덱싱 배열의 크기(갯수)가 같아야함

# 1. boolean 배열 인덱싱으로 배열값 추출
# True, False 로 배열을 만듦 : 추출할 인덱스에 True를 사용하는 방식
# 예 : 홀수번째 위치의 값들만 추출하는 경우
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
idxArray = np.array([True, False, True, False, True, False, True, False, True, False])
print(ar[idxArray])

# 벡터화 연산 또는 조건문 연산을 사용할 수도 있음
print(ar % 2)   # ar[0] % 2, ar[1] % 2 ... => [1 0 1 0 1 0 ...]
# 각 인덱스 위치의값을 2로 나눈 나머지들로 표현
print(ar % 2 == 0)   # ar[0] % 2 == 1, ar[1] % 2 == 0 ...
# => [True False True False True False...]
# 각 인덱스 위치의값을 2로 나눈 나머지가 0이면 True, 0이 아니면 False
print(ar[ar % 2 == 0])  # 백터화 연산을 인덱싱으로 사용

# 2. 정수 배열 인덱싱
# 인덱싱 배열을 만들 때, 추출할 위치의 인덱스 숫자를 배열로 구성
ar2 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idxArray2 = np.array([0, 2, 5, 7, 8])   # 골라낼 값에 대한 인덱스만 표기함
print(ar2[idxArray2])   # ar2[0], ar2[2], ar2[5], ar2[7], ar2[8]

# 정수 배열 인덱싱의 크기는 값 배열 크기와 같지 않아도 됨
# 값을 가진 배열보다 크기가 더 커도 됨
idxArray3 = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3]) # 15개
print(ar2[idxArray3])

# 배열 인덱싱은 다차원배열의 각 차원에 대해서도 적용할 수 있음
ar3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])   # 3행 4열
print(ar3)
print(ar3[:, [True, False, False, True]])
print(ar3[[2, 0, 1], :])    # 2행, 0행, 1행 순으로 열값 모두 추출
