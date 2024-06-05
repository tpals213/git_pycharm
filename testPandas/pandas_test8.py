# pandas_test8.py

import pandas as pd
import numpy as np

# 데이터프레임 인덱스 조작
# 인덱스 라벨이 없는 데이터프레임에 인덱스 라벨을 설정하거나 제거하는 것
# 행 인덱스와 열 인덱스를 서로 바꿔야 할 때도 인덱스 조작 가능 (인덱스 교환)
# set_index() 함수 : 기존의 행 인덱스를 제거하고, 데이터 열 중에서 하나를 행 인덱스로 설정할 때 사용
#                            한 컬럼의 값들 => 행 인덱스 라벨이 됨
# reset_index() 함수 : 기존의 행 인덱스를 제거하고, 인덱스를 데이터 열로 추가
#                               행 인덱스 라벨 => 한 컬럼의 값들로 바뀜

np.random.seed(0)
df1 = pd.DataFrame(np.vstack([list('ABCDE'),
                               np.round(np.random.rand(3, 5), 2)]).T,
                               columns=["C1", "C2", "C3", "C4"])
print(df1)

# set_index() 함수
# 기존의 행 인덱스(0, 1, 2, 3, 4) 는 지우고 특정 열 데이터를 행 인덱스 라벨로 지정
df2 = df1.set_index('C1')   # 'C1' 컬럼을 행 인덱스 라벨로 지정
print(df2)

print(df2.set_index('C2'))

# reset_index() 함수
# 기존의 행 인데스 라벨을 컬럼 값으로 바꿈
print(df2.reset_index())

# drop = True 인수 설정 시 행 인덱스로 변경된 열이 원래 컬럼으로 돌아오지 않고 지워짐
print(df2.reset_index(drop=True))

# 다중 인덱스 --------------------------------------
# 행이나 열에 여러 계층의 인덱스가 있을 때
# 데이터 프레임 생성 시, columns 인수에 리스트의 리스트(행렬)로 인덱스 설정한 경우
np.random.seed(0)
df3 = pd.DataFrame(np.round(np.random.randn(5, 4), 2),
                               columns=[['A', 'A', 'B', 'B'], ['C1', 'C2', 'C3', 'C4']])
print(df3)

# columns_names 속성
# 다중 인덱스에 이름 지정 시 사용함, 이름들은 리스트로 설정함
df3.columns.names = ['Cidx1', 'Cidx2']
print(df3)

# 행 인덱스도 다중 인덱스로 설정할 수 있음, 이름도 지정할 수 있음(index.names 사용)
np.random.seed(0)
df4 = pd.DataFrame(np.round( np.random.randn(6, 4), 2),
                   columns=[['A', 'A', 'B', 'B'], ['C1', 'C2', 'C3', 'C4']],
                   index=[['M', 'M', 'M', 'F', 'F', 'F'], ['id_' + str(i + 1) for i in range(3)] * 2])
df4.columns.names = ['Cidx1', 'Cidx2']
df4.index.names=['Ridx1', 'Ridx2']
print(df4)

# 행 인덱스와 열 인덱스 교환 : stack, unstack 사용
# stack() : 열 인덱스 ---> 행 인덱스로 변환
print(df4.stack('Cidx1'))   # 인덱스 이름 사용

# unstack() : 행 인데스 --> 열 인덱스로 변환
print(df4.unstack('Ridx2'))

# 인덱스 이름이 없으면 인덱스 정수를 사용해도 됨
print(df4.unstack(0))




