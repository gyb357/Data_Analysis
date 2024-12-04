# %%
import numpy as np
# %%
height = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weight = np.array([86, 74, 59, 95, 80, 68])

bmi = weight/height**2
print(bmi)
# %%
score = np.array([88, 72, 93, 94, 89, 78, 99])
# score[2] -> 93
# score[-1] -> 99
# %%
ages = np.array([18, 19, 25, 30, 28])
y = ages > 20
y_ = ages[ages > 20]
print(y)
print(y_)
# %%
print(bmi[bmi > 25])
# %%
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix[0][2])
print(matrix[0, 2])
print(matrix[2, -1])

matrix[0, 0] = 12
print(matrix)

matrix[2, 2] = 1.234
print(matrix)
# %%
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15 ,16]
])
print(matrix[0:2, 2:4])
print(matrix[0])
print(matrix[1, 1:3])
# %%
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# 논리 인덱싱
print(matrix[matrix > 5])
print(matrix[:, 2])
print(matrix[:, 2] > 5)
print(matrix[:] % 2 == 0)
print(matrix[matrix % 2 == 0])
# %%
x = np.array([
    ['a', 'b', 'c', 'd'],
    ['c', 'c', 'g', 'h'],
])
# c만 추출
print(x[x == 'c'])
# %%
players = np.array([
    [170, 76.4],
    [183, 86.2],
    [181, 78.5],
    [176, 80.1]
])
# 키가 180 이상, 몸무게가 80을 넘는 선수 추출
print(players[(players[:, 0] >= 180) | (players[:, 1] > 80)])
# %%
arr = np.arange(5)
print(arr)
arr = np.arange(1, 6)
print(arr)
arr = np.arange(1, 10, 2)
print(arr)

arr = range(5)
arr = range(0, 5, 2)
arr = list(range(0, 5, 2))
arr = np.array(range(5))
print(arr)
# %%
linspace = np.linspace(0, 10, 100)
logspace = np.logspace(0, 5, 10)
print(linspace)
print(logspace)
# %%
y = np.arange(12)
y = y.reshape(3, 4)
print(y)
y = y.reshape(6, -1)
print(y)
# y = y.reshape(7, 2)
# print(y)
y = y.flatten()
print(y)
# %%
random = np.random.rand(5)
print(random)

random_matrix = np.random.rand(5, 3)
print(random_matrix)

a = 10
b = -20
print((b - a)*np.random.rand(5) + a)

random_int = np.random.randint(1, 7, 10)
print(random_int)

random_int = np.random.randint(1, 11, (2, 5))
print(random_int)

rand_n = np.random.randn(5)
print(rand_n)

rand_n = np.random.randn(5, 4)
print(rand_n)

mu = 10
sigma = 2
randoms = mu + sigma*np.random.randn(5, 4)
print(randoms)
# %%
# 평균 중앙값 계산하기
m = 175
sigma = 10
heights = m + sigma*np.random.randn(1000)
print(np.mean(heights))
print(np.median(heights))

a = np.array([3, 7, 1, 2, 21])
print(np.mean(a))
print(np.median(a))
# %%
# 선수들 100명의 데이터가 2차원 넘파이 배열에 저장되어 있다.
# 각 선수당 키, 몸무게, 나이를 저장한다
# 넘파이 배열의 이름은 player이다
# 정규 분포를 이용하여 자동으로 데이터를 생성해보자.
# 100명의 선수가 각각 키, 몸무게, 나이를 가지므로 배열의 형태는 (100, 3)
# 생성할 때 키는 175, 몸무게는 70, 나이는 22를 평균값으로 하고, 표준편차는 모두 10으로 설정한다.

player = np.random.randn(100, 3)*10 + np.array([175, 70, 22])
# print(player)

print('신장 평균: ', np.mean(player[:, 0]))
print('신장 중앙값:', np.median(player[:, 0]))
print('몸무게 평균:', np.mean(player[:, 1]))
print('몸무게 중앙값:', np.median(player[:, 1]))
print('나이 평균:', np.mean(player[:, 2]))
print('나이 중앙값:', np.median(player[:, 2]))
# %%
