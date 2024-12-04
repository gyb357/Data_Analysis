# %%
def sum1(a, b):
    return a + b

def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x
# %%
print(abs(-3.5))
print(all([1, 2, 3, 4]))
print(any([1, 2, 3, 4]))
print(chr(97))
print(ord('c'))
print(divmod(7, 3))
print(oct(8))
print(hex(15))
print(id('a'))
print(int('3'))
print(int(3.5))
print(str(3))
print(list('python'))
print(tuple('python'))
print(type('abc'))

a = 1
print(type(a))

# %%
add = lambda x, y: x + y
print(add(3, 4))
# %%
print(max([1, 4, 2, 6, 9]))
print(min([1, 4, 2, 6, 9]))
print(pow(2, 3))
print(c = input())
# %%
print(range(5))
print(range(0, 5))
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))
# %%
print(len('python'))
# %%
print(sorted([9, 4, 8, 1]))
print(sorted('python'))
# %%
def add3(a, b):
    return a + b

def sub(a, b):
    return a - b
