# path : crawling/crawling2_bs4.py
# url 을 키보드로 입력 받아서 크롤링 테스트

import urllib.request as req, bs4

url = input('URL : ')
# url은 웹상의 자원까지의 경로를 의미함
# 프로토콜://도메인명/폴더명/파일명?이름=값&이름=값
# 쿼리스트링 : 서버측의 대상 파일로 전달되는 값들을 표현한 것
#       ?이름=값&이름=값&이름=값
# https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%98%81%ED%99%94
# https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%98%81%ED%99%94&oquery=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94&tqi=iBeQhdqVN8ossn59QFlssssst10-350074
web_page = req.urlopen(url)
result_code = bs4.BeautifulSoup(web_page, 'html.parser')

print(result_code)