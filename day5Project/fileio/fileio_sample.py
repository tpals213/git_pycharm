# path : fileio\\fileio_sample.py
# module : fileio.fileio_sample

# 파이썬에서의 파일 입출력 처리
# open() --> write() or read() --> close()

'''
파일 변수 = open('디렉토리명\\파일명.확장자', '열기모드')
파일 입출력의 기본은 텍스트(문자)파일 입출력
열기모드 :
w(wt), x(xt) : 새로 쓰기
    - w(wt) : 대상 파일이 없으면 파일을 자동으로 새로 만들어서 열기함
                  대상 파일이 있으면, 파일 안의 내용을 모두 지우고 새로 쓰기 상태로 열기
    - x(xt) : 대상 파일이 없을 때 파일을 자동으로 새로 만들어서 열기함
                  대상 파일이 있으면 에러
    - r(rt) : 읽기 전용
    - a(at) : append - 추가 쓰기
                 대상 파일이 없으면 파일을 자동으로 새로 만들어서 열기
                 대상 파일이 있으면, 파일 안의 내용을 그대로 두고 열기
'''

# 파일을 새로 만들고 값 기록 저장
import os

def test_fwrite():
    # f = open('testa.txt', 'w')  # 기본 경로는 현재 폴더 아래 저장
    f = open('testa.txt', 'w', encoding='utf-8')
    f.write('test file write running.')
    f.write('12345')
    f.write('파일에 저장 확인!')   # 텍스트 파일 인코딩이 'ms949' 문자셋임
    f.write('＃＃＃＃＃＃＃＃＃＃')
    # 파일 open 시 인코딩 문자셋 지정하면 해결 됨
    f.close()

    # os 모듈을 활용하면 현재 작업중인 디렉토리 경로 확인 가능
    print(os.getcwd())

# 원하는 디렉토리(폴더)에 파일을 만드려면
# open() 함수 첫번째 인자에 전체 경로명과 파일명을 함께 입력하면 됨
# 경로(path)는 백슬러시(\) 이스케이프 문자를 반드시 2개로 표기해야 함
def test_fwrite2():
    # x 모드 : 대상 파일이 존재하면 FileExistsError 발생함 (덮어쓰기 방지용으로 주소 사용)
    f = open('D:\\python_workspace\\day5Project\\fileio\\testb.txt', 'x', encoding='utf-8')
    f.write('test file path open test\n')
    f.write('경로를 포함해서 파일 지정 확인\n')
    f.write('2024년 04월 25일 작성한 파일임.')
    f.close()

# a 모드 : append(추가쓰기 모드)
# 기존 내용 다음에 추가됨
def test_fwrite3():
    f = open('testc.txt', 'a', encoding='utf-8')
    f.write('test file append running.\n')
    f.write('파일의 기존 내용 뒤에 추가쓰기 확인\n')
    f.close()

# 파이썬에서 파일이나 디렉토리 다루기
# os 모듈이 제공하는 함수 사용
def test_osmodule():
    # 사용 중인 컴퓨터의 사용자 계정 조회(컴퓨터 이름)
    print(os.getlogin())
    # 현재 작업 디렉토리 조회
    print(os.getcwd())

    system_user = os.getlogin()
    # 디렉토리 만들기 : os.mkdir('만들 디렉토리 경로와 디렉토리명')
    work_dir = 'C:\\Users\\' + system_user + '\\Desktop\\python'
    # os.mkdir(work_dir)  # 주의 : 같은 이름의 디렉토리 있으면 에러
    os.chdir(work_dir)  # 현재 작업토리 변경 : os.chdir('변경할 디렉토리명')
    print(os.getcwd())

    # 변경할 디렉토리에 파일 저장
    f = open('sample.txt', 'w', encoding='utf-8')
    f.write('파이썬으로 디렉토리 만들고, 만든 디렉토리로 작업 폴더를 변경함\n')
    f.write('''여러줄 테스트입니다.
    안녕하세요
    변경된 디렉토리도 실험합니다.
    유니코드로 인코딩된 글자들을 기록 저장
    확인함\n''')
    st = '''테스트 2
    이번엔 스트링 대입
    테스트\n'''
    f.write(st)
    f.close()

# 리스트, 튜플, 셋, 딕셔너리 등에 저장한 데이터들을 파일에 저장
# writelines() 함수 사용
def test_writeline():
    tp = ('a', 'b', 'c')
    ls = ['r', 'g', 'b']
    f = open('list.txt', 'w', encoding='utf-8')
    f.writelines(tp)
    f.write('\n')
    f.writelines(ls)
    f.write('\n')

    # 각 아이템별로 한 줄씩 기록을 원하면, write() 반복 실행
    # f.write(ls) # write() 는 str 만 사용 가능, 리스트 사용 불가
    for data in ls:
        f.write(str(data))  # 문자가 아닌 아이템은 str() 사용
        f.write('\n')

    f.close()

# r(rt, read text) : 읽기 전용
# 주의 : 대상 파일 없으면 에러
# read() : 파일 전체 내용을 한번에 읽음
# readline() : 파일 안의 내용을 한줄씩 읽음
#                    마지막 라인을 읽고, 더이상 읽을 라인이 없으면 None 리턴
# readlines() : 파일의 내용을 줄단위(아이템)로 모두 읽어서 리스트로 반환
def test_fread():
    print(os.getcwd())
    # f = open('sample.txt', 'r', encoding='utf-8')
    f = open('testb.txt', 'r', encoding='utf-8')
    # print(f.read())

    # 파일의 내용을 한 줄씩 읽도록 처리한다면
    while True:
        line = f.readline()
        if not line : # line 변수의 값이 없다면, None 이면과 동일
            break
        print(line, end='')

    f.close()

def test_fread2():
    f = open('testb.txt', 'r', encoding='utf-8')
    flist = f.readlines()
    print(flist)
    f.close()


# 함수 실행
if __name__ == '__main__':
    # test_fwrite()
    # test_fwrite2()
    # test_fwrite3()
    # test_osmodule()
    # test_writeline()
    # test_fread()
    test_fread2()


