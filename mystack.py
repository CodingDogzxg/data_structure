# author:CodingDog

class MyStack:

    def __init__(self, stack_capacity):  # 初始化栈
        self.stack_capacity = stack_capacity
        self.s_top = 0  # 栈顶
        self.stack = []  # 栈

    def destroy_stack(self):  # 释放栈内存
        pass

    def clear_stack(self):  # 清空栈
        self.__init__(0)
        # self.s_top = 0 可以将top赋值为0 下一次使用栈直接覆盖

    def stack_empty(self):  # 判断栈是否为空
        return True if self.s_top == 0 else False

    def stack_full(self):  # 判断栈是否为满
        return True if self.s_top == self.stack_capacity else False

    def len_stack(self):  # 测量栈的长度
        return self.s_top

    def enter_elements(self, element):  # 插入元素 栈顶向上移动 总是插入在栈顶
        if self.stack_full():
            return False
        elif not self.stack_full():
            self.stack.insert(self.s_top, element)
            self.s_top += 1

    def remove_elements(self):  # 剔除元素 栈顶向下移动 总是剔除栈顶的元素
        if self.stack_empty():
            return False
        elif not self.stack_empty():
            self.stack.pop()
            self.s_top -= 1

    def for_stack(self, is_from_bottom=True):  # 遍历栈元素
        if is_from_bottom:  # 自栈底遍历
            for n in range(0, self.s_top):
                print(self.stack[n])
        if not is_from_bottom:  # 自栈顶遍历
            n = self.s_top
            for x in range(0, self.s_top):
                print(self.stack[n - 1])
                n -= 1


if __name__ == '__main__':
    a = MyStack(4)
    a.enter_elements(1)
    a.enter_elements(2)
    a.for_stack(False)
    print('---')
    a.enter_elements(3)
    a.enter_elements(4)
    a.enter_elements(5)
    a.for_stack(False)
    print('---')
    a.remove_elements()
    a.for_stack()
    a.remove_elements()
    a.remove_elements()
    a.remove_elements()
    a.for_stack()
    print("---")
    a.enter_elements('another')
    a.enter_elements('another 2')
    a.for_stack()
    print("---")