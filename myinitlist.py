# author:CodingDog

class MyList:

    def __init__(self, list_capacity):  # 初始顺序表
        self.list_capacity = list_capacity  # 顺序表容积
        self.l_length = 0  # 顺序表长度
        self.list = []  # 顺序表

    def destroy_list(self):  # 释放顺序表内存
        pass

    def clear_list(self):  # 清空顺序表
        self.__init__(0)

    def list_empty(self):  # 判断顺序表是否为空
        return True if self.l_length == 0 else False

    def list_full(self):  # 判断顺序表是否为满
        return True if self.l_length == self.list_capacity else False

    def len_list(self):  # 测量顺序表的长度
        return self.l_length

    def get_elements(self, subscript):  # 获取顺序表内指定下标的元素
        if subscript < 0 or subscript >= self.l_length:
            return False
        elif not subscript < 0 or subscript >= self.l_length:
            print(self.list[subscript])
            return True

    def locate_element(self, element):  # 定位顺序表内制定元素的下标
        for i in range(0, self.l_length):
            if self.list[i] == element:
                return i
            elif i == self.l_length -1:
                return -1

    def prior_element(self, current_element):  # 获取顺序表内制定元素的前驱
        temp = self.locate_element(current_element)
        if temp == -1 or temp == 0:
            return False
        else:
            print(self.list[temp - 1])
            return True

    def next_element(self, current_element):  # 获取顺序表内制定元素的后继
        temp = self.locate_element(current_element)
        if temp == -1 or temp == self.l_length - 1:
            return False
        else:
            print(self.list[temp + 1])
            return True

    def insert_element(self, subscript, element):  # 在指定下标插入元素
        if subscript < 0 or subscript > self.list_capacity -1:
            return False
        elif not subscript < 0 or subscript > self.list_capacity -1:
            self.l_length += 1
            self.list.insert(subscript, element)

    def delete_element(self, subscript):  # 删除制定下标的元素
        if subscript < 0 or subscript > self.l_length -1:
            return False
        elif not subscript < 0 or subscript > self.l_length -1:
            self.l_length -= 1
            self.list.remove(self.list[subscript])

    def for_list(self):  # 遍历顺序表
        for elem in self.list:
            print(elem)


if __name__ == '__main__':
    a = MyList(12)
    a.insert_element(0, 0)
    a.insert_element(10, 1)
    a.insert_element(100, 2)
    a.insert_element(1, 999)
    a.for_list()
    print('---')
    a.delete_element(1)
    a.delete_element(10)
    a.insert_element(1, 100)
    a.for_list()
    print('---')
    a.prior_element(100)
    a.next_element(100)
    a.get_elements(1)
