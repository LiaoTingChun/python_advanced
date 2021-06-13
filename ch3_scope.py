# scope 範圍
# 查找name的順序: LEGB rule
# 低層不能對高層寫入(改變)，只能讀取
# 可用global, nonlocal語法改變x

# x = 1 # global x
def f():
    x = 1 # enclosed scope
    def ff():
        nonlocal x
        x = 10 # local scope
    ff()
    print(x)
f()
# print(x)

def f1():
    x = 5

f() # 執行期間local namespace才存在 (life cycle)
print(x) # 無法拿到x