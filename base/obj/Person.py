class Person:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def greet(self):
        print('Hello,world! I am {}'.format(self.name))
def fun():
    print('I am normal function')

foo=Person()
bar=Person()

foo.set_name('Luck')
#  可以看成是 bar.set_name('Anakin')
Person.set_name(bar,'Anakin')

# foo.greet() 可以看成是 Person.greet(foo) 的缩写
foo.greet()
Person.greet(bar)

print(foo.get_name())
print(bar.get_name())

# 重新设置name
bar.name='pys'
bar.greet()
# 可以将方法关联到一个普通函数
bar.greet=fun
bar.greet()

