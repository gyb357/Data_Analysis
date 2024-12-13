# %%
print(3+5)

# %%
number = 0
for score in [90, 25, 67, 45, 93]:
    number = number + 1
    if score >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")

# %%
number = 0
for i in range(1, 10+1):
    number += i

print(number)

# %%
number = 0
for i in range(500, 1000+1):
    if i % 2 == 1:
        number += i

print(number)

# %%
number = 0
for i in range(1, int(input(''))+1):
    number += i

print(number)

# %%
start = int(input('시작 숫자를 입력하세요: '))
end = int(input('끝 숫자를 입력하세요: '))
increment = int(input('증가폭을 입력하세요: '))
number = 0

# 2에서 300까지 3씩 증가하면서 더하기
for i in range(start, end+1, increment):
    number += i

print(number)

# %%
# 구구단 출력
inputs = int(input('몇 단을 출력할까요? '))
for i in range(1, 9+1):
    print(f"{inputs} x {i} = {inputs*i}")

# %%
# 이중 for문을 이용한 구구단 출력
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f"{i} x {j} = {i*j}")
    print()

# %%
# while True:
    # print('Ctrl + C를 눌러야 종료됩니다.')

# %%
first = int(input('첫 번째 숫자를 입력하세요: '))
second = int(input('두 번째 숫자를 입력하세요: '))
print(f"{first} + {second} = {first+second}")

# %%
