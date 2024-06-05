# list_mission2.py
# 리스트 실습 문제 2
"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)
처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.
출력 내용 :
    리스트에 저장된 값들을 출력함,   국, 영, 수, 총, 평균 순서로 출력
     -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
"""

kor = float(format(float(input('국어 : ')), '.2f'))
eng = float(format(float(input('영어 : ')), '.2f'))
mat = float(format(float(input('수학 : ')), '.2f'))
total_score = float(kor + eng + mat)
print(type(kor))
print(type(total_score))
average_score = format((total_score / 3), '.2f')
tot = []
tot.append([kor, eng, mat, total_score, average_score])

kor = float(input('국어 : '))
eng = float(input('영어 : '))
mat = float(input('수학 : '))
total_score = kor + eng + mat
average_score = total_score / 3
tot.append([kor, eng, mat, total_score, average_score])

kor = float(input('국어 : '))
eng = float(input('영어 : '))
mat = float(input('수학 : '))
total_score = kor + eng + mat
average_score = total_score / 3
tot.append([kor, eng, mat, total_score, average_score])

print(tot)
print('총점 : ', tot[0][3] + tot[1][3] + tot[0][3])





