'''
虽然return和yield两者执行的顺序有区别，但整个要做的事情是一样的，
所以使用yield并不会比return快，甚至我们可以猜测由于yield总发生上下文切换在速度上还会慢一些，所以速度不是yield的意义。

他们的主要区别是yiled要迭代到哪个元素那个元素才即时地生成，而return要用一个中间变量result_list保存返回值，
当result_list的长度很长且每个组成元素内容很大时将会耗费比较大的内存，此时yield相对return才有优势
'''
class TestYield:
    def gen_iterator(self):
        for j in range(3):
            print(f"do_something-{j}")
            # yield在for循环内部
            yield j

    def call_gen_iterator(self):
        # yield并不是直接返回[0,1,2]，执行下边这句后result_list什么值都没有
        result_list = self.gen_iterator()
        # i每请求一个数据，才会触发gen_iterator生成一个数据
        for i in result_list:
            print(f"call_gen_iterator-{i}")

if __name__ == "__main__":
    obj = TestYield()
    obj.call_gen_iterator()





