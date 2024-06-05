# test_matlpotlib.py
# matplotlib를 이용한 그래프 그리기

# matplotlib 패키지 설치함
import matplotlib as mpl
import matplotlib.pyplot as plt

def test_plot1():
    '간단한 plot 그리기 : 기본은 선그래프임(line plot)'
    # 그래프로 표현할 데이터는 리스트 또는 배열이여야 함
    sample_data = [1, 4, 9, 16]
    plt.title('Line Plot')  # 그래프 제목 지정 함수
    plt.plot(sample_data)  # 그래프 그리기 함수
    # 리스트가 하나이면 y축 값으로 사용됨
    plt.show()  # 그래프 출력 함수

def test_plot2():
    # title : 그래프 제목

    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.title('Line Plot')
    plt.plot(x, y, '.--')   # 점선과 포인트로 그래프 표시
    plt.xlabel('x-axis')    # xlabel : x축 이름
    plt.ylabel('y-axis')    # ylabel : y축 이름
    plt.xlim(0, 6)  # xlim : x축 범위
    plt.ylim(0, 30) # ylim : y축 범위
    plt.xticks([1, 2, 3, 4, 5, 6])  # xticks : x축 눈금
    plt.yticks([0, 5, 10, 15, 20, 25, 30])  # yticks : y축 눈금
    plt.grid(visible=True)  # 눈금 표시
    plt.show()

# 그래프에 한글을 사용하려면, 한글 폰트 파일을 다운 받아서 사용
import matplotlib.font_manager as fm

def test_fonts():
    # 라이브러리 자원(설치한 패키지) 저장 폴더 경로 확인하기
    print(mpl.matplotlib_fname())
    # matplotlib 모듈에서 다운 받은 글꼴을 그래프(plot)의 기본 글 꼴로 사용하게 하려면
    # D:\python_workspace\visualizationProject\.venv\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
    # ttf 폴더 안에 다운 받은 글꼴 파일을 복사해 넣음
    # 참고 : 압축 푼 ttf 파일을 더블 클릭해서 설치 버튼 누르고 설치한 경우에는
    #          C:\\windows\\fonts 에 기본 설치 됨

    # 글꼴 파일 복사 후 matplotlib 캐시에 변경 내용 반영함
    # 1. 캐시 파일 저장 위치 확인함
    print(mpl.get_cachedir())
    # 2. 해당 위치의 캐시 파일을 직접 파일 탐색기에서 찾아내서 삭제
    # => 이전 폰트 리스트 정보를 가진 캐시임
    # 3. 프로그램 재실행하면 ㅋ시 파일 생성 > 파일 탐색기에서 확인
    # => 만약, 캐시 파일 안 생기면 재부팅
    # mpl.rcParams['font.family'] = 'Malgun Gothic'
    # mpl.rcParams['axes.unicode_minus'] = False

def test_fonts2():
    # 폰트 설정
    # 첫번째 방법 : rcParams 함수를 이용해서 설정 후 그래프 작업 전체에 사용

    # 현재 사용 중인 폰트 종류와 글자 크기 확인
    print(mpl.rcParams['font.family'])
    print(mpl.rcParams['font.size'])

    # 한글 폰트로 설정 변경
    mpl.rc('font', family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    # 축에 적용되는 유니코드에 (0~65535) 숫자에 음수 부호 사용 해제

    # 그래프에 설정된 글꼴 사용 확인
    plt.title('한글 그래프 제목')
    plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
    plt.xlabel('x축')
    plt.ylabel('y축')
    plt.show()

def test_fonts3():
    # 그래프의 특정 부분만 원하는 글꼴로 설정을 변경할 수도 있음
    # 사용할 글꼴 파일의 위치는 어디든 상관 X
    # font_path = '드라이브:/경로명.../글꼴 파일이 있는 폴더명/ 사용할 글꼴파일명.확장자'
    font_path = './fonts/NanumGothicBold.ttf'
    font_prop = fm.FontProperties(fname=font_path, size=18)

    plt.title('예제 그래프', fontproperties=font_prop)
    plt.plot([10, 20, 30, 40, 50], [1, 4, 9, 16, 25])
    plt.xlabel('x축', fontproperties=font_prop)
    plt.ylabel('y축', fontproperties=font_prop)
    plt.show()

def test_fonts4():
    # 값 객체마다 별도의 폰트 적용 : fontdict 인수에 넣어서 사용
    font1 = {'family': 'NanumGothic', 'color': 'darkred','size': 12, 'weight': 'bold'}
    font2 = {'family': 'NanumMyeongjo', 'color': 'darkblue','size': 18}
    font3 = {'family': 'NanumGothic', 'color': 'darkgreen','size': 24, 'weight': 'light'}

    plt.title('한글 그래프 제목', fontdict=font1)
    plt.plot([10, 20, 30, 40, 50], [1, 4, 9, 16, 25])
    plt.xlabel('X축', fontdict=font2)
    plt.ylabel('Y축', fontdict=font3)
    plt.show()



if __name__ == '__main__':
    # test_plot1()
    # test_plot2()
    # test_fonts()
    # test_fonts2()
    # test_fonts3()
    test_fonts4()