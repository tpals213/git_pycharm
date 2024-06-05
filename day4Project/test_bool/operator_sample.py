# test_bool/operator_sample.py
# 모듈로 표현 : test_bool.operator_sample

# bool 자료형 확인
def func_bool():
    flag = True
    print('flag : ', flag, type(flag))

    flag = False
    print('flag : ', flag, type(flag))

    # 파이썬에서는 대소문자 구분
    # flag = true   # NameError

# bool() 함수 사용 : 값의 논리상태를 확인할 떄 사용
def func_bool2():
    print('result1 : ', bool('abcd'))   # True
    print('result2 : ', bool(''))   # False

    # 값이 저장되어 있는 지 , 비어 있는지 확인 용도
    print('result3 : ', bool({'a' : 1, 'b' : 2}))   # True
    print('result4 : ', bool({}))   # False

    print('result5 : ', bool([1, 2, 3, 4])) # True
    print('result6 : ', bool([]))   # False

    print('result7 : ', bool((1, 2, 3, 4))) # True
    print('result8 : ', bool(()))   # False

    print('result9 : ', bool(12))   # True
    print('result10 : ', bool(0))   # False


# 비교(관계) 연산자
# 2개의 값을 가지고 크냐(>, 초과), 작으냐(<. 미만), 같으냐(==), 같지않는(!=)
# 크거나 같으냐(>=, 이상), 작거나 같으냐(<=, 이하)
# 이항연산자 : 값1 연산자 값2
def func_compare():
    print('1 == 1 : ', 1 == 1)  # True
    print('1 == 2 : ', 1 == 2)  # False

    print('1 > 0 : ', 1 > 0)    # True
    print('1 < 2 : ', 1 < 2)    # True

    print('1 >= 1 : ', 1 >= 1)  # True
    print('1 != 1 : ', 1 != 1)  # True

# 논리 연산자 : 논리값(True, False) 을 계산에 사용하는 연산자
# and, or, not
def func_logical():
    a = 1
    b = 2

    print(a > 0 and b > 1)  # True and True => True
    print(a == 0 or b != 1) # False or True => True

    # and 연산자의 특징 :
    # 앞 and 뒤 : 앞이 False 이면 뒤를 실행 안 함
    # 앞이 True 이면 뒤를 실행함
    # 이 성질을 이용하는 짧은 조건문이 있음 (모든 스크립트에서 사용 가능)
    print('a' and 'b')  # 앞이 True 이므로 뒤를 실행 => 'b' 출력
    print('' and b) # 앞이 False 면 뒤를 실행 안함 => '' 출력

    # or 연산자의 특징 :
    # 앞 or 뒤 : 앞이 False 이면 뒤를 실행
    # 앞이 True 이면 뒤 실행 안함
    print('a' or 'b')   # a 출력



