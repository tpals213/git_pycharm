# path : exception\\mission.py
# 예외 처리 실습 문제

# 2단에서 9단까지의 구구단을 선택해서 한개의 단을 출력처리함
# 키보드로 출력할 단을 입력받아서 진행함
# 입력된 단수는 정수여야 함 (예외처리)
# 입력된 단수는  2~ 9 사이의 값이여야 구구단 출력됨
# 입력된 단수가 2보다 작으면 단수는 2로 처리함
# 입력된 단수가 9보다 크면 단수는 9로 처리함
# try: except: else: finally: 형식으로 작성함

def gugudan():
    try:
        x = int(input("출력할 단을 입력하세요 : "))
    except ValueError:
        print('숫자를 입력하세요')
    else :
        if x < 2:
            print('2보다 큰 숫자를 입력하세요, 2단을 출력합니다.')
            x = 2
        elif x > 9:
            print('9보다 작은 숫자를 입력하세요, 9단을 출력합니다.')
            x = 9
        for i in range(1, 10):
            print(f'{x} * {i} = {x * i}')
    finally:
        print('프로그램 종료')


if __name__ == "__main__":
    gugudan()