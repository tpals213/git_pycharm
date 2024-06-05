# path : module\\sample_module.py
# module : module.sample_module
# 파이썬에서 모듈 만들어서 사용하기

# 모듈 (module) : 파이썬 소스 파일이다. (파일명.py)
# 파일명이 모듈명이 됨
# 모듈용 소스 파일에는 함수와 변수가 저장되면 됨
# 모듈이 제공하는 함수와 전역변수를 사용하려면, import 모듈명 으로 선선안 다음에
# 모듈명.함수명(), 모듈명.변수명으로 사용하면 됨

import keyword
# keyword.py 파일을 의미

print(keyword.kwlist)   # 예약어 리스트 출력됨

# 모듈은 다른 파이썬 파일에서 사용할 수 있도록 함수(기능) 와 변수 값들을 따로 저장해서
# 제공하는 목적의 소스 파일

# 모듈 임포트시에 모듈명에 대한 줄임말 같이 선언 가능
# import 모듈명 as 줄임말
import keyword as k

print(k.kwlist)
print(k.__file__) # 해당 모듈(파일)의 위치가 출력 됨
# help('modules')

# 파이썬이 제공하는 표준 모듈들 ------------------------------
import os   # 파일이나 디렉토리 관련 기능을 제공

print(os.getcwd())

import time # 날짜와 시간 관련 기능 제공

print(time.localtime()) # 현재 날짜와 시간 정보 출력
# time.sleep(1)   # 1초 멈춤
print(time.localtime())

import random

print(random.random())  # 0.0 <= random < 1.0
print(random.randint(1, 5))  # 1 <= random <= 5
print(random.randrange(1, 10, 2))   # 1<= 2 간격의 정수 < 10

import math # 수학 계산 관련 기능 제공

print('원주율 : ', math.pi)
print('5! : ', math.factorial(5))

import calendar

calendar.prmonth(2024,5)




# __name__ : 현재 실행되고 있는 모듈 이름 확인
print(__name__) # 현재 파일명 출력
# 프로그래을 실행하면 기본 파일은 main 모듈(파일)이 됨. 즉, main 만 실행할 수 있다는 의미

# ----------------------------------------------------------------
# 사용자 정의 모듈 사용하기
import mymodule as my

print('더하기 : ', my.sum(10, 20))
print('빼기 : ', my.sum(15, 7))
print('곱하기 : ', my.sum(15, 3))
print('나누기한 몫 : ', my.sum(12, 3))
print('나누기한 나머지 : ', my.sum(10, 20))

try:
    print('나누기한 나머지 : ', my.mod(12, 0))
except Exception as msg:
    print(msg)
    pass

print('가장 큰 값 : ', my.max())
print('가장 큰 값 : ', my.max(10))
print('가장 큰 값 : ', my.max(1, 84, 74, 9, 64, 87, 3, 48, 1557))

print('가장 큰 값 : ', my.min())
print('가장 큰 값 : ', my.min(10))
print('가장 큰 값 : ', my.min(1, 84, 74, 9, 64, 87, 3, 48, 1557))

print('글자 갯수 : ', my.strlen())
print('글자 갯수 : ', my.strlen('module test'))

print('원주율 : ', my.pi)
print('카운트 : ', my.count)












