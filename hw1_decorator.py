# 作業1-練習寫Decorator

def modify_error(func):
    def inner(n, d):
        if d == 0:
            return 0
        else:
            return func(n, d)
    return inner

@modify_error
def divide(n, d):
    return n/d

print(divide(5, 5))
print(divide(2, 0))