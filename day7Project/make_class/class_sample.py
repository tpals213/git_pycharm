# path : make_class\\class_sample.py
# 파이썬에서 클래스 만들어 사용하기

# 파이썬은 객체 지향 스크립트 언어이다
# 절차 지향 프로그래밍 가능함 : 실행 코드 구문이 작성 된 순서대로 작동 됨

# 객체 지향 프로그래밍(OOP) 은 클래스 만들기 부터 시작

'''
class 클래스명:
    멤버 변수 = 초기값
    ...
    def 함수명 (self, 매개변수, 매개변수 = 기본값, *매개변수):
        필드에 대한 값 처리 내용에 대한 코드 작성
        self.멤버변수 = 변경할 값 | 계산 식
        return self.필드명 또는 return 결과값

- 매개변수 self : 자바, C++, javaScript, C# 의 this 와 같음
'''

# 클래스 이름은 첫글자 영문 대문자 권장 (Naming Rule)
class SClass:
    pass    # 멤버가 없는 빈 클래스 작성할 수 있음
# 비어 있는 클래스는 실행시 namespace 가 할당됨 => 이름만 있어도 메모리 공간이 할당됨

# 클래스 사용 : 객체 생성 (메모리에 클래스에 대한 객체 공간(instance) 할당)
# 레퍼런스 변수 = 클래스명()
ref1 = SClass()
ref2 = SClass()

print('ref1 이 가진 주소 : ', id(ref1))
print('ref2 이 가진 주소 : ', id(ref2))

# 파이썬은 실행할 때(동적으로) 멤버 변수(필드)를 추가할 수 있음
ref1.score = 100    # ref1이 참조하는 인스턴스 안에 score 를 추가하고 100을 저장함
print('ref1이 참조하는 객체 안의 score 필드 값 : ', ref1.score, id(ref1.score))
# print('ref1이 참조하는 객체 안의 score 필드 값 : ', ref2.score) # error