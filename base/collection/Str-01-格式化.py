import math

formatStr = 'Hello %s,this is %d'
values = ('world', 10)
print(formatStr % values)

print('{} world,this is {}'.format('world', 10))
print('{0} world,this is {1},{0}'.format('world', 10))
print('{name} world,this is {num},{num}'.format(name='world', num=10))
print('{foo} {1} {bar} {0}'.format(1, 2, bar=4, foo=3))

# 设置格式完整版
# 字段名（索引或标识符）!转换标志（跟在感叹号后面\r,\s,\a）:格式说明符(跟在冒号后面的表达式)
print('{pi!s} {pi!r} {pi!a}'.format(pi='π'))

# 指定宽度
print('----------------指定宽度，精度和填充----------------')
print("test {num:5}".format(num=3))
print("test {name:5}".format(name='pys'))
# 指定精度
print('{pi:.2f}', ' is {pi:.2f}'.format(pi=math.pi))
# 指定宽度和精度
print('{pi:10.2f}', ' is {pi:10.2f}'.format(pi=math.pi))
# 使用0填充，指定宽度和精度,保留10位数
print('{0:010.2f}', 'is {0:010.2f}'.format(math.pi))

print('----------------对齐方式----------------')
# 左对齐
print('{0:<10.2f}'.format(math.pi))
# 居中
print('{0:^10.2f}'.format(math.pi))
# 右对齐
print('{0:>10.2f}'.format(math.pi))

print('----------------填充和设置前缀----------------')
# 使用填充字符来扩充对齐说明符，默认是空格
print('{:#^20}'.format(" WIN BIG "))
# 使用=，指定填充字符放在符号和数字之间
print("{0:10.2f}\n{1:10.2f}".format(math.pi, -math.pi))
print("{0:10.2f}\n{1:=10.2f}".format(math.pi, -math.pi))
# 指定精度前缀，给正数加上+
print('{0:-.2},{1:-.2}'.format(math.pi, -math.pi))
print('{0:+.2},{1:-.2}'.format(math.pi, -math.pi))
print('{0: .2},{1: .2}'.format(math.pi, -math.pi))

print('----------------井号(#)选项----------------')
# 井号(#)选项，用在符号说明符和宽度之间（如果指定了这两种设置），会触发另一种转换方式
print('{:b}'.format(42))
# 加上井号，会加上二进制前缀
print('{:#b}'.format(42))

print('----------------字符串格式设置示例----------------')

width = 35
price_width = 10
item_width = width - price_width

# header_fmt='{:25}{:>10}'
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
# fmt='{:25}{:>10.2f}'
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)

print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))

print('=' * width)

print(header_fmt)
print(fmt)
