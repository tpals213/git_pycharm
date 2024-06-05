


# 파이썬 패키지 수입
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os
import glob

# from keras.datasets import mnist
# from keras.layers import Dense, Flatten, Reshape
# from keras.layers import LeakyReLU
# from keras.models import Sequential
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.models import Sequential


# 하이퍼 파라미터
MY_GEN = 128
MY_DIS = 128
MY_NOISE = 100

MY_SHAPE = (28, 28, 1)
MY_EPOCH = 5000
MY_BATCH = 300


# 출력 이미지 폴더 생성
MY_FOLDER = 'output/'
os.makedirs(MY_FOLDER,
            exist_ok=True)

for f in glob.glob(MY_FOLDER + '*'):
    os.remove(f)


########## 데이터 준비 ##########
# 라이브러리 중복 관련 에러 발생하면 아래의 코드를 추가함
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# 결과는 numpy의 n-차원 행렬 형식
def read_data():
    # 학습용 입력값만 사용 (GAN은 비지도 학습)
    (X_train, _), (_, _) = mnist.load_data()

    print('데이터 모양:', X_train.shape)
    plt.imshow(X_train[0], cmap='gray')
    plt.show()

    # 데이터 스케일링 [-1, 1]
    X_train = X_train / 127.5 - 1.0

    # 채널 정보 추가
    X_train = np.expand_dims(X_train, axis=3)
    print('데이터 모양:', X_train.shape)

    return X_train


########## 인공 신경망 구현 ##########


# 생성자 설계
def build_generator():
    model = Sequential()

    # 입력층 + 은닉층 1
    model.add(Dense(MY_GEN,
                    input_dim=MY_NOISE))
    model.add(LeakyReLU(alpha=0.01))

    # 은닉층 2
    model.add(Dense(MY_GEN))
    model.add(LeakyReLU(alpha=0.01))

    # 은닉층 3 + 출력층
    # tanh 활성화는 [-1, 1] 스케일링 때문
    model.add(Dense(28 * 28 * 1,
                    activation='tanh'))
    model.add(Reshape(MY_SHAPE))

    print('\n생성자 요약')
    model.summary()

    return model


# 감별자 설계
def build_discriminator():
    model = Sequential()

    # 입력층
    model.add(Flatten(input_shape=MY_SHAPE))

    # 은닉층 1
    model.add(Dense(MY_DIS))
    model.add(LeakyReLU(alpha=0.01))

    # 출력층
    model.add(Dense(1,
                    activation='sigmoid'))

    print('\n감별자 요약')
    model.summary()

    return model


# DNN-GAN 구현
def build_GAN():
    model = Sequential()

    # 생성자 구현
    generator = build_generator()

    # 감별자 구현
    # 생성자 학습시 감별자 고정
    discriminator = build_discriminator()

    discriminator.compile(optimizer='adam',
                          loss='binary_crossentropy',
                          metrics=['acc'])

    discriminator.trainable = False

    # GAN 구현: 생성자 먼저 추가, 그 다음 감별자
    model.add(generator)
    model.add(discriminator)

    # GAN은 정확도 무의미
    model.compile(optimizer='adam',
                  loss='binary_crossentropy')

    print('\nGAN 요약')
    model.summary()

    return discriminator, generator, model


########## 인공 신경망 학습 ##########


# 감별자 학습 방법
def train_discriminator():
    # 진짜 이미지 임의로 한 batch 추출
    total = X_train.shape[0]
    pick = np.random.randint(0, total, MY_BATCH)
    image = X_train[pick]

    # 숫자 1을 한 batch 생성
    all_1 = np.ones((MY_BATCH, 1))

    # 진짜 이미지로 감별자 한번 학습
    d_loss_real = discriminator.train_on_batch(image,
                                               all_1)

    # 생성자를 이용하여 가짜 이미지 생성
    # 노이즈 벡터는 표준 정규 분포를 사용
    noise = np.random.normal(0, 1,
                             (MY_BATCH, MY_NOISE))
    fake = generator.predict(noise)

    # 숫자 0을 한 batch 생성
    all_0 = np.zeros((MY_BATCH, 1))

    # 가짜 이미지로 감별자 한번 학습
    d_loss_fake = discriminator.train_on_batch(fake,
                                               all_0)

    # 평균 손실과 정확도 계산
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    return d_loss


# 생성자 학습 방법
def train_generator():
    # 노이즈 벡터는 표준 정규 분포를 사용
    noise = np.random.normal(0, 1,
                             (MY_BATCH, MY_NOISE))

    # 숫자 1을 한 batch 생성
    all_1 = np.ones((MY_BATCH, 1))

    # 가짜 이미지로 생성자 한번 학습
    g_loss = gan.train_on_batch(noise,
                                all_1)

    return g_loss


# 샘플 이미지 NxN 출력
def sample(epoch):
    row = col = 4

    # 노이즈 벡터 생성
    noise = np.random.normal(0, 1,
                             (row * col, MY_NOISE))

    # 생성자를 이용하여 가짜 이미지 생성
    fake = generator.predict(noise)

    # 채널 정보 삭제
    fake = np.squeeze(fake)

    # 캔버스 만들기
    fig, spot = plt.subplots(row, col)

    # i행 j열에 가짜 이미지 추가
    cnt = 0
    for i in range(row):
        for j in range(col):
            spot[i, j].imshow(fake[cnt], cmap='gray')
            spot[i, j].axis('off')
            cnt += 1

    # 이미지를 PNG 파일로 저장
    path = os.path.join(MY_FOLDER,
                        'img-{}'.format(epoch))
    plt.savefig(path)
    plt.close()


# GAN 학습
def train_GAN():
    begin = time()
    print('\nGAN 학습 시작')

    for epoch in range(MY_EPOCH + 1):
        d_loss = train_discriminator()
        g_loss = train_generator()

        # 매 50번 학습때마다 결과와 샘플 이미지 생성
        if epoch % 50 == 0:
            print('에포크:', epoch,
                  '생성자 손실: ', g_loss,
                  '감별자 손실: ', d_loss[0],
                  '감별자 정확도: {:.1f}%'.format(d_loss[1] * 100))
            sample(epoch)
    end = time()

    print('최종 학습 시간: {:.1f}초'.format(end - begin))


########## 컨트롤 타워 ##########


# 데이터 준비
X_train = read_data()

# GAN 구현
discriminator, generator, gan = build_GAN()

# GAN 학습
train_GAN()
