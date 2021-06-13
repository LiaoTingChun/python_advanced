# closure

def f():
    x = 1 # enclosed
    def qqq():
        print('asdasdasd')

    class Batman:
        def __init__(self):
            print('Bat man')

    def inner():
        print(x) # local
        qqq()
        b = Batman()

    return inner 

y = f()
print(y.__closure__)
y()