# pass by value
# pass by reference
# python: pass by object reference

def f(y):
    y.append(1)

x = [0]
f(x)
print(x) # [0] or [0, 1] ?

def ff(y):
    y += 1

x = 0
ff(x)
print(x) # 0 or 1 ?