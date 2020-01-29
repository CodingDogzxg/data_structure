# author:CodingDog
# info: 基于数组构建树


class MyTree:

    def __init__(self, tree_capacity, father_node):
        self.tree_capacity = tree_capacity
        self.tree = []
        for i in range(0, self.tree_capacity):  # 将树内的所有节点都赋值为0
            self.tree.append(0)
        self.tree[0] = father_node

    def destroy_tree(self):
        pass

    def search_node(self, subscript):
        if subscript < 0 or subscript >= self.tree_capacity:
            return None
        if self.tree[subscript] == 0:
            return None
        return self.tree[subscript]

    def add_node(self, subscript, direction, node):  # subscrip指的是父节点的位置
        if subscript < 0 or subscript >= self.tree_capacity:  # 判断下标是否有合法
            return False
        if self.tree[subscript] == 0:  # 判断这个节点是否有意义
            return False
        if direction == 0:  # 0值是默认插入到节点左边
            if subscript * 2 + 1 >= self.tree_capacity:
                return False
            if self.tree[subscript * 2 + 1] != 0:  # 判断这个节点不为0
                return False
            self.tree[subscript * 2 + 1] = node
        elif direction == 1:  # 1值是默认插入到节点右边
            if subscript * 2 + 2 >= self.tree_capacity:
                return False
            if self.tree[subscript * 2 + 2] != 0:
                return False
            self.tree[subscript * 2 + 2] = node

    def delete_node(self, subscript):  # 删除节点
        if subscript < 0 or subscript >= self.tree_capacity:  # 判断下标是否合法
            return False
        if self.tree[subscript] == 0:  # 判断这个节点是否有意义
            return False
        self.tree[subscript] = 0

    def for_tree(self):
        for x in self.tree:
            print(x)


if __name__ == '__main__':
    a = MyTree(10, 3)
    a.add_node(0, 0, 5)
    a.add_node(0, 1, 8)
    a.for_tree()
    print("---")
    a.delete_node(2)
    a.delete_node(1)
    a.for_tree()
    print("---")
    print(a.search_node(0))
    a.add_node(0, 0, 5)
    print(a.search_node(1))