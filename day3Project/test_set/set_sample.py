# test_set/set_sample.py
# 모듈로 표현 : test_set.set_sample

# 집합(set) 자료형
# 교집합(&), 합집합(|), 차집합(-) 연산 가능한 자료형
# 저장 방식은 자바의 Set 과 같음 : 같은 값 중복 저장 X, 저장 순서 X

# set 정의 방법 1 : {} 중괄호 사용
def test1():
    set1 = {1, 2, 3, 4, 1, 2}
    print(f'set1 = {set1}')

# set 정의 방법 2 : set() 함수 사용
def test2():
    set1 = set()
    print(f'set1 = {set1}')

# set 에 문자열을 저장하는 경우 : 문자 하나씩 저장됨
def test3():
    set1 = set('Hello') # 중복 저장 X -> 'l' 이 한개만 저장
    print(set1, type(set1))

    set2 = set('Python')    # 저장 순서 X -> 순서 무작위
    print(set2, type(set2))

# set 에 list 저장할 수 있음
# 리스트 자체는 값 순서대로 저장함 -> set 이 저장 순서를 유지하게 하는 방법으로 이용
def test4():
     set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
     print(set1, type(set1))

     set2 = set([4, 6, 1, 3, 2, 8])
     print(set2, type(set2))

# set 자료형은 집합 연산 가능 : 합집합, 교집합, 차집합
def test5():
    set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
    print(set1, type(set1))
    set2 = set([4, 5, 6, 7, 8, 9, 10])
    print(set2, type(set2))

    # 교집합 : & 연산자 사용 또는 intersection() 함수 사용
    print('교집합 : ', set1.intersection(set2))
    print('교집합 : ', set1&set2)

    # 합집합 : | 연산자 사용 또는 union() 함수 사용
    print('합집합 : ', set1.union(set2 ) )
    print('합집합 : ', set1 | set2)

    # 차집합 : - 연산자 사용 또는 difference() 함수 사용
    print('차집합 : ', set1.difference(set2))
    print('차집합 : ', set1 - set2)

    # 합집합 - 교집합
    print(set1 ^ set2)

# 값 추가, 삭제 가능
def test6():
    set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
    print(set1, type(set1))

    # 값 1개 추가 : add()
    set1.add(99)
    print(set1, type(set1))

    # 값 여러개 추가 : update()
    set1.update([777])
    print(set1, type(set1))
    set1.update([33, 44, 55])
    print(set1, type(set1))

    # 값 삭제 : remove()
    set1.remove(777)
    print(set1, type(set1))

# list 의 값 중복 제거할 때 set 이용
def test7():
    list1 = [1, 1, 22, 2, 3, 3, 4, 4, 4, 6, 8, 12, 32, 22, 15, 11]
    print('list1 = ', list1)
    set1 = set(list1)
    print(set1, type(set1))

    list1 = [set1]
    print('list1 = ', list1, type(list1))









