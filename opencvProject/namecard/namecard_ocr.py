# namecard\\namecard_ocr.py
# 명함 사진에서 글자 추출

'''
Tesseract-ocr 설치하기

1. tesseract-ocr-w64-setup-5.3.3.20231005.exe 파일 다운로드
   (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe)
2. 설치 시 "Additional script data" 항목에서 "Hangul Script", "Hangul vertical script" 항목 체크,
   "Additional language data" 항목에서 "Korean" 항목 체크.
3. 설치 후 시스템 환경변수 PATH에 Tesseract 설치 폴더 추가
   (e.g.) c:\Program Files\Tesseract-OCR
4. 설치 후 시스템 환경변수에 TESSDATA_PREFIX를 추가하고,
   변수 값을 <Tesseract-DIR>\tessdata 로 설정
5. <Tesseract-DIR>\tessdata\script\ 폴더에 있는
  Hangul.traineddata, Hangul_vert.traineddata 파일을
   <Tesseract-DIR>\tessdata\ 폴더로 복사
6. 명령 프롬프트 창에서 pip install pytesseract 명령 입력
'''
import sys
import numpy as np
import cv2
import pytesseract

# 함수 만들기
def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))    # 컬럼0 --> 컬럼1 순으로 정렬한 인덱스 반환
    pts = pts[idx]    # x 좌표로 정렬

    if pts[0,1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]    # x 좌표로 정렬한 인덱스를 기준으로 pts[0]과 pts[1]을 바꿈

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]    # y 좌표로 정렬한 인덱스를 기준으로 pts[2]과 pts[3]을 바꿈

    return pts

# 명함 이미지 들어있는 사진 파일 불러오기
filename = '../images/namecard1.jpg'

# 이 파일을 실행파일로 만들어서, 외부에서 실행 시 전달인자로 이미지 파일을 전달하는 경우
if len(sys.argv) > 1:
    filename = sys.argv[1]  # 프롬프트 > 실행파일명 처리할이미지파일명.확장자

src = cv2.imread(filename)

if src is None:
    print('Image load failed!')
    sys.exit()


# 출력 영상 설정
dw, dh = 720, 400
srcQuad = np.array([[0,0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0,0], [0, dh], [dw, dh], [dw, 0]], np.float32)

# 입력 영상 전처리
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
th, src_bin = cv2.threshold(src_gray, 0,  255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출 및 명함 검출
countours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 명함 사각형 좌표값 추출
for pts in countours:
    # 너무 작은 면적의 도형 제외
    if cv2.contourArea(pts) < 10:
        continue

    # 외곽선 근사치 처리
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    # print(approx)

    # 컨백스(닫혀진 일반 다각형)가 아니고, 사각형이 아니면 제외
    if not cv2.isContourConvex(approx) or len(approx)!= 4:
        continue

    # 골라낸 컨백스에 테두리 그리기 (다각형 도형 그리기)
    cv2.polylines(src, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))

    # 명함 이지미 사각형 이미지 만들기
    per = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(src, per, (dw, dh), flags=cv2.INTER_CUBIC)

    # 명함에서 글자 추출
    dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    str = pytesseract.image_to_string(dst_rgb, lang='Hangul+eng')
    print(str)

# for closed -----------------------------------

# 처리 이미지 출력 확인
cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.imshow('dst_rgb', dst_rgb)


cv2.waitKey()
cv2.destroyAllWindows()
















