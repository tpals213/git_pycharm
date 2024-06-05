# chap04_list.py
# 리스트(list) 자료형
# 파이썬이 제공하는 군집자료형임
# 자바의 List 와 같은 자료형

# 개념 : 여러 종류의 값들을 순차적으로 저장하는 자료형
# 저장 용량 제한 x
# 저장 값 종류 제한 x
# 저장 순서에 대한 순번(인덱스 : index) 가 있음

# 리스트 생성 방법 1 : list() 함수 사용
list_1 = list()
print(list_1, type(list))

# 리스트 생성 방법 2 : [] 대괄호 사용
list_2 = []
print(list_2, type(list))

# list 자료형 특징 1 : 문자열(str)과 같이 인덱싱, 슬라이싱 연산 가능
# index(순번 : 저장 순서, 0부터 시작)
# 인덱싱 표현 :  리스트 변수[index]
list_3 = [1, 'a', 0.634, [1, 2, 3, 'qwt'], True, 'betw']
print('0번째 값 : ', list_3[0])
print('3번째 값 : ', list_3[3])
print('5번째 값 : ', list_3[5])

# 슬라이싱 : 리스트에 저장된 데이터들 부분 추출
# 표현 : 리스트변수[시작인덱스 : 끝인덱스 : 간격]
# 시작인덱스~끝인덱스 -1 까지 추출
# 간격 : 생략시 기본값 1
print('0번 인덱스부터 3번 인덱스 데이터 추출 : ', list_3[0:4:1])
print('0번 인덱스부터 3번 인덱스 데이터 추출 : ', list_3[:4:1])

# len(리스트 변수) : 리스트에 저장된 데이터 갯수 리턴
print('list_3 에 저장된 값 갯수 : ', len(list_3))
# len() 을 이요해서 마지막 위치의 값 조회 활용 가능
print('list_3에 저장된 값의 마지막 인덱스 : ', len(list_3)-1)
print('list_3 의 마지막 값 : ', list_3[len(list_3)-1])

# list 자료형 특징 2 : 요소(element) 의 값은 변경 가능
# 변경할 값의 종류 제한 x
# 인덱스 이용 : 리스트변수[인덱스] = 바꿀값
print('변경 전 : ', list_3)
list_3[0] = 874
print('변경 후 : ', list_3)
list_3[1] = 'text'
print('변경 후 : ', list_3)

# list 자료형의 특징 3 : 리스트를 다루는 함수(메소드)들이 제공됨
# 리스트변수.함수명(전달인자)
# append() : 뒤에 추가
# insert() : 엘리먼트 사이에 추가
# remove() : 삭제
# pop() : 꺼내면서 리스트에서 제거
# reverse() : 리스트 안에 데이터 순서 반대로

# chap05. 파이썬에서 제공하는 list 관련 함수 테스트 ------------------------
lst = [1, 3.5, 'list', True, 20, ['a', 'b', 'c']]
print(f'before : {lst}')
print(f'length : {len(lst)}')

# append() : 리스트 뒤로 추가, 마지막 인덱스 증가
# 리스트변수.append(추가할 값)
lst.append(456)
print(f'before : {lst}')
print(f'length : {len(lst)}')

# remove() : 지정한 데이터 제거, 인덱스 감소
# 리스트변수.remove(제거할 데이터)
lst.remove(20)
print(f'before : {lst}')
print(f'length : {len(lst)}')

# 같은 값들이 여러 개 저장되어 있는 리스트인 경우
lst_1 = [1, 1, 2, 2, 1, 3]
print(f'before : {lst_1}')
print(f'length : {len(lst_1)}')

lst_1.remove(1) # 앞에서 부터 검색해서 첫번째로 만나는 값을 제거
print(f'before : {lst_1}')
print(f'length : {len(lst_1)}')

# insert() : 리스트 안의 원하는 위치에 추가
# 리스트변수.insert(위치인덱스, 추가할 값)
lst.insert(1, '추가확인')
print(f'before : {lst}')
print(f'length : {len(lst)}')

# pop() : 인덱스 위치의 값을 꺼냄 (제거)
# 리스트변수.pop() : 마지막 위치의 값 빼냄 (제거)
# 리스트변수.pop(index) : 해당 인덱스 위치의 값을 빼냄
num = lst.pop()
print(f'before : {lst}')
print(f'length : {len(lst)}')
print(f'num : {num}')

lst.pop(3)
print(f'before : {lst}')
print(f'length : {len(lst)}')   # 제거

# extend() : 기존 리스트 뒤에 다른 리스트를 추가해서 리스트를 확장
# 기존 리스트.extend(추가할 리스트)
lst.extend(lst_1)
print(f'before : {lst}')
print(f'length : {len(lst)}')

lst.extend(lst)
print(f'before : {lst}')
print(f'length : {len(lst)}')

# reverse() : 리스트의 저장 순서를 반대로 뒤집기함
# 리스트변수.reverse()
lst.reverse()
print(f'before : {lst}')
print(f'length : {len(lst)}')

# sort() : 리스트의 저장 값들을 오름차순 정렬
# 주의 : 한 가지 종류의 값들로만 저장되어 있을 때 사용가능
# lst.sort() # error

lst_int = [1, 3, 23, 754, 23, 12, 65,12, 63, 1623, 34]
print(f'before sort : {lst_int}')
lst_int.sort()
print(f'after sort : {lst_int}')
lst_int.sort(reverse=True)  # 내림차순 정렬
print(f'after sort : {lst_int}')

lst_str = ['a', 'wr', 'qehbwr', 'aevwqw', 'A', 'qw', 'ABes', 'ABc']
print('before sort : {} '.format(lst_str))
lst_str.sort()
print('after sort : {} '.format(lst_str))
lst_str.sort(reverse=True)
print('after sort : {} '.format(lst_str))

lst_kr = ['가', '나', '까나', 'ㅂㅂㄷ', 'ㄱㄱㄱ', 'weq', 'WEQ', 'Weq', 'ABC']
print('before sort : {} '.format(lst_kr))
lst_kr.sort
print('after sort : {} '.format(lst_kr))
lst_kr.sort(reverse=True)
print('after sort : {} '.format(lst_kr))

# count() : 리스트에 저장된 똑같은 값의 갯수 조회
# 리스트변수.count(찾을 값)
print(f'lst : {lst}')
print(f'lst 에 저장된 1의 갯수 : {lst.count(1)}')