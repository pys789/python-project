# 给list切片赋值
nameStr=list('Perl')
nameStr[3:]=list('python')
print(nameStr)

# 使用空的列表替换，间接实现删除
numbers=[1,2,3,4,5]
numbers[1:4]=[]
print(numbers)

# 列表方法
lst=[1,2,3]
lst.append(1)
print(lst)

print(lst.count(1))

print('x=[1,2,3,1]')
x=[1,2,3,1]
print('x.pop()=',x.pop())
print('x.remove(1)=',x.remove(1))
print(x)

print('list排序')
a=[2,4,6,1,2,7]
b=sorted(a)
print(b)
print(a)
