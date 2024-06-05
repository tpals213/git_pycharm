# path : entity/Movie.py
# module : entity.Movie
# 크롤링해서 추출한 영화 정보 저장용 클래스 정의 스크립트

class Movie:
    # filed (attribute) : private (이름 앞에 _ 2개 붙임)
    rank = 0
    title = ""
    star_point = 0.00
    release_date = ""
    genre = ""
    link = ""

    # 생성자(constructor)
    def __init__(self, rank, title, star_point, release_date, genre, link):
        self.rank = rank
        self.title = title
        self.star_point = star_point
        self.release_date = release_date
        self.genre = genre
        self.link = link

    # 메서드
    # 연산자 오버로딩
    # 자바의 toString() == 파이썬 __str__(self)
    # 객체가 가진 필드 값들을 하나의 문자열로 반환하는 메서드
    def __str__(self):
        return f'{self.rank}위 : {self.title}, 장르 : {self.genre}, 평점 : {self.star_point}, 개봉일 : {self.release_date}, 상세 페이지 : {self.link}'
