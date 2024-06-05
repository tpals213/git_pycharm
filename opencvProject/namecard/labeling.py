# namecard\\labeling.py
# 이미지 입력 => 그레이스케일로 입력 => 이진화 작업(검정, 흰색) : threshold => 라벨링 처리

import cv2
import numpy as np
import sys
import random

src = cv2.imread('../images/coins.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


# w (width : 가로 => 열), h (height : 세로 => 행) ==> h(행), w(열)
print('src.shape : ', src.shape)    # 해상도 (246, 300)
h, w = src.shape[:2]    # [begin : end] => begin 부터 end -1 위치까지 추출
# [:2] == [0 : 2] == 0, 1 추출 => 인덱스 0의 값 246이 h 에 대입, 인덱스 1의 값 300은 w에 대입
print('h : ', h)
print('w : ', w)

# 3차원 행렬(매트릭스) 만들기 : 각 픽셀에 표시할 레이블(숫자) 기록용 행렬을 준비하는 것
dst1 = np.zeros((h, w, 3), np.uint8)  # 각 픽셀에 기록할 숫자의 자료형 1바이트 비부호 정수, 기본 0
dst2 = np.zeros((h, w, 3), np.uint8)  # unit8 : unsigned 8 bit int, 0 ~ 255 정수만 사용
# int8 : 정수 8비트 (-128 ~ -1, 0, 1 ~ 127), uint8 : 0 ~ 255
print(type(dst1))
# print(dst1)

# 전처리 (pre-processing)
# print('blur before ---------------------------------')
# print(src)

# 검정(0)과 흰색(1)으로 바꾸는 이진화 처리
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)
# print('src_bin : ', src_bin)

# 레이블링 : 흰색 영역별 픽셀에 랜덤값으로 색상을 만들어서 추출된 픽셀 위치에 색상값 기록
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
# print('cnt : ', cnt)
# print('labels : ', labels)    # 16개로 구분된 코인(흰색 영역) 영역 표시
# print('labels.shape : ', labels.shape)
# print('stats : ', stats)
# print('centroids : ', centroids)

for i in range(1, cnt):
    # 랜덤하게 rgb 색을 만듦
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # 라벨링을 위해 준비된 행렬에 추출된 코인(흰색 영역) 부분에 색을 칠함(라벨링)
    dst1[labels == i] = random_color
print('dst1 : ', dst1)

# 외곽선 검출
countours, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# print(type(countours))
# print(len(countours))   # 외곽선에 해당되는 픽셀의 위치값들 [[(y행, x열)], [], []...]

# 외곽선에 해당되는 픽셀에 색을 지정함 : dst2 에 외곽선 색 저장
for i in range(len(countours)): # 각 외곽선 픽셀에 색칠함
    # 랜덤하게 rgb 색 만듦
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst2, countours, i, random_color, 3)   # 테두리선 그리기

# 각 단계별 이미지 처리 결과 확인
cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()






