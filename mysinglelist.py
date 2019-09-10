# author:CodingDog
# info:此篇相比之前的数据结构 颇为抽象 注释添加的比较完整 方便食用


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyList:

    def __init__(self):  # 初始化头结点
        self.list_head = Node()  # 头结点起引导作用  不参与数据存放
        self.s_length = 0  # 单链表的长度

    def destroy_list(self):  # 释放单链表的内存
        pass

    def clear_list(self):  # 清空单链表
        current_node = self.list_head.next  # 头结点无意义 无需清理 需要的是指针域
        while current_node:
            temp = current_node.next  # 保存指针域 留作追溯 准备删除结点
            current_node.data = None
            current_node.next = None
            current_node = temp  # 循环内部实现遍历操作
        self.list_head.next = None

    def list_empty(self):  # 检测单链表是否为空
        return True if self.s_length == 0 else False

    def len_list(self):  # 测量单链表的长度
        return self.s_length

    def insert_head(self, elem):  # 从单链表的头部插入元素
        temp = self.list_head.next  # 将单链表头结点的指针域赋值给临时变量
        node = Node(elem)  # 创建新的结点 准备插入
        self.list_head.next = node  # 将新结点赋值给头结点的指针域 让头结点指针域指向新结点
        node.next = temp  # 将原先头结点的指针域赋值给新结点 让新结点指向头结点的下一个结点
        self.s_length += 1  # 完成插入工作 单链表长度加一

    def insert_tail(self, elem):  # 从单链表的尾部插入元素
        current_node = self.list_head  # 将头结点赋值给循环变量
        while current_node.next:  # 循环至结点的指针域指向None
            current_node = current_node.next  # while内部实现循环的遍历操作
        node = Node(elem)  # 创建新的结点 准备插入
        current_node.next = node  # 遍历完成以后 将最后一个结点的指针域指向新的结点
        self.s_length += 1  # 完成插入工作 单链表长度加一

    def list_insert(self, subscript, elem):  # 在任意位置插入元素
        if subscript < 0:  # 如果提供的下标不合法&小于0 按照从头插入处理
            self.insert_head(elem)
        elif subscript > self.s_length:  # 如果提供的下标不合法&大于单链表的长度 按照从尾插入处理
            self.insert_tail(elem)
        elif not subscript < 0 and not subscript > self.s_length:  # 判断下标处于合法状态
            current_node = self.list_head  # 将头结点赋值给循环变量
            for i in range(0, subscript):   # 进行下标-1次for循环找到要插入元素的结点位置
                current_node = current_node.next  # for循环内部实现的遍历操作
            node = Node(elem)  # 创建新的结点准备插入
            node.next = current_node.next  # 将新结点的指针域指向指定位置结点的指针域
            current_node.next = node  # 将指定位置结点的指针域指向新结点

    def list_delete(self, subscript):  # 删除指定下标的元素
        if not subscript < 0 and not subscript >= self.s_length:  # 判断下标是否合法
            current_node = self.list_head  # 将头结点赋值给循环变量
            current_node_before = None  # 创建一个变量保存指定下标前一个结点 用于连接单链表
            for i in range(0, subscript + 1):  # 进行下标+1次循环操作 找到指定位置结点以及前一个结点
                current_node_before = current_node  # 先找前一个结点 赋值以后进行循环内遍历
                current_node = current_node.next  # for循环内部实现遍历操作
            current_node_before.next = current_node.next  # 将指定位置前一个结点的指针域指向指定位置的指针域
            current_node = None  # 删除指定结点
            self.s_length -= 1  # 完成删除操作 单链表长度减一

    def get_element(self, subscript):  # 获取制定下标的元素
        if not subscript < 0 and not subscript >= self.s_length:  # 判断下标是否合法
            current_node = self.list_head  # 将头结点赋值给循环变量
            for i in range(0, subscript + 1):  # 进行f下标+1次循环操作 找到指定位置的结点
                current_node = current_node.next  # for循环内部实现遍历操作
            print(current_node.data)  # 将取到的结点的数据域打印出来
        else:
            print(None)

    def locate_element(self, elem):  # 获取指定数据所在结点的下标
        current_node = self.list_head  # 将头结点赋值给循环变量
        count = 0  # 计次循环次数 作为下标（位置）返回
        while current_node.next:  # 循环至尾结点
            current_node = current_node.next  # while循环内部实现遍历操作
            if current_node.data == elem:  # 每一次循环都判断当前结点的数据域是否与提供的数据匹配
                return count  # 如果匹配 返回第一个相同元素的位序！！ 后面可能仍然有相同的元素
                # ⬆可以利用哈希表进行改进 请自行脑补
            count += 1  # 一定要在return以后进行计次++操作
            return -1  # 未匹配 返回-1

    def prior_element(self, elem):  # 获取指定元素的前驱 部分代码与获取指定数据所在结点的下标相同 不再赘述
        current_node = self.list_head
        while current_node.next:
            current_node_before = current_node
            current_node = current_node.next
            if current_node.data == elem:
                if current_node_before == self.list_head:
                    return None
                return current_node_before.data
        return None

    def next_element(self, elem):  # 获取指定元素的后继 同上
        current_node = self.list_head
        while current_node.next:
            current_node = current_node.next
            if current_node.data == elem:
                if not current_node.next:
                    return None
                return current_node.next.data
        return None

    def for_list(self):  # 遍历单链表
        current_node = self.list_head
        while current_node.next:
            current_node = current_node.next
            print(current_node.data)


if __name__ == '__main__':
    a = MyList()
    a.insert_head(1)
    a.insert_head(2)
    a.insert_head(3)
    a.insert_head(4)
    a.insert_head(5)
    a.for_list()
    print("---")
    a.insert_tail(0)
    a.insert_tail(-1)
    a.insert_tail(-2)
    a.for_list()
    print("---")
    print(a.prior_element(5))
    print(a.prior_element(1))
    print(a.next_element(-2))
    print(a.next_element(-1))
    print("---")
    print(a.len_list())
    print(a.list_empty())
    print("---")
    a.get_element(1)
    a.get_element(0)
    a.get_element(100)