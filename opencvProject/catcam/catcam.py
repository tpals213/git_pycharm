# catcam\\catcam.py
# 카메라를 통해 들어오는 영상에서 얼굴을 인식해서, 머리에 고양이 귀 그림 오버레이 처리

import cv2
import sys
import numpy as np

# 오버레이 처리 함수
# 영상 프에임 이미지, 고양이 귀 이미지, 고양이 귀 표시할 위치 정보 전달 받아서 오버레이 후 출력 처리
def overlay(frame, cat, pos):
    if pos[0] < 0 or pos[1] < 0 :
        return

    if pos[0] + cat.shape[1] > frame.shape[1] or pos[1] - cat.shape[0] > frame.shape[0] :
        return

    sx = pos[0]
    ex = pos[0] + cat.shape[1]
    sy = pos[1]
    ey = pos[1] + cat.shape[0]

    img1 = frame[sy:ey, sx:ex]  # shape = (h, w, 3), 얼굴 픽셀을 슬라이싱해서 저장함
    img2 = cat[:, :, 0:3]   # 고양이 그림을 슬라이싱해서 저장 (고양이 그림 전체 선택)
    alpha = 1. - (cat[:, :, 3] / 255.)      # shape = (h, w)

    # 고양이 귀 외 부분에 대한 투명도 처리 (얼굴이 가려지지 않게 함)
    img1[:, :, 0] = (img1[:, :, 0] * alpha + img2[:, :, 0] * (1. - alpha)).astype(np.uint8)
    img1[:, :, 1] = (img1[:, :, 1] * alpha + img2[:, :, 1] * (1. - alpha)).astype(np.uint8)
    img1[:, :, 2] = (img1[:, :, 2] * alpha + img2[:, :, 2] * (1. - alpha)).astype(np.uint8)


# overlay 함수 --------------------------------

# 영상 이미지에서 얼굴을 인식하는 ai 학습 모델 (텐서플로우에서 제공한 모델 다운받은 것)
model = 'opencv_face_detector_uint8.pb'
config = 'opencv_face_detector.pbtxt'

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('카메라를 열 수 없습니다.')
    sys.exit()

# opencv 가 제동하는 dnn 사용
net = cv2.dnn.readNet(model, config)
if net.empty():
    print('dnn 모델을 읽을 수 없습니다.')
    sys.exit()

# 고양이 귀 그림 읽어오기
cat = cv2.imread('cat.png', cv2.IMREAD_UNCHANGED)
if cat is None:
    print('고양이 귀 이미지를 읽을 수 없습니다.')
    sys.exit()

# 영상에서 얼굴 인식 출력 확인
while True:
    ret, frame = cap.read()
    if not ret:
        print('프레임을 읽을 수 없습니다.')
        break

    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (107, 177, 123))
    net.setInput(blob)
    detect = net.forward()  # ai 실행
    # print(detect, detect.shape)

    (h, w) = frame.shape[:2]
    detect = detect[0, 0, :, :]

    # 얼굴 위치에서 계산 처리
    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            continue

        x1 = int(detect[i, 3] * w + 0.5)
        y1 = int(detect[i, 4] * h + 0.5)
        x2 = int(detect[i, 5] * w + 0.5)
        y2 = int(detect[i, 6] * h + 0.5)

        # 고양이 귀 그림 표시할 위치를 얼굴 위치에서 계산 처리
        fx = (x2 - x1) / cat.shape[1]
        cat2 = cv2.resize(cat, (0, 0), fx=fx, fy=fx)    # 고양이 귀 그림을 프레임의 얼굴 크기에 맞춤
        pos = (x1, y1 - (y2 - y1) // 4)


        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0))   # 얼굴 위치에 초록색 사각형 선 표시
        overlay(frame, cat2, pos)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()