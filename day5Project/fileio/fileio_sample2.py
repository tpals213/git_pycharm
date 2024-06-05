import os
import pickle

# 파이썬의 기본 파일 입출력은 텍스트 파일 입출력
# 텍스트가 아닌 자료형의 파일을 다룰때는 pickle 모듈 활용
# 바이너리(이진데이터 : binary) 형식의 파일로 저장
# 열기 모드 : wb, rb, ab 로 표기해야 함

def test_binary_fio():
    data = {1: 'python', 2: 'you need'}

    f = open('btest.dat', 'wb')
    pickle.dump(data, f)    # 파일에 딕셔너리 객체가 이진 데이터로 기록됨
    f.close()

def test_binary_fio2():
    f = open('btest.dat', 'rb')
    read_data = pickle.load(f)
    f.close()
    print(read_data)
    print(type(read_data))  # wb 는 객체 타입 그대로 기록함

# 표준 입출력을 파일로 대상을 변경 가능
# 표준 입력 : 키보드 입력 (컴퓨터 기본 입력 장치), sys.stdin 표현
# 표준 출력 : 모니터 출력 (컴퓨터 기본 출력 장치), sys.stdout 표현
import sys

def change_stdinout():
    # 시스템 표준 출력을 따로 변수에 저장함 (원래 상태로 되돌리기 위해 필요)
    stdout = sys.stdout

    f = open('test.txt', 'w', encoding='utf-8')
    sys.stdout = f   # 표준 출력을 파일로 바꿈
    print('표준 출력을 바꾸어 파일에 내용이 기록됨')
    f.close()

    sys.stdout = stdout
    print('콘솔에 출력 확인')

# os 모듈의 함수 사용
# 디렉토리 만들기 : mkdir(), 디렉토리 변경하기 : chdir()
# 사용자 계정 조회 : getlogin(), 현재 작업 디렉토리 조회 : getcwd()
# 시스템의 환경변수, 디렉토리, 파일 다룰 때 주로 이용함
def test_os():
    # listdir() : 해당 디렉토리 안의 파일과 하위 디렉토리 목록 조회
    print(os.listdir('.'))  # 현재 디렉토리
    print(os.listdir('../')) # 상위 디렉토리

    # rename() : 디렉토리나 파일의 이름 변경
    # os.rename('test.txt', 'sample.txt')
    print(os.listdir('.'))

    # path.exists() : 파일이나 디렉토리의 존재 여부 확인
    print(os.path.exists('example.txt'))    # 파일 없으면 False
    print(os.path.exists('sample.txt')) # 파일 있으면 True

    # path.abspath() : 파일이나 디렉토리의 절대 경로 조회
    # print(os.path.abspath('sample.txt'))
    # f = open(os.path.abspath('sample.txt'), 'a', encoding='utf-8')
    # f.write(os.path.abspath('sample.txt'))
    # f.close()

    # path.basename(), dirname(), split() : 파일명, 경로명, 두개 분리
    current_path = os.path.abspath('sample.txt')
    print('current_path : ', current_path)
    print('basename : ', os.path.basename(current_path))    # 파일명.확장자 추출
    print('dirname : ', os.path.dirname(current_path))  # 경로명만 추출
    print('split : ', os.path.split(current_path))  # ('경로명', '파일명.확장자') 분리

    # path.splitdrive(), path.splittext() : 경로에서 드라이브명만, 확장자만 추출
    print(os.path.splitdrive(current_path)) # ('드라이브명', '나머지경로') 분리
    print(os.path.splitext(current_path))   # ('경로명과 파일명', '.확장자') 분리

if __name__ == '__main__':
    # test_binary_fio()
    # test_binary_fio2()
    # change_stdinout()
    test_os()