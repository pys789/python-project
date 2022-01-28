# 使用format_map格式化字符串
template='Hello {name},I am {age}'
data={'name':'world','age':'21'}
print(template.format_map(data))

# dict简单操作
d={}
d.setdefault('name','N')
print(d)
d['name']='ppp'
print(d)
d.setdefault('name','N')
print(d)

print(d.get('name'))
print(d.get('age',20))