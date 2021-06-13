# @staticmethod
# @classmethod

class Batman:
    def __init__(self, hp):
        self.hp = hp

    def f(self):
        print('f')

    @staticmethod # 不需要用到class裡的東西，比如self
    def cal_avg(x):
        return sum(x)/len(x)
        f()

    @classmethod  # 暫時建立一個實例
    def fffff(cls):
        cls(100).f()

#x = [1,2,3]
#print(Batman.cal_avg(x))
#Batman.f()
Batman.fffff()