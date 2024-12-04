# %%
from _2024_10_02_00 import add3, sub

print(add3(3, 4))
print(sub(3, 4))
# %%
import sys
print(sys.path)
# %%
# sys.path.append('c:/python')
# print(sys.path)
# %%
partyA = set(['Park', 'Kim', 'Lee'])
partyB = set(['Park', 'Choi', 'Jung'])
print(partyA)
print(partyB)

# 2개의 파티에 모두 참석한 사람
print(partyA & partyB)
print(partyA.intersection(partyB))
# %%
a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7]

# 중복 숫자 제거
b = set(a)
print(b)
# %%
f = open('text.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
# %%
f = open('text.txt', 'r', encoding='utf-8')

lines = f.read()
print(lines)
f.close()

# lines = f.readlines()
# for line in lines:
    # line = line.strip()
    # print(line)
# f.close()

# while True:
    # line = f.readline()
    # if not line:
        # break
    # print(line)
# f.close()

# line = f.readline()
# print(line)
# f.close()
# %%
f = open('text.txt', 'a', encoding='utf-8')
for i in range(11, 21):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()
# %%
