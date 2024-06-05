import cv2
import numpy as np
import sys
import random

filenames = ['../images/namecard1.jpg', '../images/namecard2.jpg', '../images/namecard3.jpg', '../images/namecard.jpg']

for filename in filenames:
    src =cv2.imread(filename, cv2.IMREAD_COLOR) # BGR 로 읽음

    if src is None:
        print('Image load failed!')
        sys.exit()

    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    # 이진화를 위해 그레이스케일로 변환
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 이미지의 가로 세로 크기 행렬 변환
    h, w = src_gray.shape[:2]

    # 레이블링과 외곽선 저장용 삼차원 행렬 만들기
    dst1 = np.zeros((h, w, 3), np.uint8)
    dst2 = np.zeros((h, w, 3), np.uint8)

    # 이진화 처리
    _, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    te = cv2.adaptiveThreshold(src_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # 외곽선 검출 : mode 다르게 해서 2가지 추출
    countour1, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    countour2, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    countour3, _ = cv2.findContours(te, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    countour4, _ = cv2.findContours(te, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # 외곽선 그리기
    '''
    for i in range(len(countour1)):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst1, countour1, i, random_color, 3)

    for i in range(len(countour2)):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst2, countour2, i, random_color, 3)

    for i in range(len(countour3)):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst1, countour3, i, random_color, 3)

    for i in range(len(countour4)):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst2, countour4, i, random_color, 3)
    '''

    # 외곽선 그리기 & 좌표값 뽑아내기
    for i in range(len(countour1)):
        pts = countour1[i]
        # print(pts)  # 외곽선 좌표값 확인

        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst1, countour1, i, random_color, 2)

        # 면적이 너무 작은 객체는 제외
        if cv2.contourArea(pts) < 1000:
            continue    # 아래 내용 실행하지 말고 다음 인덱스의 외곽선으로 넘어가라. 위로 올라가는 작업

        # 외곽선 근사화 : 0.02 오차 범위 지정
        approx = cv2.approxPolyDP(pts, 0.02 * cv2.arcLength(pts, True), True)

        # 근사화된 외곽선을 그리기
        cv2.drawContours(dst2, [approx], 0, (0, 0, 255), 3)

        # 닫혀진 사각형(컨벡스)이 아니면 제외
        if not cv2.isContourConvex(approx):
            continue

        # 사각형이면 외곽선 그려라
        if len(approx == 4) :
            cv2.drawContours(dst2, countour1, i, random_color, 2)
            # 좌표값 추출
            extLeft = tuple(pts[pts[:,:,0].argmin()][0])
            extRight = tuple(pts[pts[:,:,0].argmax()][0])
            extTop = tuple(pts[pts[:,:,1].argmin()][0])
            extBot = tuple(pts[pts[:,:,1].argmax()][0])
            print(extLeft, extRight, extTop, extBot)

    cv2.imshow('src', src)
    cv2.imshow('src_bin', src_bin)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)

    cv2.waitKey()
    cv2.destroyAllWindows()