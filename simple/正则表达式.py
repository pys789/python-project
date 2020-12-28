import re

#分组匹配
line = "Cats are smarter than dogs"

#可以直接match，也可以先compile定义pattern
#matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
pattern = re.compile(r'(.*) are (.*?) .*')
matchObj = pattern.match(line)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

#match与search的区别
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")



