import re

"""
()表示捕获分组，()会把每个分组里的匹配的值保存起来，从左向右，以分组的左括号为标志，
第一个出现的分组的组号为1，第二个为2，以此类推
"""
print("-----------------捕获组()-----------------")
a = "123abc456ww"
pattern = "([0-9]*)([a-z]*)([0-9]*)"
print(re.search(pattern, a).group(0, 1, 2, 3))

print("-----------------非捕获组(?:)-----------------")
# (?:)表示非捕获分组，和捕获分组唯一的区别在于，非捕获分组匹配的值不会保存起来
pattern = "(?:[0-9]*)([a-z]*)([0-9]*)"
# (?:[0-9]*) 匹配的第一个 [0-9]*  没有保存下来，即没有保存匹配到的“123”，而([0-9]*)则保存了下来
print(re.search(pattern, a).group(0, 1, 2))

"""
(?:pattern)在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。
例如，'industr(?:y|ies)' 就是一个比 'industry|industries' 更简略的表达式
"""
a = "British industry"
pattern = "industr(?:y|ies)"
print(re.search(pattern, a).group(0))
# group(1)会报错，因为没有保存捕获到的“y”

pattern = "industr(y|ies)"
print(re.search(pattern, a).group(0, 1))

print("-----------------(?=pattern) 正向肯定预查-----------------")
"""
(?=pattern) 正向肯定预查，匹配pattern前面的位置。这是一个非获取匹配
简单说，以 xxx(?=pattern)为例，就是捕获以pattern结尾的内容xxx
预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始
"""
pattern = "Windows(?=95|98|NT|2000)"
# 能匹配"Windows2000"中的"Windows",结果为Windows
print(re.search(pattern, 'Windows2000').group(0))

pattern = "Windows(?=95|98|NT|2000)([0-9]*)"
print('Windows(?=95|98|NT|2000)([0-9]*)=', re.search(pattern, 'Windows2000').group(0, 1))

# 但不能匹配"Windows3.1"中的"Windows"
# print(re.search(pattern,'Windows3.1').group(0))

a = 'I am Windows 98ABC end'
# 消耗字符（从(?:98|2000|XP)后匹配ABC）
print(re.search("Windows (?:98|2000|XP)ABC", a).group(0))
# 不消耗字符，继续从(?:98|2000|XP)匹配ABC）,匹配失败
# print(re.search("Windows (?=98|2000|XP)ABC",a).group(0))

print("-----------------(?!pattern) 正向否定预查-----------------")
"""
(?!pattern)
正向否定预查(negative assert)，在任何不匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配
"""
pattern = "Windows(?!95|98|NT|2000)"
# Windows3.1能匹配到
print('Windows3.1 ', re.search(pattern, 'Windows3.1').group(0))
# Windows2000不能匹配到
# print('Windows2000 ',re.search(pattern,'Windows2000').group(0))


print("-----------------(?<=pattern) 反向肯定预查-----------------")
"""
(?<=pattern) 反向肯定预查，与正向肯定预查类似，只是方向相反,匹配pattern后面的位置
"""
# 能匹配 95Windows，不能匹配 3.1Windows
print(re.search('(?<=95|98|XP)Windows', '95Windows').group())

b = """
{"errorCode":0,"errorMsg":"suc","result":{"datas":[
{"Status":0,"id":8,"orderNum":1,"status":1,"title":""},
{"Status":0,"id":13,"orderNum":1,"status":1,"title":"food"},
{"Status":0,"id":11,"orderNum":2,"status":1,"title":"stock"},
{"Status":0,"id":12,"orderNum":3,"status":1,"title":"beauty"},
{"Status":0,"id":14,"orderNum":5,"status":1,"title":"baby"}
],"version":"15"},"success":true}
"""
# 合并成一行
# tt=''
# c = b.split('\n')
# for line in c:
#     tt += line.strip()
# print(tt)

print(re.findall('(?<="id":)\\d+', b))

print("-----------------(?<!pattern) 反向否定预查-----------------")
"""
(?<!pattern) 反向否定预查，与正向否定预查类似，只是方向相反,匹配pattern后面的位置
"""
# 能匹配 2000Windows，不能匹配 95Windows
print(re.search('(?<!95|98|XP)Windows', '2000Windows').group())
