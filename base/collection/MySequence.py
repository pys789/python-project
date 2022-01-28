def checkIndex(key):
    if key < 0:
        raise IndexError
    if not isinstance(key, int):
        raise TypeError

# 通过定义 __len__,__getitem__,__setitem__,__delitem__几个魔法方式自定义序列
# 如果索引对应的值没有修改，通过start，step计算值，如果已经更改，使用更改后的值
class MySequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        # try:
        #     return self.changed[key]
        # except:
        #     return self.start + key * self.step
        if self.changed.get(key) is None:
            return self.start + key * self.step
        else:
            return self.changed.get(key)

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


seq = MySequence(1, 2)
print(seq[4])
seq[4] = 2
print(seq[4])
print(seq[5])
