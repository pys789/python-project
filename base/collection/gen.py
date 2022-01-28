strings = ['a', 'c', 'e', 's', 'e', 'a']
for index, string in enumerate(strings):
    if 'e' in string:
        strings[index] = 'a'
print(strings)

print('------------zip------------')
names=['anne','beth','george','damon']
ages=[12,45,32,56]
for name,age in zip(names,ages):
    print(name,':',age)

print('------------推导------------')
# 简单推导
gen_list = [a * a for a in range(10) if a % 3 == 0]
print(gen_list)

gen_multi = [(x, y) for x in range(3) for y in range(3)]
print(gen_multi)

print('------------女孩和男孩匹配(首字母相同)------------')
# 女孩和男孩匹配(首字母相同)
grils = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

girlsDict = {}
girlsDict2 = {}
for girl in grils:
    girlsDict.setdefault(girl[0], []).append(girl)
    girlsDict2.setdefault(girl[0], girl)

print(girlsDict)
print([b + ',' + g for b in boys for g in girlsDict[b[0]]])

print(girlsDict2)
print([b + ',' + girlsDict2[b[0]] for b in boys])
