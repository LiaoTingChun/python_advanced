from ch3_dunder_methods import Product # parent class

# child class / derived class
class Drink(Product):
    # override
    def __init__(self, name, price, volume):
        super().__init__(name, price) # 繼承parent class的__init__
        self.volume = volume


# type()會創造出一個class實例
# 用class()做出自己的實例
# type是object的實例
# object -> type -> class

d = Drink('珍奶', 80, 600)
#print(d.name)
print(d.volume)
print(type(d))
print(type(Drink))
print(isinstance(d, Drink))
print(isinstance(d, Product))
print(isinstance(Drink, type))
print(isinstance(type, object))
print(isinstance(Drink, object))

Food = type('Food', (Product,), {})
f = Food('義大利麵', 220)
print(type(f))


# metaclass (class的上一級)
# 決定class如何生成 (framework等級)