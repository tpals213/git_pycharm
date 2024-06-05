# hellocv.py
# opencv 패키지 설치 : opencv-python
# opencv 모듈명 : cv2

import cv2
import sys

# print(cv2.__version__)

# 시스템 기본 카메라로부터 cv2.VideoCapture() 객체 생성
cap = cv2.VideoCapture(0)   # 카메라 열기

if not cap.isOpened():  # 카메라 열기가 실패했다면
    print('카메라를 열 수 없습니다.')     # 카메라가 없거나, 카메라 드라이버 미설정
    sys.exit()  # 프로그램 종료

# 카메라 프레임 해상도 출력
print('Frame with : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 매 프레임 처리 및 화면 출력
while True:
    ret, frame = cap.read()  # 프레임 읽기, 다른 앱에서 카메라 사용중(on)이면 작동 안 됨
    # frame : 카메라로부터 읽은 프레임 정보 저장
    # ret : 읽기 성공 여부 저장 (True/False)
    if not ret:  # 프레임 읽기 실패    if ret == False
        print('프레임을 읽을 수 없습니다.')
        break

    edge = cv2.Canny(frame, 10, 10)    # 경계선 검출 함수 : 이미지의 경계선만 리턴
    # cv2.Canny(프레임, threshold1, threshold2)
    # threshold1 : minVal 임계값 (값이 크면 엣지 검출 어려움, 작을수록 앳자 검출 쉬움)
    # 적으면 경계선이 이어짐, 크면 경계선이 끊어짐
    # threshold2 : maxVal 임계값 (경계선인지 아닌지를 판단하는 임계값임, 작을수록 엣지가 많아짐)

    cv2.imshow('edge', edge)  # 경계선 화면 출력
    cv2.imshow('frame', frame)  # 프레임 화면 출력

    if cv2.waitKey(1) == 27:  # ESC 키 입력
        break  # 프로그램 종료

# 카메라 사용 해제
cap.release()
cv2.destroyAllWindows()  # 모든 윈도우 창 닫기

print('프로그램을 종료합니다.')
