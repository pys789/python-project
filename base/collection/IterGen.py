# 迭代式生成器
def flatten(nested):
    # 处理字符串，将字符串当成单个元素
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten(['foo', 'abc', [4, 5, 6]])))
print(list(flatten([[1, 2], 3, [4, 5, 6]])))
