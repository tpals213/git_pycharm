# path : function\\func_sample.py

# 파이썬에서 함수 만들어 사용하기

'''
함수란, 반복 사용되는 소스 코드를 별도로 분리 작성해서 이름 붙인 것
- 파이썬 함수 만들기
def 함수명(매개변수) :     -> 매개변수(parameter) : 0 ~ n 개
    함수가 실행할 코드 구문들
    ...
    :return 값 또는 변수 또는 값, 값 , ... , 값 여러 개 => 받는 변수는 튜플임

- 함수의 사용 : 함수 호출(function call) 이라고 함
   함수가 만들어진 형태(signature)에 맞춰서 사용해야 함
   => 함수 이름 (대소문자 주의, _ 갯수 확인),
   => 매개변수의 갯수 일치되게 전달인자(argument) 사용해야 함
   => 반환값 여부도 확인
        반환값 있는 함수는 함수(중첩 함수()) 로 사용 가능함
'''

# 아무런 기능이 없는 (처리할 코드가 준비중인) 빈 함수를 만들 때는 pass 사용
def func():
    pass

def func153():
    None

# 함수 이름 아래에 함수 설명(description)을 적어둘 수 있음, 따옴표 사용
def hello():
    '이 함수는 ~~~ 기능 이며 작성 연습용입니다.'
    print('Welcome!')
    print('함수명에 공백, 예약어 사용 불가')
    return # 반환값 없는 리턴은 생략해도 됨

# 매개변수 있고, 반환값 있는 함수 작성
def add(x, y):
    print(f'x : {x} , y : {y}')
    return x + y

# 파이썬에서는 여러 개의 값을 리턴할 수 있음, 자동 tuple 로 처리
def func2(a, b):
    print(f'a : {a} , b : {b}')
    return a * 2, b * 2

# 함수 실행
# if __name__ == '__main__':
    # func()
    # func153()
    # hello()
    # 함수 설명(description) 을 확인할 때 help(함수명) 사용
    # help(hello)
    # help(input)
    # help(print)

    # 매개변수 있고 반환값 있는 함수 사용(call)
    # 반환값 받는 변수 = 함수명(매개변수에게 줄 값, 전달 인자)
    # result = add(10, 20)
    # print(f'result : {result}')
    #
    # result2 = add(1.3, 4.5)
    # print(f'result2 : {result2}')

    # result3 = func2(11, 22)
    # print(result3, type(result3))
    #
    # n1, n2 = func2(3.3, 4.4)
    # print(n1, n2)

# ----------------------------------------------------
# 변수 생성과 사용 영역 (지역, 스코프)
# 지역변수(Local Variable)와 전역변수(Global Variable)

def func1():
    num = 10    # 함수 안에서 만들어진 변수 : 지역변수
    print(f'num : {num}')

# 함수 밖에서 지역 변수 사용 못 함
# print(f'num : {num}')
gnum = 100  # 전역변수
print(f'gnum : {gnum}')

def func_global():
    # print(f'gnum : {gnum}') # 전역변수 선언 다음 위치에서는 어디서나 전역변수 사용 가능
    # 파이썬에서는 변수 = 값 구문은 새로운 변수 생성(할당)임

    global gnum# 전역변수 사용을 선언하는 구문을 먼저 작성해야함
    gnum = 200  # 새로 만든 지역 변수임 => 전역변수 gnum 의 값을 변경하는 구문이 되려면
    print(f'전역변수 gnum : {gnum}')

# 함수의 매개변수(parameter)는 전달받은 값 변경 불가
# 전달 받은 값이 군집 자료형일 때는 아이템(요소)는 변경할 수 있음
def list_func(plist):
    print('plist 가 받은 주소 : ', id(plist))
    print('before : ', plist)
    plist[1] = 10
    print('after : ', plist)

if __name__ == '__main__':
    # func1()
    func_global()
    print(f'전역변수 gnum : {gnum}')
    lst = [1, 2, 3]
    print('lst 가 참조하는 리스트 객체의 주소 : ', id(lst))
    print('lst', lst)
    list_func(lst)
    print('plist가 받은 주소 : ', id(lst))