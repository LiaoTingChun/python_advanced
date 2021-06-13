# property
# encapsulation 封裝 : 隱瞞class內部細節

class Batman:
    def __init__(self, hp):
        self.hp = hp

    @property 
    def hp(self):
        #print('asdasd')
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp

b1 = Batman(100)
b1.hp = 150
print(b1.hp)