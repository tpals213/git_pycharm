# path : testdb\\test_oracle2.py
# 오라클 연동과 insert 쿼리문 실행 테스트

# 1. 사용할 패키지(모듈) import
import cx_Oracle
import os
import common.dbConnectTemplate as db

# 2. 드라이버 등록
db.oracle_init()
conn = db.connect()

# 3. 쿼리 생성
# query = "insert into member values('user77', 'pass77', '장세민', 'M', '30', '010-7777-7777', 'tpals213@naver.com', default, default, default, default, default, null)"

# insert 구문에 사용할 값을 외부 데이터를 이용할 경우 (키보드 입력)
# 주의 : 쿼리문에 적용할 외부값은 반드시 튜플로 저장해야 한다.
# 키보드로 값을 입력 받아서 튜플에 저장 처리 :
userid = input('아이디 : ')
passwd = input('비밀번호 : ')
name = input('이름 : ')
gender = input('성별 : ')
age = int(input('나이 : '))
phone = input('전화번호 : ')
email = input('이메일 : ')

# 튜플로 저장
data = (userid, passwd, name, gender, age, phone, email)

# 튜플을 쿼리문에 적용할 때, 값을 1234 순으로 적용해야 함 (순서 주의)
query = "insert into member values(:1, :2, :3, :4, :5, :6, :7, default, default, default, default, default, null)"

# 4. 쿼리 실행 후 close
cursor = conn.cursor()

try:
    cursor.execute(query, data)
    conn.commit()
    print('회원가입 성공')
except Exception as e:
    conn.rollback()
    print('회원가입 실패')
    print(e)
finally:
    cursor.close()
    db.close(conn)

