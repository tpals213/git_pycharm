# path : function\\func_lambda2.py
# 람다함수를 이용하는 파이썬 내장함수 사용 테스트

# map 내장함수 :
# 맵객체변수 = map(실행할 함수명, 시퀀스객체)
# 시퀀스(Sequence) 객체 : 값을 순차적으로 저장하는 객체, 리스트나 튜플이 해당됨
# 시퀀스 객체의 각 요소값을 하나씩 꺼내서 함수로 보내고, 처리결과를 리턴 받아서 맵객체에 저장하는 함수
def func(x):
    return x * x

def test_map():
    lst = [1, 2, 3, 4, 5]
    m = map(func, lst)
    print(m, type(m))   # 맵참조변수 출력 : 참조객체 타입과 16진수 주소(id)가 출력
    print(list(m))  # 맵참조변수가 가진 값들 출력

    # 함수명 대신에 람다함수로 작성을 바꾼다면
    m = map((lambda x: x * x), lst)
    print(list(m))

    # 람다는 코드를 간결하게 표현하는게 목적
    # 위의 코드를 한줄로 표현한다면
    print(list(map((lambda x: x * x), [1, 2, 3, 4, 5])))

# ----------------------------------------------------------

# filter 내장 함수 :
# 필터결과객체 = filter(실행할 함수명, 시퀀스 객체)
# 시퀀스 객체의 각 요소의 값에 대해 함수 처리 결과가 참(True)인 요소만 골라서 저장하는 함수
def func1(x):
    return x > 2

def test_filter():
    nlist = [1, -2, 5, 6, 4]
    f = filter(func1, nlist)
    print(f, type(f))
    print(list(f))

    # 람다로 한줄로 코드 줄인다면
    f = filter((lambda x: x > 2), nlist)
    print(list(f))

    # 람다로 한줄로 코드를 줄인다면
    print(list(filter((lambda x: x > 2), [-1, 2, 4, 7])))

# --------------------------------------------------------------

# sorted() 내장 함수 : 정렬 함수
# 시퀀스에 저장된 복잡한 개게를 정렬할 때 사용하는 함수
# 정렬객체변수 = sorted(정렬할 시퀀스 객체, key=정렬에 사용할 키, reverse=True | False(기본값)

import operator

def test_sorted():
    students = [('김영희', 'A', 95), ('홍철수', 'B', 96), ('이길동', 'C', 90)]
    print(students)
    print(sorted(students)) # 키 지정 누락 시 자동 각 아이템의 [0]번째가 키로 지정 됨
    print(sorted(students, key=lambda x: x[1])) # 각 아이템의 [1]번째가 정렬의 키가 됨
    print(sorted(students, key=lambda x: x[2])) # 각 아이템의 [2]번째가 정렬의 키가 됨

    # sorted () 키 지정시
    # 파이썬이 제공하는 operator 모듈 사용 가능
    print(sorted(students, key=operator.itemgetter(2))) # [2]번째가 정렬의 키가 됨

    # 내림차순정렬 : reverse = True 로 지정함
    # 점수 기준 내림차순 정렬
    print(sorted(students, key=operator.itemgetter(2), reverse=True))

# -----------------------------------------------------------

# 리스트 내포와 람다함수
# 구구단 2단부터 9단까지 곱하기한 결과만 리스트에 저장 처리
def list_lambda():
    print([dan*su for dan in range(2, 10) for su in range(1, 10)])
    print([(lambda x, y : x*y)(x, y) for x in range(2, 10) for y in range(1, 10)])   #람다









if __name__ == '__main__':
    # test_map()
    # test_filter()
    # test_sorted()
    list_lambda()