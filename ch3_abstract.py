# abstract class
# 抽象類別不能生成實例, 只能被繼承
# class中包含一個以上abstract method, 即為abstract class
# 改寫type, 就是在寫metaclass

from abc import ABCMeta, abstractmethod, ABC  # abstract base class

# 改用ABCMeta生成class
class Product(metaclass=ABCMeta):
    @abstractmethod
    def hi(self):
        pass

    @abstractmethod
    def hi2(self):
        pass

class Drink(Product):
    def hi(self): # override
        print('hi')

    def hi2(self): # override
        print('hi')

#p = Product()
#p = Drink()

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('bark')

class Cat(Animal):
    def make_sound(self):
        print('meow')

class Person(Animal):
    def make_sound(self):
        print('hi')

d = Dog()
d.make_sound()
c = Cat()
c.make_sound()
s = Person()
s.make_sound()

for animal in [d, c, s]:
    animal.make_sound()