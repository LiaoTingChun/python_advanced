# namespace
# 不同的命名空間 LEGB
# Built-in Namespace
# Module: Global Namespace 全域(file level)
# Function: Local Namespace 區域

import ch3_namespace2
print(ch3_namespace2.x)
from ch3_namespace2 import f

x = 5
y = 10
f()
def f():
    x = 1# enclosed namespace
    def ff():
        x = 5

def qwe():
    q = 1

# Global: {x:5, y:10, f:func, qwe:func}
# Enclosed: {x:1}
# Local: {x:5, q:1}