print('----------list切片numbers=[1,2,3,4,5,6,7,8,9,10]----------')
numbers=[1,2,3,4,5,6,7,8,9,10]
print("numbers[7:10]=",numbers[7:10])
print('numbers[-3:-1]=',numbers[-3:-1])
print('numbers[3:]=',numbers[3:])
print('numbers[:-2]=',numbers[:-2])
print('numbers[0:10:2]=',numbers[0:10:2])
print('numbers[::4]=',numbers[::4])
print('numbers[::-2]=',numbers[::-2])

print('----------list切片操作----------')
print('[1,2,3]+[4,5,6]=',[1,2,3]+[4,5,6])
print('Hello,+'+'World=','Hello,'+'World')
print('python*3=','python'*3)
print('[None]*10=',[None]*10)


print('-------打印内容在屏幕中央-------')
# sentence=input("Sentence: ")
sentence='abcdefg'
screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-box_width)//2

print()
print(' '*left_margin,'+','-'*(box_width-2),'+')
print(' '*left_margin,'|',' '*(box_width-2),'|')
print(' '*left_margin,'|','  '+sentence+'  ','|')
print(' '*left_margin,'|',' '*(box_width-2),'|')
print(' '*left_margin,'+','-'*(box_width-2),'+')

print('list 的函数:funList=[100,34,678]')
funList=[100,34,678]
print('len(funList)=',len(funList))
print('max(len(funList)=',max(funList))
print('min(len(funList)=',min(funList))
print('hello字符串转list',list('hello'))



