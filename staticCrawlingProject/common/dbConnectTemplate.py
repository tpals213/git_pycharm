# path : common\\dbConnectTemplate
# module : common.dbConnectTemplate
# 데이터 베이스 연결 관리용 공통 모듈 정의 (변수와 함수만 정의)

# 1. 사용할 패키지(모듈) import
# 설치 패키지 : cx-Oracle => import 시 모듈명은 cx_Oracle

# 설치 실패시 : C++ 빌드 툴즈 설치
# exe 다운받음 > 설치
# 주의 : 설치 시 C++ 를 사용한 데스크톱 개발 만 체크하여 설치
# 설치 후 '수정'으로 추가

import cx_Oracle

# 오라클 연결을 위한 값들을 전역변수로 지정
url = 'localhost:1521/xe'
user = 'c##testweb'
pwd = 'testweb'

def oracle_init():  # 애플리케이션에서 딱 한번만 구동
    cx_Oracle.init_oracle_client(lib_dir='D:\\instantclient_18_5')
    # Mac 에서 필요 없음

def connect():
    try:
        conn = cx_Oracle.connect(user, pwd, url)
        # Mac 에서는 아래 구문을 사용
        # conn = cx_Oracle.connect('c##testweb/testweb@localhost:1521/xe')
        conn.autocommit = False
        return conn
    except Exception as msg:
        print('오라클 연결 에러 : ', msg)
        return None

    # conn = cx_Oracle.connect('c##testweb', 'testweb', 'localhost:1521/xe')

def close(conn):
    try:
        if conn:    # conn 이 Null 이 아니면(True)
            conn.close()
    except Exception as msg:
        print('오라클 닫기 실패 : ', msg)

def commit(conn):
    try:
        if conn:    # conn 이 Null 이 아니면(True)
            conn.commit()
    except Exception as msg:
        print('오라클 커밋 실패 : ', msg)

def rollback(conn):
    try:
        if conn:    # conn 이 Null 이 아니면(True)
            conn.rollback()
    except Exception as msg:
        print('오라클 롤백 실패 : ', msg)




