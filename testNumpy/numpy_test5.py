# numpy_test5.py

import numpy as np

# 배열 생성시에 array() 함수 사용
# array() 함수 사용시 dtype 매개변수를 이용해서, 배열에 저장되는 값의 종류를 명시할 수도 있음
# dtype 을 사용하지 않으면, 자동으로 기록되는 값의 자료형이 저장됨
x1 = np.array([1,2,3])
print(x1.dtype) # int32 => 정수(integer) 32비트 => 4바이트 정수 (파이썬 정수 기본형)
print(type(x1))

x2 = np.array([1.0,2.0,3.0])
print(x2.dtype) # float64 => 실수(integer) 64비트 => 8바이트 실수 (파이썬 실수 기본형)
print(type(x2))


x3 = np.array([1,2,3.0])   # 같은 종류가 되기 위해 정수가 실수로 자동 형변환됨
print(x3.dtype)
print(x3)

#배열 생성시 dtype 인수에 자료형일 지정할 경우
# 제공되는 접두사 뒤에 바이트(또는 비트)수를 지정함 ex > int32, float64
# 문자타입 (char type) 접두사 뒤에는 글자수를 지정할 수 있음
# b : boolean
# i : integer
# f : float
# u : unsigned int (부호없는 정수 : 음수를 양수로 변환한 정수, ex > -128 ~ 127 => unsigned 하면 0 ~255)
# 0 ~ 127 그대로 두고, -128 ~ -1 을 127 뒤에 붙임, 0 ~ 127, -128 ~ -1 => -128은 128이 됨, -1이 255가됨
# c : 복소수 (complex)
# O : Object
# S : String (바이트문자열), 1byte : 1글자
# U : Unicode string (유니코드문자열), 2byte : 1글자
# 사용예 : i8 (정수8바이트 : 64비트), f8 (실수8바이트), U24(유니코드문자 24글자)
x4 = np.array([1,2,3], dtype = 'f')
print(x4.dtype)         # float 32
print(x4)
print(x4[0] + x4[1])  # float + float => float : 3.0

x5 = np.array([1, 2, 3], dtype = 'U')
print(x5.dtype) #  <U1 : 유니코드문자 1글자
print(x5)
print(x5[0] + x5[1])    # '1' + '2' => 문자합치기 : '12'

# inf 와 nan
# numpy 에서 무한대를 표현하기 위해 np.inf (infinity 줄임말) 와
# 정의할 수 없는 숫자를 표현하기 위해 np.nan (not a number 줄임말) 을 제공함
# 적용 예 : 1을 0으로 나누려고 하거나, 0에 대한 로그값 계산하면 무한대인 np.inf
# 0을 0으로 나누기하면 np.nan이 표시됨

print(np.array([0, 1, -1, 0]) / np.array([1, 0, 0, 0])) # [0 inf -inf nan] RuntimeWarning 발생
print(np.log(0))    # -inf
print(np.exp(-np.inf))      # 0.0 으로 바꿈


