# path : testdb\\test_mysql.py

# 파이썬 외부 모듈(패캐지) 설치와 사용
# 파이썬 외부 모듈은 프로젝트에 직접 설치해서 사용하는 방법이 있고 (venv)
# 아나콘다에 별도의 콘다 환경을 준비해서 필요한 패키지를 따로 설치한 다음 프로젝트에 가져다 사용하는 방법 (conda)

# 프로젝트에 직접 설치하는 방법
# 파이참 툴 좌하단의 Python Packages 탭 클릭 후 설치




# 첫번째 :
# 좌 하단 Python Packages 탭 클릭
# 검색 후 우측 install package 버튼으로 설치
# 만약, 설치 실패 시 오류 메세지에서 에러 이유 찾아내서 해결

# 두번째 :
# 모든 파이썬 개발 툴에서 공통으로 사용하는 방법
# Terminal 탭 클릭 후 pip install 패키지명 으로 패키지 설치 가능
# 터미널종료 현재프로젝트경로 > 프롬프트 표시됨
# pip install 패키지명
# 주의사항 : pip 버전을 먼저 upgrade 해야 하는 경우가 있음
# 패키지 설치와 pip 업그레이드 동시 수행
# python -m pip install --upgrade 설치할 패키지명

# 세번째 :
# File 메뉴 > Settings... > 왼쪽 항목에 Project : 프로젝트명 펴시 찾음
# > 프로젝트명 부분을 확장시킴
# 오른쪽 아래에 'python interpreter' (파이썬 인터프리터) 선택
# => 현재 프로젝트에 설치된 패키지 모듈 볼 수 있음
# > 위쪽의 '+' 클릭 > 새 창 열림
# 설치할 패키지 검색 > 검색한 패키지 이름 선택 > 아래쪽의 '설치' 버튼 클릭
# 설치 성공 메세지 확인하고 창 닫음



# 데이터베이스 연결에 필요한 파이썬 패키지 --------------------
# mysql db : pymysql 패키지 필요
# oracle db : cx_Oracle 패키지 필요

# 1. 설치 후에 import 선언하고 사용함
import pymysql

# 2. 해당 데이터 베이스에 연결하기 위한 코드 작성
# db 서버의 ip 주소(url), 포트 번호, 사용자 이름, 암호
dbURL = 'localhost' # dbURL = '192.168.120.34'
dbPort = 3306
dbUser = 'root'
dbPassword = '1234'

# 3. 데이터베이스 연결
# 임포트한 모듈에서 제공하는 메소드를 사용 : pymysql.connect()
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPassword, db='testdb', \
                       charset='utf8', use_unicode=True)

# 연결이 실패하면 conn = null (None)
# 연결이 성공하면의 조건식 -> if conn!= null :

# 4. db 연결이 성공했다면, 필요한 쿼리문(C:insert, R:select, U:update, D:delete) 실행
# 예 : select 쿼리문 작성해서 실행 처리
query = "select * from sample"
cursor = conn.cursor()  # 자바의 Statement | PreparedStatement
cursor.execute(query)   # 쿼리문 보내서 실행
result = cursor.fetchall()  # 조회된 모든 결과를 받음, 반환 자료형은 tuple 임

# 이후 결과 매핑 처리 : 반복문으로 행의 컬럼값들을 vo (dto) 객체의 필드(property)에 저장 처리

# 5. 쿼리문이 dml 이면 트랜잭션 처리 필수
if result > 0:
    conn.commit()
else:
    conn.rollback()

# 6. 데이터베이스 연결 종료
cursor.close()
conn.close()
























