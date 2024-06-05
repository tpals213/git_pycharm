# path : crawling/crawling3_bs4.py
# 네이버 개봉 영화 정보 페이지 크롤링 분석 테스트

import urllib.request, bs4

web_page = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
result_code = bs4.BeautifulSoup(web_page, "html.parser")

# 개봉영화 정보가 기록된 태그 앨리먼트 찾기
# 찾아진 태그 앨리먼트 안의 값을 추출 : find() 함수 사용 => 찾은 첫번째 앨리먼트만 리턴함
# find(찾을 텍스트가 기록된 태그명, 태그속성_= '속성값')
# find(태그속성_='속성값')
# find(찾을태그명)

# data_box = result_code.find("div", {"class": "data_box"})
# print(data_box)  # 첫번째 항목 한개만 출력
# movie_title = data_box.find("a", {"class": "this_text"})
# print(movie_title)  # 한 개만 출력

# 태그 앨리먼트 여러 개 추출 : find_all() 사용
# movie_list = result_code.find_all("a", {"class": "this_text"})
# print(movie_list)
# print(len(movie_list))  # a 태그들

# 영화 제목만 추출하기
# for idx in range(len(movie_list)):
#     title = movie_list[idx].text  # a 태그 안의 글자 추출
#     print(title)

movie_div = result_code.find_all("div", {"class": "data_box"})
print(len(movie_div))

movie_list = list()  # 추가함
# 영화제목, 개봉일, 장르, 별점, 링크 추출
for idx in range(len(movie_div)):
    movie_title = movie_div[idx].find("a", {"class": "this_text"}).get_text()
    # movie_title = movie_div[idx].find("a", {"class": "this_text"}).text
    # print(movie_title)
    movie_link = movie_div[idx].find("a", {"class": "this_text"}).attrs['href']
    #movie_link = movie_div[idx].find("a", {"class": "this_text"})['href']
    # print(movie_link)
    movie = dict()  # 딕셔너리에 저장하는 방법
    movie["title"] = movie_title
    movie["link"] = "https://search.naver.com/search.naver" + movie_link
    movie["genre"] = movie_div[idx].find("dl", {"class": "info_group"}).find("dd").text
    # print(movie["genre"])
    movie["star_point"] = float(movie_div[idx].find("span", {"class": "num"}).text)
    # print(movie["star_point"])
    movie["release_date"] = movie_div[idx].find("div", class_="info").find_all("dl")[1].find("dd").get_text()
    # print(movie["release_date"])

    movie_list.append(movie)

# 리스트에 저장된 영화 정보 출력 확인
for movie in movie_list:
    print(movie)
    
# 등수 처리 : 벌점 이용 , 4번째 기록돔 =>[3]
sort_list = sorted(movie_list, key=lambda x: x["star_point"], reverse=True)
print('sorted after ---------------------------------')
print(sort_list)
print('----------------------------------------------')

# 정렬 후 등수 추가 확인
for idx in range(len(sort_list)):
    movie = sort_list[idx]
    print(movie)
    movie['rank'] = idx + 1


# 오라클 db Movie 테이블에 기록 처리
import cx_Oracle
import common.dbConnectTemplate as dbtemp

# 오라클 드라이버 설정
dbtemp.oracle_init()  # 애플리케이션 전체에서 딱 한번 실행함
conn = dbtemp.connect()

# 크롤링한 결과 db 에 기록 처리 : insert 문 사용
query = "insert into movie values (:1, :2, :3, :4, :5, :6)"

# 리스트에 저장된 딕셔너리를 튜플로 변환해서 쿼리문에 적용해서 실행 처리함
for movie in sort_list:
    tp_value = (movie['rank'], movie['title'], movie['star_point'], movie['release_date'], movie['genre'], movie['link'])
    cursor = conn.cursor()
    try:
        cursor.execute(query, tp_value)
        dbtemp.commit(conn)
    except:
        dbtemp.rollback(conn)
    finally:
        cursor.close()





