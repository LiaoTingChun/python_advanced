# coding style

x = 5 # this is a comment

'''
多行註解
可以使用3個單(雙)引號

'''

# docstring
# 寫在class, function的一開始, 會被python視為說明書，用__doc__取得字串

class Batman:
    """A tool to .....

    A longer description......
    """
    pass

print(Batman.__doc__)