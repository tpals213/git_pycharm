# test2.py
# konlpy 모듈에서 메소드 매개변수 사용 테스트 : Okt 클래스 사용
from konlpy.tag import Okt  # 클래스
from konlpy.utils import read_txt   # 함수

# 형태소 분석 태깅 : pos(), morphs(), nouns() 등에 사용하는 매개변수들
# norm : 형태소를 깔끔하게 만들어 주고, 불필요한 데이터 제거
# stem : 형태소의 원형을 찾아서 반환해 줌
okt = Okt()

# 텍스트 파일(*.txt) 의 데이터를 읽어와서 분석
text = read_txt('./data/sample.txt', u'utf-8')
test = u'아니 존나 웃기넼ㅋㅋㅋㅋ시바 말이라고 하나ㅋㅋㅋㅋ개탕후루조 개이득'


print('norm=True, stem=True -----------------------')
mal_list = okt.pos(text, norm=True, stem=True)
print(mal_list)

print('norm=False, stem=False -----------------------')
mal_list = okt.pos(text, norm=False, stem=False)
print(mal_list)

mal = okt.pos(test, norm=True, stem=True)
print(mal)