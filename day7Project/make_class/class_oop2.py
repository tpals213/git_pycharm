# path : make_class\\class_oop2.py
# oop 에서의 연산자 오버로딩 (operator overloading)

# 오버로딩 ; 중복 작성(정의), 이름이 같은 메소드를 클래스 안에 여러개 만드는 것
# 연산자 : 값 계산에 사용되는 기호 문자
# c++, python 에서는 기존 값 계산에 사용되는 연산자에다가 클래스 객체에 대한 연산으로
# 새로운 의미를 정의하는 것

'''
객체 + 값 : __add__(self, 값) : return self.필드 + 값
객체 - 값 : __sub__(self, 값) : return self.필드 - 값
객체 * 값 : __mul__(self, 값) : return self.필드 * 값
객체 / 값 : __truediv__(self, 값) : return self.필드 / 값
객체 > 값 : __gt__(self, 값) : return self.필드 > 값
객체 >= 값 : __ge__(self, 값) : return self.필드 >= 값
객체 < 값 : __lt__(self, 값) : return self.필드 < 값
객체 <= 값 : __le__(self, 값) : return self.필드 <= 값
객체 == 값 : __eq__(self, 값) : return self.필드 == 값
객체 != 값 : __ne__(self, 값) : return self.필드 != 값
'''
# 시퀀스나 맵 타입으로 오버라이딩 할 수 있음

class OOP:
    __num = 0

    def __init__(self, num):
        self.__num = num

    # + 연산자를 메소드로 오버로딩 처리
    def __add__(self, other):   # c++ : public int operator + (value){retrun this.num + value;}
        '+ 연산자를 메소드로 오버로딩 처리'
        return self.__num + other

    def __sub__(self, other):
        '- 연산자를 메소드로 오버로딩 처리'
        return self.__num - other

    def __mul__(self, other):
        '* 연산자를 메소드로 오버로딩 처리'
        return self.__num * other

    def __truediv__(self, other):
        '/ 연산자를 메소드로 오버로딩 처리'
        return self.__num / other

    def get_num(self):
        return self.__num

    def set_num(self, num):
        self.__num = num

# ----------------------------------------------------------------

# 클래스 객체 생성
ref = OOP(100)
# 객체와 값의 연산
# 기본적으로 객체와 값의 연산은 불가능임
# 클래스 안에 연산자 오버로딩 메소드가 작성된 경우에만 객체와 값 연산이 가능함
# print('ref > 30 : ', ref > 30)    # TypeError: '>' not supported between instances of 'OOP' and 'int'
print('ref + 30 : ', ref + 30)  # 130
print('ref - 30 : ', ref - 30)  # 70
print('ref * 30 : ', ref * 30)  # 300
print('ref / 30 : ', ref / 30)  # 3.33333333














