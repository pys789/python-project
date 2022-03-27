class TestReturn:
    def gen_iterator(self):
        result_list = []
        for j in range(3):
            print(f"gen_iterator-{j}")
            result_list.append(j)
        # return在循环的外部，待变量完全生成后一次性返回
        return result_list

    def call_gen_iterator(self):
        # 执行下边这句后result_list直接是完成的结果[0,1,2]
        result_list = self.gen_iterator()
        for i in result_list:
            print(f"call_gen_iterator-{i}")

if __name__ == "__main__":
    obj = TestReturn()
    # 一次性执行完下层函数，生成完整的迭代器类型返回值result_list，一次性返回给上层函数
    obj.call_gen_iterator()



