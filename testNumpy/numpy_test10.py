# numpy_test10.py

import numpy as np

# 기술 통계 (descriptive statistics) : 통계 계산용 함수를 말함
# 데이터 갯수(count), 평균(mean, average), 분산(variance), 표준편차(standard deviation)
# 최대값(maximum), 최소값(minimum), 중앙값(median), 사분위수(quantile)

x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8, 2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13])
print(x)

# 데이터 갯수 : len()
print(len(x))

# 평균 : np.mean(배열변수)
print(np.mean(x))

# 표본 분산 (sample variance) : 데이터와 평균 간의 차이의 제곱의 평균 np.var()
print(np.var(x))
print(np.var(x, ddof=1))    # 비편향분산

# 표준편차 : 표본 분산의 양의 제곱근, ss 라고 표시 np.std()
print(np.std(x))

# 최대값, 최소값, 중앙값
print(np.max(x))
print(np.min(x))
print(np.median(x))

# 사분위수(quantile) : 데이터를 크기 순서대로 정렬했을 때, 1/4, 2/4, 3/4 위치에 해당하는 값
# 1사분위, 2사분위, 3사분위, 4사분위 라고 함
# 데이터 갯수가 100개이면, 1사분위는 25번째 수가 됨
print(np.quantile(x, 0.25))
print(np.quantile(x, 0.50))
print(np.quantile(x, 0.75))
print(np.quantile(x, 1.00))

# 난수 발생과 카운팅
# 난수 (random number) : 프로세스가 임의로 발생하는 수
# numpy 의 random 서브패키지에서 함수들이 제공

# np.random.seed(인수)
# seed : 난수의 시작값
# 인수 : 정수 >= 0 사용
np.random.seed(0)   # 난수의 시작값 지정

# np.random.rand(갯수)
# 값의 범위 : 0.0 <= 값 < 1
print(np.random.rand(5))

# 데이터 섞기 (shuffle)
x = np.arange(10)
print(x)
np.random.shuffle(x)
print(x)