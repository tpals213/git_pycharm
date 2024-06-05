#test1.py
# 한글 형태소 분석 테스트 스크립트 1

# Hannanum : KAIST 말뭉치를 이용해 생성된 사전
from konlpy.tag import Hannanum     # 클래스만 임포트

# 레퍼런스변수 = 클래스명(전달할 초기값)    => 객체 생성
hannanum = Hannanum()

# 제공되는 메소드 정리 : 레퍼런스.메소드(전달인자)
# hananum.analyze() : 구(phrases) 분석
# hannanum.morphs() : 형태소 분석
# hannanum.nouns() : 명사 분석
# hannanum.pos() : 형태소 분석 태깅


# 사용 예시
print('Hannanum 이용 ----------------------------------------')
text1 = u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'
print(hannanum.analyze(text1))
print(hannanum.morphs(text1))
print(hannanum.nouns(text1))
print(hannanum.pos(text1))

# KKma : 세종 말뭉치를 이용해 생성된 사전(꼬꼬마, 서울대에서 만듬)
from konlpy.tag import Kkma
kkma = Kkma()

# 메소드
# kkma.sentences() : 문장 분석
# kkma.morphs() : 형태소 분석
# kkma.nouns() : 명사 분석
# kkma.pos() : 형태소 분석 태깅

# 사용 예시
print('Kkma 이용 ----------------------------------------')
print(kkma.sentences(text1))
print(kkma.morphs(text1))
print(kkma.nouns(text1))
print(kkma.pos(text1))

# Komoran : Java 로 쓰여진 오픈 소스 한글 형태소 분석기
from konlpy.tag import Komoran
komoran = Komoran()

# 메소드 정리
# komoran.morphs() : 형태소 분석
# komoran.nouns() : 명사 분석
# komoran.pos() : 형태소 분석 태깅

print('Komoran 이용 ----------------------------------------')
print(komoran.morphs(text1))
print(komoran.nouns(text1))
print(komoran.pos(text1))

# Twitter (Okt) - 오픈 소스 한글 형태소 분석기
from konlpy.tag import Okt

okt = Okt()

# 제공되는 메소드 정리 : 레퍼런스.메소드(전달인자)
# okt.phrases() : 구(Phrase) 분석
# okt.morphs() : 형태소 분석
# okt.nouns() : 명사 분석
# okt.pos() : 형태소 분석 태깅


# 사용 예시
print('Okt 이용 ----------------------------------------')
print(okt.phrases(text1))
print(okt.morphs(text1))
print(okt.nouns(text1))
print(okt.pos(text1))

# stem : 각 단어에서 어간 추출 처리 매개 변수
print('Okt method : stem parameter using ------------------------------')
print(okt.morphs(text1, stem=True))






