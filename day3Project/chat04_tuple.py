# chap04_tuple.py
# 튜플(tuple) 자료형 : 리스트와 저장 방식 동일
# 여러 종류의 값들을 순차적으로 저장하는 집합자료형
# 리스트와 다른 점은 저장된 값은 변경할 수 없음 -> 상수 개념 적용

# 튜플 정의방법 1 : 소괄호 () 로 정의
tp_1 = ()
print(tp_1, type(tp_1))

# 튜플 정의 방법 2 : tuple() 함수 사용
tp_2 = tuple()
print(tp_2, type(tp_2))

# 튜플도 리스트와 같이 인덱싱, 슬라이싱 연산 가능
lst = [10, 20, 30]
tpl = (11, 22, 33)
print(lst, type(lst))
print(tpl, type(tpl))

print('0번째 값 : ', lst[0], tpl[0])
print('0번째부터 1번째까지의 값들 : ', lst[0:2], tpl[0:2])
print('리스트 합치기 : ', lst + lst)
print('튜플 합치기 : ', tpl + tpl)

# 튜플과 리스트의 차이점 : 튜플은 값 변경 불가
lst[2] = 99
print('lst : ', lst)
# tpl[2] = 15   # error

# 주의사항 :
# 튜플 생성시에 1개의 값만 가질때는 반드시 값 뒤에 콤마(,) 붙일 것
tp_3 = (1)
print(tp_3, type(tp_3))

tp_4 = (1, )
print(tp_4, type(tp_4))

# 튜플 생성 시 저장 데이터가 1개 일때는 소괄호 생략해도 됨
tp_5 = 1,
print(tp_5, type(tp_5))

# 튜플 내장함수
# count() : 찾는 값의 갯수 조회
# 튜플변수.count(찾는값)
number_count = tpl.count(11)
print('tpl 에 저장된 11의 갯수 : ', number_count)

# index() : 찾는 값의 인덱스(순번) 조회
# 튜블변수.index(찾는값)
# 찾는 값이 없으면 에러
find_index = tpl.index(33)
print('tpl 에 저장된 33의 위치 : ', find_index)
# print('tpl 에 저장된 55의 위치 : ', tpl.index(55)) #error

# len(튜플변수) : 저장된 데이터의 갯수
print('tpl에 저장된 데이터 갯수 : ', len(tpl))

# 참고사항 : () 없이 하나의 변수에 값 나열 대입하면 자동 튜플 처리
x = 1, 2, 3
print(x, type(x))

# 참고사항 : 함수에서 튜플 리턴 가능
def f_test():
    return(1, 3)

# 함수 사용 부분
x, y = f_test()
print(x, type(x))
print(y, type(y))

# 참고사항 : 함수에서 여러 개의 값을 리턴 불가
def f_test2():
    return 1, 2, 3  # 원래 return 은 한개의 값만 리턴할 수 있는 것이 일반적

# 함수 사용 부분
z = f_test2()
print(z, type(z))










