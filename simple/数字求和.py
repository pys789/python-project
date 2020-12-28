# 常规方法
# num1 = input("请输入第一个数:")
# num2 = input("请输入第二个数:")
#
# sum = float(num1)+float(num2)
# print('{0}+{1}={2}'.format(num1,num2,sum))

#方法一
#print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))

#方法二
print('两数之和为 {:.1f}'.format(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))