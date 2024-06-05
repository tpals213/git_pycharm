# namecard\\perspective.py
# 4 단계 : 명함 이지미에서 외곽선 추출 후 외곽선 도형 모양 변형 처리 (명함을 반듯한 사각형으로)

import cv2
import numpy as np
import sys
import random

src = cv2.imread('../images/namecard1.jpg')
print(src.shape)    # (810, 1080, 3)

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400     # 결과로 만들 명함 크기 지정
# 정해진 사각형 크기에 대한 행렬(매트릭스) 만들기 : 외곽선 추출로 명함의 위치를 가지고 행렬을 만듬
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)    # 좌표값 변경 함수
dst = cv2.warpPerspective(src, pers, (w, h))    # 명함 사각형 변경 함수

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
