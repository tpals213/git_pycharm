# path : function\\func_lambda.py

# 파이썬에서 람다함수 만들어 사용

'''
리스트 내포(list in for), 간단 조건문처럼 여러 줄로 된 코드를 간결하게 표현할 수 있는 새로운 함수 정의 방법
def 로 정의하는 함수를 간단하게 lambda 로 작성
한 줄로 표현 가능한 처리 내용일 때 주로 이용함 => 일회성 코드일 때 이용
함수 이름 없음, 참조변수가 함수명을 대신할 수는 있음

작성과 사용법 :
작성 :
참조변수 = lambda 매개변수, 매개변수: 처리구문
사용 1:
참조변수(전달값, 전달값)
사용 2:
(lambda 매개변수, 매개변수: 처리구문)(전달값, 전달값)
'''

# 일반함수
def add(x, y):
    return x + y

# 람다함수
add2 = lambda x, y: x + y

if __name__ == '__main__':
    # 일반함수 사용
    result = add(2, 3)
    print('결과 : ', result)

    # 람다함수
    result = add2(20, 30)
    print('람다 확인 : ', result)

    # 람다는 주로 작성과 실행을 함께 처리하는 방식으로 사용됨
    print('더하기 결과 :', (lambda x, y: x + y)(11, 22))

    # 람다함수의 매개변수에도 기본, 키워드, 가변 매개변수 적용 가능
    print('(기본)더하기 결과 :', (lambda x, y = 20 : x + y)(11))
    print('(키워드)더하기 결과 :', (lambda x, y: x + y)(x = 11, y = 22))
    print('(가변)더하기 결과 :', (lambda x, *y: x * y)(3, 1, 2, 3))

    # 람다함수 안에 간단 조건문 사용 가능
    print((lambda x, y : x if x % 2 == 0 else y)(3, 5))





