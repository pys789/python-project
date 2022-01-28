# 自定义统计get调用方法调用次数的列表（继承普通list）
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


c = CounterList(range(10))
print(c)
print(c.counter)

# get调用次数加2
print(c[4]+c[2])
print(c.counter)