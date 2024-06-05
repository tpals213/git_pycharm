# chap02_input.py

# 파이썬에서 실행시 키보드 값 입력받기 : input() 함수 사용
# 변수 = input(안내문구)
# num = input() # input 은 무조건 스트링
# num = input('숫자 입력')
# print('num : ', num, type(num))

# 파이썬의 input()함수로 입력 들어오는 값은 모두 문자형(str)이다
# print('더하기 : ', num + 100)  # 숫자와 문자는 계산 불가

# 숫자형으로 바꾸고자 한다면
# 정수는 int('정수문자'), 실수는 float('실수문자') 함수 사용
# inum = int(num)
# print('inum : ', inum, type(inum))
# print('더하기 : ', inum + 100)

# 입력 예
# 정수 두 개 각각 입력 받아서, 사칙연산 결과 출력 처리
# first = int(input("Enter first name: "))
# second = int(input("Enter second name: "))
#
# print('first+second = ', first + second)
# print('first-second = ', first - second)
# print(f'{first} * {second} = {first * second}') # f'str' : format string
# print('{} / {} = {}'.format(first, second, first/second))   #format() 함수 이용
# # format() 함수와 순번(index)을 적용한 출력
# print('{0} // {1} = {2}'.format(first, second, first//second))
# print('{0} / {1} = {2: .2f}'.format(first, second, first/second))
# print(f'{first} ** {second} = {first**second}')

# 입력 연습
'''
신상정보를 입력받아, 각 변수에 저장하시오. 변수 이름은 임의 지정
이름(str), 나이(int), 성별(str, 남|여로 입력), 키(float), 몸무게(float)
각 변수의 값을 아래의 형식으로 출력하는 코드를 작성
홍길동은 27세 남자이고, 키는 178.5cm 몸무게는 72.0kg 입니다.
'''
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")
# height = float(input("Enter your height: "))
# weight = float(input("Enter your weight: "))
#
# print(f'{name}은/는 {age}세 {gender}자이고, 키는{height: .1f}cm 몸무게는{weight: .1f}kg 입니다.')

# 입력 연습
'''
키보드로 값을 입력 받아 요구 조건대로 처리하고 출력되게 코드 작성
기본값을 가진 변수 생성 할당
    total_point = 12500
입력 내용 : 
total_point = 12500
    고객 이름 : 황지니 (custom_name : str)
    결재 금액 : 3000000 ( price : int)
처리 내용 : 
    결재 금액의 5%를 포인트(point : float) 로 처리
    계산된 포인트를 누적포인트(total_point)에 증가 연산 처리
출력 내용
    황지니 고객님의 결재 금액은 3000000 원, 발생 포인트는 15000
    현재 이용하실 수 있는 누적 포인트는 162500 점입니다.
'''
# format() 사용
custom_name = input("Enter your name: ")
price = int(input("Enter your price: "))
point = price * 0.05
total_point = 12500 + point

print('{} 고객님의 결제 금액은 {} 원, 발생 포인트는 {}\
 현재 이용하실 수 있는 누적 포인트는 {} 점입니다.'\
      .format(custom_name, price, int(point), int(total_point)))

# f-string 포매팅 사용
print(f'{custom_name} 고객님의 결제 금액은 {price} 원, 발생 포인트는 {int(point)}\
 현재 이용하실 수 있는 누적 포인트는 {int(total_point)} 점입니다.')




