# path : crawl/crawling_bs4.py
# bs4 : beautifulSoup4 를 이용한 웹 크롤링 테스트 1

# 패키지 설치 : pip install beautifulsoup4
# import bs4  # 웹 페이지의 웹 문서를 html 로 분석하는 모듈
# import urllib.request as req    # 웹상의 데이터를 가져오는 모듈
import urllib.request as req, bs4

# 1. url 로 웹페이지에 접속함
web_page = req.urlopen('https://www.naver.com')

# 2. 접속한 페이지 소스를 읽어옴 > 출력확인 (인코딩된 상태)
# html_code = web_page.read()
# print(html_code)

# 3. 읽어온 인코딩 된 소스를 html 태그 구문으로 변경
decoding_code = bs4.BeautifulSoup(web_page, 'html.parser')
print(decoding_code)
