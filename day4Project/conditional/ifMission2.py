# conditional\\ifelseMission2.py
# conditional.ifelseMission2
# if else 실습문제
'''
키보드로 나눌값과 나누기할 수를 입력받아 계산해서 출력하시오.
입력 내용 :
 나눌 값 : 25 (value : int)
 나누기할 수 : 0 (div_num : int)
처리 내용 :
 조건 처리 : 나누기할 수가 0 이 아니면 계산해서 몫과 나머지 출력함
          나누기할 수가 0이면 '0으로 나눌 수 없습니다.' 출력
마지막 출력구문 : if 문과 별개의 구문
 프로그램이 종료되었습니다.
'''

def practice1():
    n1 = int(input('나눌 값 : '))
    n2 = int(input('나누기할 수 : '))

    if n2 == 0 :
        print('0으로 나눌 수 없습니다.')
    else :
        print(f'몫 : {int(n1/n2)}, 나머지 : {n1%n2}')
    print('프로그램이 종료되었습니다.')
