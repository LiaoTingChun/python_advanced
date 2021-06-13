# iterate 迭代

for i in [1, 2, 3]: # iterate over [1, 2, 3]
    print('hi') 


# iterables 能被迭代的物件
# list, string...

for i in 'Allen':
    print(i)


# iterator 迭代器
# stateful 會更新狀態
# 只能迭代過一次, 會耗盡
x = [1, 2, 3]
it = x.__iter__()
print(sum(it))
print(sum(it)) # 已經迭代過了, 無法再走一次
print(dir(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())

'''
it = iter(x) # 產生一個iterator
next(it) # 呼叫__next__()
'''