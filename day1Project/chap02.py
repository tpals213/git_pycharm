# chap02.py
# 식별자 : 개발자가 지어주는 이름
# 변수(variable) : 프로그램 구동시 메모리(RAM)에 값 기록하는 공간(방)
# 함수(fuction) : 반복 사용되는 코드를 분리 작성해서 이름 붙여준 것 (코드의 조각 코드들)
# 모듈(module) : 함수들을 따로 모아놓은 파일
# 클래스(class) : 파이썬은 객체 지향형 스크립트 언어임

# 파이썬의 이름 작성 규칙 (식별자 조건 : Naming Rule)
# 1. 대소문자 구분 : name != Name
NAME = '홍길동'
name = '이순신'
Name = '장세민'
print(NAME, name, Name)

# 2. 이름의 첫글자에 숫자 사용 불가 : 1num(에러)
# 1num = 100
# print(1num)

# 3. 이름의 첫글자는 문자 또는 _(underscore) 만 사용 가능
_score = 100.0
print(_score)

# 4. _를 제외한 기호문자, 공백 사용 불가
# num& = 12     # SyntaxError
# print(num&)

# 5. 이름의 중간 위치나 끝에 숫자 사용할 수 있음 : num1, first1_num
num1 = 10
num2 = 20
print(num1 > num2)   # False

# 6. 예약어 (프로그램 언어가 사용하기 위해서 별도로 정해 놓은 단어)는 이름으로 사용 불가
# True = 1    #error
true = 1    # ok
print(true)

# 파이썬이 제공하는 예약어 확인
# keyword 모듈에서 제공함 : import 해서 사용
import keyword

print(keyword.kwlist)   # 35개

# 파이썬에서 제공하는 내장함수 : 기본으로 제공됨
# 별도의 import 선언하지 않고 바로 사용함
# max, min, type, len, range, str, int, float, print, input 등의 함수들

# type(값 또는 변수명) : 값의 자료형 리턴

# len(값 또는 변수) : 길이(저장된 값의 갯수) 리턴
a = 'abcd'
b = [1, 2, 3, 4, 5]
print(len(a), len(b))   # 4, 5

# max(값들 또는 변수) : 최대값(가장 큰 값), min(값들 또는 변수) : 최소값(가장 작은 값)
print(max('abcdefg'))   #g
print(max('123456789')) #9
print(min('abcdefg'))   #a
print(min('123456789')) #1

# 주석
# 한 줄 주석
'''
여러 줄 주석
작은 또는 큰 따옴표를 앞뒤에 3개씩 표시
파이썬에서는 single quotation 과 double quotation 동일 취급
'''

print(abs(-10)) #10

# 파이썬에서는 변수는 반드시 값을 가져야 생성
# num # name 'num' is not defined
num = 12
print(num)

# 파이썬에서는 변수에 기록할 값의 종류(data type : 자료형)을 정하지 않음
# 자료형 변수명 = 기록할 값 => 자료형 = 기록할 값
# 변수방에 기록된 값에 따라 자료형이 정해짐 : 동적 할당
value = 100
print(value, type(value))

value = 'python'
print(value, type(value))

value = 3.14
print(value, type(value))

value = False
print(value, type(value))

# 변수 제거 : del 변수명
del value
# print (value, type(value)) #error

















