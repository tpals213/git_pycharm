# path 표현 : conditional\\ifSample.py
# module 표현 : conditional.ifSample

# 제어문 (조건문) : if 문, if else 문, if elif else 문 사용 테스트 스크립트

'''
제어문 종류 : 조건문, 반복문, 분기문
조건문 : 조건을 제시해서 결과가 참(True) 또는 거짓(False) 이 나오게끔 작성해서
            결과에 따라서 처리 내용을 선택 작동되게 하는 구문

반복문 : loop (루프, 반복되는 구간)가 있는 문장, 루프문 이라고도 함
            반복 실행할 구문을 원하는 횟수만큼 또는 종료 조건이 될 때 까지 반복 실행되게 작성하는 구문
            for 문, while문
분기문 : 실행 순서를 중간 생략하거나, 강제로 종료시키는 구문, 반복문 내에서만 사용 가능
            continue 문, break 문
'''

# 조건문에서는 조건식(표현식 : expression) 작성이 중요함
# 조건표현식(계산식)은 반드시 결과가 참 또는 거짓이 나오게끔 작성
# 비교, 논리 연산자 주로 사용됨

'''
if 조건식 :
    조건의 결과가 참일 때 실행 할 구문 (들여쓰기)
'''
# 조건식 작성형식 1 : if 만 사용하는 조건문 예
def test_if():
    #if(True):
    if(False) :
        print('if 조건이 참이면 실행')

    print('if 문이 종료되고 나서 실행')

    # if True :
    # print('test')   # IndentationError

# if 문의 족선식은 주로 값을 확인하거나, 값이 원하는 범위 안의 값인지 확인
# 입력받은 정수 숫자가 1이냐?
def test_if2():
    num = int(input('정수 입력 : '))
    if num == 1:
        print('num : ', num)

# 정수를 입력받아서 짝수인지 확인
# 짝수 : 2의 배수, 2로 나눈 나머지가 0
# 홀수 : 2의 배수 X, 2로 나눈 나머지가 1
def test_even():
    num = int(input('정수 입력 : '))
    k = num % 2
    if k == 0:
        print('num : ', num, '은 짝수입니다.')

# 조건문 작성형식 : if else 문
'''
if 조건식 : 
    참일 때 실해할 구문
    ...
else : 
    거짓일 때 실항할 구문
    ...
'''
def test_even2():
    num = int(input('정수 입력 : '))
    k = num % 2
    if k == 0 :
        print('num : ', num, '은 짝수입니다.')
    else :
        print('num : ', num, '은 홀수입니다.')

# 정수를 하나 입력받아서, 1~100 사이의 값이면 입력값의 제곱 출력
# 해당 범위의 값이 아니면, '1~100 사이의 값만 입력하세요' 출력
def test_range():
    n = int(input('정수 입력 : '))
    if(1 <= n <= 100) :
        print(n,'의 제곱은 : ', n**2)
    else :
        print('1~100 사의 값만 입력하시오')

# in 연산자 : 군집자료형 (list, tuple, set, dict, str) 에 사용
# 변수 또는 값 in 군집자료형 변수 : x in s => s 안에 x 가 있느냐
# x not in s => s 안에 x 가 없느냐
def test_in():
    print(2 in [1, 2, 3])   # True
    print(2 not in [1, 2, 3])   # False
    print('a' in 'abcdef')# True
    print('a' not in ('a', 'b', 'c'))   # False

# 결제 수단 중에 'money' 가 있으면, '5000원을 현금 지불하였습니다.' 출력
# 없으면, '다른 결제 수단을 선택하세요' 출력
def checkPayment():
    payment = ['money', 'card', 'mobile']
    price = 5000

    # if 'money' in payment:
    if 'bank' in payment:
        print(price, '원을 현금 지불하였습니다.')
    else :
        print('다른 결제 수단을 선택하세요.')

# 조건문 작성형식 3 : 다중 if 문
# if...elif...elif...else
# if...elif...elif...elif...
def checkPayment2():
    payment = ['결재수단', 'money', 'card', 'mobile', 'zeropay']

    print('========결재 수단 선택 ==========')
    print('1. 현금')
    print('2. 카드')
    print('3. 모바일')
    print('4. 제로페이')

    no = int(input('결재 수단 번호 선택 : '))
    price = int(input('결재할 금액 : '))

    if no == 1 :
        print(f'{price}원을 {payment[no]}로 지불하였습니다.')
    elif no == 2 :
        print(f'{price}원을 {payment[no]}로 지불하였습니다.')
    elif no == 3 :
        print(f'{price}원을 {payment[no]}로 지불하였습니다.')
    else :
        print(f'{price}원을 {payment[no]}로 지불하였습니다.')

# 중첩 if 문 : if 문 또는 else 문 안에 if 문 사용
def muli_if():
    n1 = 10
    n2 = 20

    if n1 == 10 :
        print(f'n1 : {n1}')
        if(n2 == 20):
            print(f'n2 : {n2}')
        else:
            print('n2는 20이 아닙니다.')

    else:
        print('n1은 10이 아닙니다.')

# 간단 if 문
# 변수 = 참일 때 실행할 값 if 조건식 else 거짓일 때 실행 값
def shortCondition():
    a = 1
    message = 'a is 1' if a == 1 else 'a is not 1'
    print(message)

def shortCondition2():
    score = int(input('점수 입력 : '))
    message = '합격' if score >= 60 else '불합격'
    print(message)




