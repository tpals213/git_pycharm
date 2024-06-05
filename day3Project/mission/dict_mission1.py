# 경로 표시 : \\ 사용 표기 : mission\\dict_mission.py
# 경로 표시 : / 사용 표기 가능 : mission/dict_mission.py
# 모듈로 표시 : mission.dict_mission.py

# 사전(dict) 자료형 복습문제
"""  키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    학생이름 : 홍길동 (name : str)
    학년 : 2 (grade : int)
    반 : 3 (s_class : int)
    번호 : 12 (s_no : int)
    점수 : 87.5 (score : float)
처리 내용 :
    입력받은 값들을 사전(student_dict)에 저장 처리함
    위의 변수이름들을 키(str)로 사용함
출력 내용 :
    사전에 저장된 값들을 출력함
    2학년 3반 12번 홍길동의 점수는 87.50 입니다.
    -> 점수는 소수점아래 둘째자리까지 표시
    -> format()  또는 f-string 또는 포멧서식(%포멧문자) 사용함
"""

def dict_func():
    name = input('학생 이름 : ')
    grade = int(input('학년 : '))
    s_class = int(input('반 : '))
    s_no = int(input('번호 : '))
    score = float(input('점수 : '))

    student_dict = {'name': name,
                            'grade' : grade,
                            's_class' : s_class,
                            's_no' : s_no,
                            'score' : score}

    print(student_dict)
    print(student_dict['grade'], '학년', student_dict['s_class'], '반', student_dict['s_no'], '번'
          , student_dict['name'], '의 점수는 ', format(student_dict['score'],'.2f'), '입니다.')




