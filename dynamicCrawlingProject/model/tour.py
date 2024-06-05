# path : model\\tour.py
# module : model.tour
# 여행지 정보 저장용 클래스 정의 스크립트

# 순위(rank), 이름(name), 설명(description), 카테고리(category)
class TourInfo:
    # field : private
    __rank = ''
    __name = ''
    __description = ''
    __category = ''

    # constructor
    def __init__(self, rank, name, description, category):
        self.__rank = rank
        self.__name = name
        self.__description = description
        self.__category = category

    # operator overloading
    # 객체가 가진 필드값들을 하나의 문장으로 만들어서 리턴
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__rank, self.__name, self.__description, self.__category)

    # getter
    def getRank(self):
        return self.__rank

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getCategory(self):
        return self.__category

    # setter
    def setRank(self, rank):
        self.__rank = rank

    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description

    def setCategory(self, category):
        self.__category = category

