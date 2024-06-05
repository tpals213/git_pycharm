# numpy_test2.py
# numpy 는 ndarray 클래스 사용 : C언어로 만든 내부 로직 제공
# type 을 확인하면, 배열의 자료형은 numpy.ndarray
# ndarray : N - Dimensional Array 줄임말 (N차원 배열)
# 1차원부터 다차원배열 다룰 수 있음
import numpy
import numpy as np

# 2차원 배열 만들기
# 1차원 배열 여러 개 (값 갯수가 같아야 함)를 하나로 묶으면 => 2차원 배열
# 1차원 배열 == 백터(Vector)
# 2차원 배열 == 매트릭스(Matrix) : 행과 열로 구성된 행렬 형태
# [[...], [...], [...]] : list of list 형태
tar = np.array([[0, 1, 2], [3, 4, 5]])  # 2행3열 matrix
print(tar)
print(len(tar)) # 2 : 행 갯수
print(len(tar[0]))  # 3 : 0행 안의 값 갯수

# 2차원 배열의 각 값에 접근 : 배열변수[행순번][열순번]
# 행 (Row) : 세로방향(줄, 높이), 열 (Column) : 가로방향 (칸, 너비)
# 2중 for 문으로 각 인덱스 위치의 값을 처리함
for row_index in range(len(tar)):   # 0, 1
    for col_index in range(len(tar[row_index])):  # 0, 1, 2
        print('tar[{}][{}] : {}'.format(row_index, col_index, tar[row_index][col_index]))

# 3차원 배열 만들기
# 값의 종류가 같고, 행과 열 갯수가 같은 2차원 배열들의 묶음
# 면(깊이, depth), 행(줄, row), 열(칸, column) 로 구성됨 == Tensor (텐서) 라고 함
thar = numpy.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],  # 0면
                    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]) # 1면

print(thar) # 2면 3행 4열
print(len(thar))    # 면의 갯수
print(len(thar[0]))  # 0면의 갯수 == 행갯수 = 3행
print(len(thar[1]))  # 1면의 갯수 == 행갯수 = 3행
print(len(thar[0][0]))  # 4열

# 3차원배열 안의 각 값을 다루려면, 배열변수 [면순번][행순번][열순번]
# 3중 for 문 사용해야 함
for didx in range(0, len(thar)) :   # 면 반복 : 0, 1
    for ridx in range(0, len(thar[didx])) :  # 행 반복 : 0, 1, 2
        for cidx in range(0, len(thar[didx][ridx])) :  # 열 반복 : 0, 1, 2, 3
            print('thar[{}][{}][{}] : {}'.format(didx, ridx, cidx, thar[didx][ridx][cidx]))
        print()
    print('================================')

# 배열의 차원(ndim) 과 크기(shape) 알아내기
# 배열변수.ndim, 배열변수.shape
print(tar.ndim)
print(tar.shape)
print(thar.ndim)
print(thar.shape)

# 1차원 배열의 ndim, shape 확인
ar = np.array([1, 2, 3])
print(ar.ndim)
print(ar.shape)

# 배열의 인덱싱 : 값에 접근하기 위한 인덱스를 표시
# 1차원 배열의 인덱싱은 리스트와 같은
print('index 1 : ', ar[1])
print('뒤에서 부터 첫번째 : ', ar[-1])

# 2차원배열의 인덱싱 : 배열변수[행순번][열순번]
# 콤마(,)를 이용할 수도 있음 : 배열변수[행순번, 열순번] => 축(axis) 이라고 함
# 행(x축), 열(y축)이 됨
print('0행 0열의 값 : ', tar[0][0], tar[0, 0])
print('1행 0열의 값 : ', tar[1][0], tar[1, 0])
print('마지막행, 마지막열의 값 : ', tar[-1][-1], tar[-1, -1])