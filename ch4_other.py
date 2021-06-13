# other syntax

# enumerate
x = ['a', 'b', 'c', 'd']
for i, name in enumerate(x):  # 印出index和內容
    print(i, name) 

# lambda
lambda x: x+1  # 匿名函式

products = [
    ('red tea', 145),
    ('green tea', 10),
    ('milk tea', 65),
]
print(sorted(products, key = lambda x: x[1], reverse = True))

# map
x = ['aesrfbhsetjn', 'sdzfrbtfg', 'edrthrt']
print(list(map(len, x)))

# filter
x = [1, 2, 3, 4, 5]
print(list(filter(lambda i: i < 3, x)))

# zip
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))