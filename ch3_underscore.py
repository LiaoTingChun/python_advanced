# _
# _name
# name_
# __name
# __name__

# _
for _ in range(10): # _ 並不重要, 無需特別命名
    print('hi')

name, _ = 'name$age'.split('$') # 假如再也用不到age


# _name : 私人(不希望給外部使用), 沒有實質作用
# public, private
class Qwe: 
    def public_func(self):
        print('asdasd')
        self._private_func()

    # helper function 
    def _private_func(self): # 加底線, 但沒有實質作用
        print('asdasd')

    def _convert_data():
        pass

q = Qwe()
q.public_func()
q._private_func()


# 但如果在function定義前面加底線，有實質作用
def _ff(): # from module import * 時，會避開import這個function
    print('ni hao') 


# name_ 
x = 5
# x_ 避開已經取名過的變數, 或避免使用關鍵字


# __name
# 為了避免撞名, python直譯器對__var會重新命名
class Person:
    def __init__(self):
        self.x = 1
        self._y = 1
        self.__z = 1

p = Person()
print(p.x)
print(p._y)
print(dir(p))


# __name__ : dunder methods / magic methods
# 通常為python內建的名稱, 我們不會自己創造