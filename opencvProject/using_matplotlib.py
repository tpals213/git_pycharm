# using_matplotlib.py
# 이미지 읽어올 때 색상 채널 변경

import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
imgRGB = cv2.imread('./images/cat.bmp') # BGR 순으로 읽어들임
imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB)
plt.axis('off')
# plt.imshow(imgBGR)
plt.imshow(imgRGB)
plt.show()

# 그레이스케일로 이미지 읽어 들이기
imgGray = cv2.imread('./images/cat.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgRGB)
plt.show()