# decorator

import time

def print_func(func): # 寫一個decorator
    def inner():
        print('running', func.__name__)
        func()
    return inner


def time_func(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('elapsed', end-start, 'seconds')
    return inner


@print_func # 等於test = print_func(test)
@time_func # 會先被鄰近的time_func修飾
def test():
    for i in range(1000000):
        i += 1
    print('hi')


def test2():
    print('ni hao')

#test = print_func(test) # test 被print_func修飾
#test = time_func(test) # inner 再被time_func修飾

test()