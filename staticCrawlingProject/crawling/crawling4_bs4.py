
# crawling\\crawling4_bs4.py
# movie 테이블에 기록된 행들을 모두 조회해 와서 출력 처리함
# 등수순 오름차순정렬해서 모두 조회해 옴
# 조회한 한 행의 정보를 Movie 클래스 객체로 생성해서, 객체를 리스트에 저장 처리함

import common.dbConnectTemplate as dbtemp
import entity.Movie as mv

# 오라클 드라이버 설정
dbtemp.oracle_init()
conn = dbtemp.connect()

query = "select * from movie order by rank asc"

movie_list = list()

cursor = conn.cursor()
resultset = cursor.execute(query).fetchall()

for row in resultset:
    # print(row)
    movie_list.append(mv.Movie(row[0], row[1], row[2], row[3], row[4], row[5]))


# 리스트에 저장된 영화 객체 정보 출력 확인
for movie in movie_list:
    print(movie)    # __str__() 이 자동 실행됨