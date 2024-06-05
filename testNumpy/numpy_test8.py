# numpy_test8.py

import numpy as np

# 배열 연결
# 두 개 이상의 배열들을 연결(concatenate)해서 하나의 큰 배열을 만듦
# 사용함수 : hstack, vstack, dstack, r_, c_, tile

# hstack (horizental stack)
# 행의 갯수가 같은 2차원배열들을 옆으로(가로로, 수평) 합칠 때 사용 => 열 갯수가 늘어나게 됨
ar1 = np.ones((2,3))    # dtype 정의가 없으므로 float
print(ar1)
ar2 = np.zeros((2,2))
print(ar2)

print(np.hstack([ar1,ar2]))

# vstack (vertical stack)
# 열의 갯수가 같은 2차원배열들을 위아래로(세로로, 수직) 합칠 때 사용 => 행 갯수가 늘어나게 됨
bar1 = np.ones((2,3))
print(bar1)
bar2 = np.zeros((3,3))
print(bar2)
print(np.vstack([bar1,bar2]))

# dstack (depth stack)
# 행과 열이 같은 2차원배열 여러 개를 깊이(depth, z축, 채널) 방향으로 합칠 때 사용함
# a 행 x b 열 배열 갯수가 n개 합치면, 결과는 a면 x b행 x n열 이 됨
car1 = np.ones((3,4))   # 3행 4열
print(car1)
car2 = np.zeros((3,4))  # 3행 4열
print(car2)

car3 = np.dstack([car1,car2])
print(car3)
print(car3.shape) # 3면 4행 2열

# stack() 함수 : 기본적으로 dstack() 과 유사함
car4 = np.stack([car1,car2])    # 그냥 갖다 붙임
print(car4)
print(car4.shape)   # 2면 3행 4열
# a 행 x b열 배열 갯수가 n개 합치면, 결과는 n면 x a행 x b열 이 됨

car5 = np.stack([car1,car2], axis=1)  # 합쳐지는 갯수를 행위치에 적용하라는 뜻임 
print(car5)
print(car5.shape)   # 3면 2행 4열

# r_ : hstack 과 유사하게 좌우로 배열을 합침
# 함수 임에도 소괄호(parenthesis, ())를 사용하지 않고, 인덱싱처럼 대괄호(braket, [])를 사용함
# 특수메서드라고 함, 인덱서라고 함
# np.r_[배열생성구문 | 배열변수, 배열생성구문 | 배열변수, ......]
car6 = np.r_[np.array([1,2,3]), np.array([4,5,6])]
print(car6)

# c_: indexer 임
# 배열의 차원을 증가시킨 후, 좌우로 연결하는 인덱서임
# 1차원배열을 연결하면 2차원배열이 된다는 의미임 : 배열의 값 갯수가 행, 합쳐지는 배열 갯수가 열이 됨
car7 = np.c_[np.array([1,2,3]), np.array([4,5,6])]
print(car7)

# tile() 함수 : 배열을 지정한 횟수만큼 복사해서 연결함
# tile (배열변수, 열반복횟수), tile(배열변수, (행반복, 열반복))
dar = np.array([[1,2,3],[4,5,6]])   # 2행 3열
dar1 = np.tile(dar, 2)
print(dar1)     # 각 행의 열이 2번 반복됨 => 2행 6열이 됨

dar2 = np.tile(dar,(3,2))   # 행으로 3번 열로 2번
print(dar2) # 6행 6열이 됨

# 2차원 그리드 포인트 생성
# 변수가 2개인 2차원 함수 그래프를 그리거나 표를 작성하려면,
# 2차원 영역에 대한 (x, y) 좌표값 쌍, 즉 그리드 포인트(grid point)가 필요함
# meshgrid() 함수로 x, y 좌표를 구성할 배열을 생성할 수 있음

# 예 : x 값이 0, 1, 2 이고, y값이 0, 1, 2, 3, 4 라면, meshgrid() 로 사각형 영역을 구성할 
# 가로축의 점들과 세로축의 점들을 조합해서 결과로 그리드 포인트의 x 행렬과 y행렬을 만들어 줌
x = np.arange(3)
print(x) # [0 1 2]
y = np.arange(5)
print(y) # [0 1 2 3 4]

metrix_X, metrix_Y = np.meshgrid(x,y)
print(metrix_X)
print('------------------')
print(metrix_Y)

# (x, y) 조합
grid_xy = [list(zip(x,y)) for x,y in zip(metrix_X,metrix_Y)]
print(grid_xy)


