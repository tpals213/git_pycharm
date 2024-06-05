# conditional\\ifMission1.py
# conditional.ifMission1
# if 문 실습문제
'''
키보드로 정수 2개를 입력받아서, 두 정수가 모두 양수일때만
합, 차, 곱, 몫(int), 나머지 를 계산해서 출력하시오.
입력 내용 :
 첫번째 정수 : 12 (num1 : int)
 두번째 정수 : 5 (num2 : int)
처리 내용 :
 조건 : 두 수 모두 양수이냐? (양수의 조건 : 값 > 0)
 양수가 맞을때만 사칙연산 계산해서 출력함
 둘 다 또는 하나만 0, 음수이면 처리할 내용이 없음
'''

def practice1():
    n1 = int(input('정수 입력 : '))
    n2 = int(input('정수 입력 : '))

    if n1 > 0 :
        if n2 > 0:
            print(f'합 : {n1 + n2}, 차 : {abs(n1 - n2)}, 곱 : {n1 * n2}, 목 : {int(n1/n2)}, 나머지 : {n1%n2}')
    else:
        print('두 정수는 모두 양수여야 합니다.')