# chap02_allocation.py

'''
파이썬에서의 변수 공간에 값 기록하는 메모리 할당(memory allocation) :
    파이썬에서의 변수 할당은 동적 할당임
    동적(Runtime 시 : 실행시) 메모리(RAM)에 변수 공간을 만들고 값을 기록
    코드 구문 :
        변수명 = 값
        변수명 = 계산식
    주의 사항 :
        변수명 (= 값이 없으면 에러, 할당이 안 된 상태)
'''

num = 1 + 2 # 계산 결과 3이 num 변수 공간에 기록 할당
print('num 변수가 가진 값 : ' , num)

# 변수 할당시 = (대입연산자) 사용
# 대입연산자는 반드시 왼쪽 변수, 오른쪽 값 또는 계산식
# 값 = 변수 # 에러
# 100 = a

# 한번에 여러 개의 변수에 값을 할당할 수도 있음
# x = 10
# y = 20
# z = 30
x, y, z = 10, 20, 30
print(x, y, z, sep=' | ') #sep(seperator) : 구분자 (출력값들을 구분할 기호)
# 10 | 20 | 30

# 한 개의 값을 여러 변수에 할당할 수도 있음
k = m = n = 77
print('k : ', k, 'm : ', m, 'n :', n, sep=', ')

# 한줄에(line) 에 여러 변수 할당 구문을 작성한다면 세미콜론(;)으로 구분
# num1 = 12
# num2 = 24
num1= 12; num2= 13; num3= 14
print('num1 : ', num1, 'num2 : ', num2, 'num3 : ', num3, sep=', ')

# 두 변수의 값 교환
first = 123
second = 456
print('first : ', first, 'second : ', second)

first, second = second, first
print('first : ', first, 'second : ', second)

# =(순수대입연산자)
# 복합대입 연산자 : 산술대입연산자가 주로 사용
# 파이썬의 산술연산자 : +, -, *, /, %, **, //
# +=, -=, *=, /=, %=, **=, //=
# 메모리의 변수 공간에 직접 연산하므로, 연산 처리 속도 빠름(사용 권장)
value = 100
print('value : ', value)

value += 10 # 10 증가 : value = value + 10 보다 빠름
print('value : ', value)

value -= 20
print('value : ', value)

value *= 5
print('value : ', value)

value = 100
value /= 10 # 나누기한 몫만 리턴, 결과형은 실수형(float)
print('value : ', value)

value = 100
value //= 10    # 나누기한 몫의 결과형이 정수
print('value : ', value)

value **=2
print('value : ', value)

# 파이썬 코드 문장은 한 줄에 작성이 원칙
# 문장이 길어서 한 줄 작성이 불편할 경우 여러줄로 나눌 수 있음
# 단, 문장이 끊어지는 부분에 반드시 백슬러시(\)를 표시
print('파이썬은 인터프피터\
언어이다\
스크립트 언어이기도 하다.\
한줄로 작성해야 한다.')
















