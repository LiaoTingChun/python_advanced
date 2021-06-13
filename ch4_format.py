# string formatting

name = 'Allen'
x = 10
y = 3.14

# 以前常用寫法
print('hi %s' % name)
print('hi %d' % x)
print('hi %f' % y)
print('hi %s, my number is %d' % (name, x))


# 使用format(), 不須告知要填入何種data type
print('hi {}, my number is {}'.format(name, x))


# python 3.6+ f-string
print(f'hi {name}, my number is {x}')


# 印出固定長度字元

print(f'hi {name:>10}, my number is {x}') # 往右對齊