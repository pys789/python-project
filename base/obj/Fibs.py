class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

# 找出第一个大于1000的斐波数
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
