try:
    a=1/0
except ZeroDivisionError:
    # 继抛出使用raise
    #  raise
    # 使用raise...from...语句提供自己的异常上下文,也可使用None禁用异常上下文
    # raise ValueError from None
    print('error')
finally:
    print('ZeroDivisionError deal over')

while True:
    try:
        x=int(input('Enter the first num: '))
        y=int(input('Enter the second num: '))
        value=x/y
        print('x/y is',value)
        # 捕获所有异常
    except:
        print('Invalid input.')
        # 正常执行的代码
    else:
        print('It is OK.')
        break



