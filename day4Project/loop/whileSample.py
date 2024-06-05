# path : loop/whileSample.py

# while 문 사용 테스트 스크립트

'''
while 반복에 대한 조건식 :
    반복 실행 구문

반복에 대한 조건식은 무한 루프가 되지 않게 작성
만약, True 를 사용했다면, 반드시 while 안에 종료에 대한 조건처리 구문 있어야함
if 종료조건:
    break
'''
def test_while():
    num = 5
    while num > 0:
        print(num)
        num -= 1

# 반복 횟수가 정해지지 않은 경우 while 문 주로 사용
# 문자 하나 입력 받아서, 그 문자의 유니코드를 출력하는 처리 반복
# 단, '0' 이 입력 되면 반복 종료
def print_unicode():
    s = input('문자 입력 : ')

    while s != '0':
        print(f'{s}의 유니코드 : {ord(s)}')
        s = input('문자 입력 : ')

def print_unicode2():
    while True:
        s = input('문자 입력 : ')
        if s != '0':
            print(f'{s}의 유니 코드 : {ord(s)}')
        else :
            break

# 파이썬에서는 여러 줄의 문자열 값을 표현할 때 3쌍의 따옴표를 이용
def display_menu():
    prompt = '''
        *** 원하는 메뉴를 선택하세요. ***
        1. 추가
        2. 삭제
        3. 출력
        4. 종료
    '''
    # print(prompt)

    while True:
        print(prompt)

        i = int(input('번호 입력 : '))
        if i == 4:
            print('프로그램을 종료 합니다.')
            break
        elif i == 1:
            print('추가')
        elif i == 2:
            print('삭제')
        elif i == 3:
            print('출력')
            
    print('------- END -------')
# 이 파이썬 스크립트 파일을 실행 파일로 만들고자 한다면, 아래쪽에 main 코드 추가
if __name__ == '__main__':
    display_menu()

