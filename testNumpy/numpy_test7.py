# numpy_test7.py

import numpy as np

# 전치연산 : T 속성 사용함 => 2차원배열변수.T
# 2차원배열의 행과 열을 바꿀 때 사용함 : 2행3열.T => 3행2열이 됨
ar = np.array([[1, 2, 3], [4, 5, 6]])
print(ar)
print(ar.shape)     # (2,3)
print(ar.T)
print(ar.T.shape)   # (3,2)

# 1차원배열을 다차원배열로 바꿀 수 있음 : reshape() 함수 사용함 => 전체 크기(갯수)는 바뀌지 않음
ar = np.arange(12)  # 0 ~ 11 로 초기화됨 : 12개
print(ar)
print(len(ar))
# 3행4열의 2차원배열로 바꾸기
bar = ar.reshape(3,4)
print(bar)
print(len(bar) * len(bar[0])) # 3행 + 4열 => 12

# reshape() 사용시에 면, 행, 열의 갯수를 지원하지 않고 -1로 표기할 수도 있음
# -1로 표시된 항목은 계산
bar2= ar.reshape(3, -1)
print(bar2)
print(bar2.shape)

#1차원배열을 3차원배열로 바꾸기
bar3 = ar.reshape(2,2,-1)
print(bar3)
print(bar3.shape)

bar4 = ar.reshape(2, -1, 2)
print(bar4)
print(bar4.shape)

# flatten() 함수, ravel() 함수
# 다차원배열을 1차원배열로 바꿀 때 사용함
print('bar : ',bar.shape)   # bar : (3,4)
print('bar.flatten : ', bar.flatten()) # 2차원배열 => 1차원배열
print('bar.ravel : ', bar.ravel())

print('bar3 : ',bar3.shape)   # bar3 : (2,2,3)
print('bar3.flatten : ', bar3.flatten()) # 3차원배열 => 1차원배열
print('bar3.ravel : ', bar3.ravel())

# newaxis() 함수 
# 배열의 차원을 1증가 시키는 함수
# 1차원배열 => 2차원배열로, 2차원배열 -> 3차원배열로
# 값의 갯수가 5개인 1차원배열의 경우, 2차원 배열로 바꿀 때 (5, 1) 과 (1,5)로 변경 가능함
# 총 값의 갯수는 5개지만, 1차원배열과 2차원배열(1행, 5열)은 엄연히 다른 배열 객체임
xar = np.arange(5)  # 0 ~ 4 로 초기화 : 5개 1차원배열
print(xar)
print(xar.shape)
print(xar.reshape(1,5))
print(xar.reshape(5,1))

# 총 값의 갯수가 같은 배열에 대해 차원만 1증가시키는 경우, newaxis() 사용할 수 있음
print(xar[:,np.newaxis])   # 열이 행이 됨
print(xar[:,np.newaxis].shape)