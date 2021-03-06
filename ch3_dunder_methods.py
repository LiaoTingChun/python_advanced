# dunder methods

class Product:
    def __init__(self, name, price):
        self.name = name # property
        self.price = price # property

    def __str__(self): # 簡易版
        return self.name + ' $' + str(self.price)
        # return f'{self.name} ${self.price}'

    def __repr__(self): # 完整版
        return f'<Product({self.name}, {self.price})>'

    def __add__(self, other):
        if isinstance(other, str):
            self.name += other
        if isinstance(other, Product):
            return [self, other]

    def __mul__(self, other):
        re = []
        if isinstance(other, int):
            for _ in range(other):
                re.append(self)
        return re

    def print_name(self):
        print(self.name)

p1 = Product('珍奶', 60)
p2 = Product('炒麵', 80)
p = Product('milk tea', 60) # instance
p + 'sweet'


class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __getitem__(self, key):
        return self.products[key]
        
s = ShoppingCart([p1, p2])


if __name__ == '__main__':
    print(p1 + p2)
    print(p1*5)
    print(p)
    #print(repr(p))
    print(s[1])