import re

"""
基本函数：
compile(pattern):编译正值表达式
search(pattern,string):在字符串中查找模式（返回匹配字符串）
match(pattern,string):在字符串开头匹配模式（返回布尔值）
split(pattern,string,[maxsplit=0]):根据模式来分割字符串
findall(pattern,string):返回一个列表，其中包含字符串中所有与模式匹配的字符串
sub(pat,repl,string,[count=0]):将字符串中与模式pat匹配的字符串都替替换成repl
escape(string):对字符串中所有的正则表达式特殊字符都进行转义
"""

print("--------------使用正则分割字符串--------------")
# split 使用正则分割字符串(逗号和空格)
print(re.split('[, ]+', 'alpha,beta,,,gamma  delta'))
