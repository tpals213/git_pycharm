# hello_tensor.py

# 패키지 설치 : tensorflow

# 텐서플로우 불러오기
import tensorflow as tf
import matplotlib.pyplot as plt

# 텐서플로우로 hello world 출력
msg = tf.constant('Hello, TensorFlow!')
tf.print(msg)

# MNIST (손글씨 숫자 이미지) 데이터를 훈련 데이터로 사용한 DNN 학습 예 :
# 손글씨 숫자 이미지 분류하기 --------------------------------
#  MNIST 데이터 불러오기

mnist = tf.keras.datasets.mnist

# MNist 4분할 데이터로 처리
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
print("학습용 입력 데이터 모양 : ", X_train.shape)
print("학습용 출력 데이터 모양 : ", Y_train.shape)
print("평가용 입력 데이터 모양 : ", X_test.shape)
print("평가용 출력 데이터 모양 : ", Y_test.shape)

# 손글씨 숫자 이미지 원본 출력

plt.imshow(X_train[0], cmap='gray')
plt.show()

print('첫번째 학급용 입력 데이터 확인 :', X_train)
print('첫번째 학급용 출력 데이터 확인 :', Y_train)

# 이미지 데이터 [0, 1] 스케일링 : 연산할 각 픽셀의 값의 범위를 축소 시킴 [0, 255] => [0, 1] 로 바꿈
X_train = X_train / 255.0   # 픽셀의 127번 색상값은 0.5 정도가 될 것임
X_test = X_test / 255.0

# 스케일링 후 데이터 확인
plt.imshow(X_train[0], cmap='gray')
plt.show()

print('첫번째 학습용 입력 데이터 확인 : ', X_train[0])

# 인공 신경망 구현
model = tf.keras.models.Sequential()
layers = tf.keras.layers

model.add(layers.Flatten(input_shape=(28, 28)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(10, activation='softmax'))

# 인공신경망 요약
model.summary()

# 인공신경망 학습(훈련) 환경 설정
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 인공 신경망 학습 (훈련)
model.fit(X_train, Y_train, epochs=5)   # 훈련 횟수 5번

# 인공 신경망 평가
model.evaluate(X_test, Y_test)

# 인공 신경망 예측
pick = X_test[0].reshape(1, 28, 28)
pred = model.predict(pick)
answer = tf.argmax(pred, axis=1)

print('인공신경망 추측 결과 (원본) : ', pred)
print('인공신경망 추측 결과 (해석) : ', answer)
print('정답 : ', Y_test[0])