import cv2

# OpenCV의 얼굴 감지기(CascadeClassifier) 초기화
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 비디오 스트림을 캡처
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # 프레임 읽기

    if not ret:  # 프레임 읽기 실패 시 종료
        print('프레임을 읽을 수 없습니다.')
        break

    # 그레이스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 감지된 얼굴 주위에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 화면에 출력
    cv2.imshow('frame', frame)

    # ESC 키 입력 시 종료
    if cv2.waitKey(1) == 27:
        break

# 종료
cap.release()
cv2.destroyAllWindows()
