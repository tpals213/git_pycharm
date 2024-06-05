# namecard\\threshold.py
# 1단계 : 명함 이미지 읽어와서 이진화 처리

import cv2
import sys
import matplotlib.pyplot as plt

filename = '../images/namecard1.jpg'

# 파이썬 파일 실행 시, 값을 전달 할 수 있음
# 파일명, 전달값1, 전달값2, ....
# 0번째, 1번째, ...

# 해당 파일을 exe 파일로 만든 다음, 외부에서 실행 시 전달값(argument)
# 프롬프트 경로 표시> 실행파일명 전달값1 전달값2   # 값 사이는 공백으로 구분
# ... > threshold namecard1.jpg  외부 입력으로 실행 시 (자바에서 파이썬 exe 파일 실행시에도 필요)
if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.imshow('src', src)  # 원래 이미지 큼
# 이미지 크기 변경
src = cv2.resize(src, (600, 400))   # 이미지 크기 줄임
# src =cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
# dsize 를 이미지 배율의 기준점 지정 (0, 0) 으로 지정, fx, fy : scaling factor (크기 배율) : 1.0 이 원래 크기
cv2.imshow('src', src)  # 원래 이미지 큼

# 아무 키나 입력되면 창 닫기
cv2.waitKey()
cv2.destroyAllWindows()

# 히스토그램은 이미지의 밝기의 분포를 그래프로 표현할 수 있음
# 그레이스케일 채널 수 1개 [0], BG 색상채널이 2개이면 [0, 1], BGR 색상 채널이 3개이면 [0, 1, 2]
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
# 이미지 소스는 반드시 리스트 형태로 입력할 것 : [src]
# cv2.calcHist([image정보], 채널, 마스크 적용 여부, 사이즈, 색상 범위)
# images : 분석 대상 이미지 (uint8 or float32 type), Array 형태
# 채널 : 분석할 색상 채널 (x축 대상)
# 이미지가 grayscale 이면 [0], 칼라이면 [0], [0, 1], [0, 1, 2] 형태 (1 : Blue, 2 : Green, 3 : Red)
# mask : 이미지 분석 영역 마스크 적용 여부, None : 전체 적용
# histSize : BINS 값 [256] 히스토그램의 막대기 사이즈
# ranges : 색상 범위 [0, 256]

# plt.plot(hist)
# plt.show()

# cv2.threshold() 함수 사용 : 임계값 적용한 이진화 결과 확인
# _, src_bin = cv2.threshold(src, 130, 255, cv2.THRESH_BINARY)
# cv2.imshow('src_bin', src_bin)
# cv2.waitKey()
# cv2.destroyAllWindows()

_, src_bin = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('src_bin', src_bin)
cv2.waitKey()
cv2.destroyAllWindows()











