# path : module\\mymodule.py
# module : module.mymodule
# 사용자 정의 모듈


# 함수와 변수들을 작성 => 저장해 놓고 다른 파일에서 사용하려는 목적의 파일임
# 실행 코드는 포함하지 않는다.
# 장점 1 : 소스 코드 중복 작성을 줄일 수 있음
# 장점 2 : 유지 보수가 편함
# 장점 3 : 애플리케이션 구조 설정이 편해짐

# (전역) 변수
pi = 3.14159
count  = 10

# 함수
def sum(a, b):
    '두 수를 전달 받아서 더하기 결과 리턴'
    return a + b

def sub(a, b):
    '두 수를 전달 받아서 빼기 결과 리턴'
    return a - b

def mul(a, b):
   '두 수를 전달 받아서 곱하기 결과 리턴'
   return a * b

def div(a, b):
    '두 수를 전달 받아서 몫 결과 리턴, 나눌 수가 0이면 Exception 발생시킴'
    if a == 0:
        raise Exception('0으로 나눌 수 없습니다.')
    return a / b

def mod(a, b):
    '두 수를 전달 받아서 몫 결과 리턴, 나눌 수가 0이면 Exception 발생시킴'
    if a == 0:
        raise Exception('0으로 나눌 수 없습니다.')
    return a % b

def max(*args):
    '가변 매개변수를 사용해서 전달 받은 수들 중 가장 큰 값을 리턴'
    try:
        max_value = args[0]
        for data in args:
            if max_value > data:
                max_value = data

    except:
        print('처리할 데이터 X')


def min(*args):
    '가변 매개변수를 사용해서 전달 받은 수들 중 가장 큰 값을 리턴'
    try:
        min_value = args[0]
        for data in args:
            if min_value > data:
                min_value = data

    except:
        print('처리할 데이터 X')

def strlen(st = None):
    '문자열을 전달 받아서 글자 갯수 리턴'
    stlen = 0
    if st != None:
        for ch in st :
            stlen += 1
    return stlen




