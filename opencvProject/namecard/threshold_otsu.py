# namecard\\threshold_otsu.py
# 2단계 : 명함 이미지 이진화 처리를 위한 threshold 연산 다중 적용 경우

import sys
import cv2

filenames = ['../images/namecard1.jpg', '../images/namecard2.jpg', '../images/namecard3.jpg', '../images/namecard.jpg']

for filename in filenames:
    src =cv2.imread(filename, cv2.IMREAD_COLOR) # BGR 로 읽음

    if src is None:
        print('Image load failed!')
        sys.exit()

    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    # 이진화를 위해 그레이스케일로 변환
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 이진화 처리
    th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print('Threshold value : ', th)
    te = cv2.adaptiveThreshold(src_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    cv2.imshow('te', te)
    cv2.imshow('src', src)
    cv2.imshow('src_gray', src_gray)
    cv2.imshow('src_bin', src_bin)
    cv2.waitKey()

cv2.destroyAllWindows()