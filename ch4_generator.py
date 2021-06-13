# generator
# generator回傳iterator
'''
def g():
    while True:
        yield 1

print(next(g()))

def my_range(n):
    i = 0
    while i < n:
        print(f'準備生成{i}')
        yield i
        i += 1

# 可節省記憶體
for i in my_range(5):
    print(i)

# generator expression
x = [0, 1, 2, 3, 4]
it1 = (i**2 for i in x)
it2 = (i+2 for i in it1)
print(next(it2))
print(next(it2))
print(next(it2))
'''

def gen(n):
    i = 0
    for i in range(n):
        print(f'生成{i}')
        yield i
it = gen(10)
for i in it:
    print(i)