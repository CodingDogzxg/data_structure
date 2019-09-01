# author:CodingDog

class MyQueue:

    def __init__(self, queue_capacity):  # 初始化队列
        self.queue_capacity = queue_capacity  # 队列容积
        self.q_length = 0  # 元素个数
        self.q_head = 0  # 队头
        self.q_tail = 0  # 队尾
        self.queue = []  # 队列

    def destroy_queue(self):  # 释放队列内存
        pass

    def clear_queue(self):  # 清空队列
        self.__init__(0)

    def queue_empty(self):  # 判断队列是否为空
        return True if self.q_length == 0 else False

    def queue_full(self):  # 判断队列是否为满
        return True if self.q_length == self.queue_capacity else False

    def len_queue(self):  # 测量队列的长度
        return self.q_length

    def enter_elements(self, element):  # 插入元素 队尾向后移动 因为插入位置永远是队尾
        if self.queue_full():
            return False
        elif not self.queue_full():
            self.queue.insert(self.q_tail, element)
            self.q_tail += 1
            self.q_tail = self.q_tail % self.queue_capacity  # 避免队尾下标超过队列容量
            self.q_length += 1

    def remove_elements(self):  # 剔除元素 队头向后移动 因为剔除的元素永远是队头
        if self.queue_empty():
            return False
        elif not self.queue_empty():
            self.queue[self.q_head] = None  # 占据索引位置 避免剔除元素之后遍历出错
            self.q_head += 1
            self.q_head = self.q_head % self.queue_capacity  # 避免队头下标超过队列容量
            self.q_length -= 1

    def for_queue(self):  # 遍历栈元素
        for n in range(self.q_head, self.q_head + self.q_length):
            print(self.queue[n % self.queue_capacity])


if __name__ == '__main__':
    a = MyQueue(4)
    a.enter_elements(1)
    a.enter_elements(2)
    a.for_queue()
    print('---')
    a.enter_elements(3)
    a.enter_elements(4)
    a.enter_elements(5)
    a.for_queue()
    print('---')
    a.remove_elements()
    a.for_queue()
    a.remove_elements()
    a.remove_elements()
    a.remove_elements()
    a.for_queue()
    print("---")
    a.enter_elements('another')
    a.enter_elements('another 2')
    a.for_queue()
    print("---")
