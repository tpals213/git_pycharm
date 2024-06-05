# path : testdb\\test_oracle.py
# 파이썬과 오라클 연동

# 패키지설치 : cx-Oracle
# 오라클사에서 제공하는 파이썬과 오라클을 연동하기 위한 드라이버 파일을 먼저 다운
# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# windows 64 bit 용 zip 다운 > 압출 풀기
# 폴더 경로를 짧게 하기 위해서 폴더 복사
# D:\\instantclient_18_5

# 1. 사용할 패키지(모듈) import
# 설치 패키지 : cx-Oracle => import 시 모듈명은 cx_Oracle

# 설치 실패시 : C++ 빌드 툴즈 설치
# exe 다운받음 > 설치
# 주의 : 설치 시 C++ 를 사용한 데스크톱 개발 만 체크하여 설치
# 설치 후 '수정'으로 추가

import cx_Oracle
import os

# 2. 오라클 드라이브(instantclient) 등록
# 방법 1. 환경변수 패스에 등록 (파이썬 코드로 등록 가능)
location = 'D:\\instantclient_18_5'
os.environ['PATH'] = location + ';' + os.environ['PATH']

# 방법 2. 코드로 오라클 초기 설정으로 지정
# 주의 : 애플리케이션 전체 실행 시 딱 한번만 작동되어야 함
cx_Oracle.init_oracle_client(lib_dir=location)

# 3. 데이터베이스 연결
url = 'localhost:1521/xe'
user = 'c##testweb'
pwd = 'testweb'

conn = cx_Oracle.connect(user, pwd, url)
# conn = cx_Oracle.connect('c##testweb', 'testweb', 'localhost:1521/xe')
# conn = cx_Oracle.connect('c##testweb/testweb@localhost:1521/xe')
print('conn : ', conn)

# 4. 쿼리문 준비하기
query = 'select * from c##testweb.member'

# 5. 쿼리문 실행시키기 위한 객체 준비하고, 쿼리문 실행 처리
# cursor : 준비된 쿼리문을 연결된 db로 전송해서 실행시키는 객체
cursor = conn.cursor()  # db 연결 정보로 커서 객체 생성
cursor.execute(query)   # 쿼리문을 db로 전송하고 실행한 결과 받음
# 커서가 실행된 쿼리문 결과를 받음
# select 쿼리문 실행시켰다면, 결과 집합(Result Set)을 커서가 받음
# dml 문(insert, update, delete) 은 처리된 행 갯수 커서가 받음
print('cursor : ', cursor)

# 6. select 쿼리문이라면 실행결과에 대한 매핑 작업
# 커서가 가진 결과 정보를 꺼내서 변수에 옮겨 기록 저장 처리
# result = cursor.fetchall()
# print('result : ', result)
# print('type(result) : ', type(result))
# print('len(result) : ', len(result))

# 커서가 가진 select 쿼리 조회 결과를 한 행씩 처리한다면
for row in cursor:
    print('행이 가진 컬럼 갯수 : ', len(row), type(row))
    # 컬럼별로 데이터 하나씩 추출
    USERID = row[0]
    USERPWD = row[1]
    USERNAME = row[2]
    GENDER = row[3]
    AGE = row[4]
    PHONE = row[5]
    EMAIL = row[6]
    ENROLL_DATE = row[7]
    LASTMODIFIED = row[8]
    SIGNTYPE = row[9]
    ADMIN_YN = row[10]
    LOGIN_OK = row[11]
    PHOTO_FILENAME = row[12]

    # print(USERID, USERPWD, USERNAME)
    # index 를 이용한 출력 처리
    for i in range(len(row)):   # range(13) : 0 ~ 12
        print(row[i], end=', ')
    print() # 줄 바꿈

# 7. 데이터베이스 연결 종료
cursor.close()
conn.close()
