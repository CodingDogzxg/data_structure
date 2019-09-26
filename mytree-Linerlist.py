# author:CodingDog
# info:基于链表构建树


class Node:
    def __init__(self):
        self.index = 0  # 节点索引
        self.data = 0  # 节点数据
        self.lchild = None  # 左节点指针
        self.rchild = None  # 右节点指针
        self.parent = None  # 父节点指针

    def search_node(self, subscript):
        if self.index == subscript:  # 本身就是要找的节点
            return self
        if self.lchild:  # 本身不是要找的节点 判断左节点是否为空
            if self.lchild.index == subscript:  # 判断左节点是否是要找的节点
                return self.lchild
        if self.rchild:  # 本身不是要找的节点 判断右节点是否为空
            if self.rchild.index == subscript:  # 判读右节点是否是要找的节点
                return self.rchild
        return None  # 未找到 返回None

    def delete_node(self):
        if self.lchild:
            self.lchild.delete_node()
        if self.rchild:
            self.rchild.delete_node()
        if self.parent.lchild == self:  # 判断自身处于父节点的什么位置
            self.parent.lchild = None
        if self.parent.rchild == self:
            self.parent.rchild = None
        del self  # 将自身删除掉

    def preorder_traversal(self):  # 前序遍历 根左右
        print(self.index, "&", self.data)  # 先将自己输出
        if self.lchild:  # 如果存在左节点，左节点调用前序遍历
            self.lchild.preorder_traversal()
        if self.rchild:  # 如果存在右节点，右节点调用前序遍历
            self.rchild.preorder_traversal()

    def inorder_traversal(self):  # 中序遍历 左根右
        if self.lchild:  # 如果存在左节点，左节点调用中序遍历
            self.lchild.inorder_traversal()
        print(self.index, "&", self.data)
        if self.rchild:  # 如果存在右节点，右节点调用中序遍历
            self.rchild.inorder_traversal()

    def postorder_traversal(self):  # 后序遍历 左右根
        if self.lchild:  # 如果存在左节点，左节点调用后序遍历
            self.lchild.postorder_traversal()
        if self.rchild:  # 如果存在右节点，右节点调用后序遍历
            self.rchild.postorder_traversal()
        print(self.index, "&", self.data)


class MyTree:
    def __init__(self):
        self.tree_root = Node()  # 初始化根节点

    def destroy_tree(self):
        self.delete_node(0)  # 将根节点删除掉就是销毁一棵树

    def search_node(self, subscript):
        return self.tree_root.search_node(subscript)

    def add_node(self, subscript, direction, node):
        temp = self.search_node(subscript)  # 临时变量接受寻找节点的结果
        if not temp:  # 如果寻找节点的结果是None
            return False
        if subscript == 0:  # 判断插入的是否为根节点
            node.parent = self.tree_root
        elif subscript != 0:
            temp_parent = self.search_node(subscript - 1)  # 将父节点找到
            node.parent = temp_parent
        if direction == 0:
            temp.lchild = node
        if direction == 1:
            temp.rchild = node
        return True

    def delete_node(self, subscript):
        temp = self.search_node(subscript)  # 临时变量接受寻找节点的结果
        if not temp:  # 如果寻找节点的结果是None
            return False
        temp.delete_node()
        return True

    def preorder_traversal(self):  # 前序遍历
        self.tree_root.preorder_traversal()

    def inorder_traversal(self):  # 中序遍历
        self.tree_root.inorder_traversal()

    def postorder_traversal(self):  # 后序遍历
        self.tree_root.postorder_traversal()


if __name__ == '__main__':
    a = MyTree()

    node1 = Node()
    node1.index, node1.data = 1, 5

    node2 = Node()
    node2.index, node2.data = 2, 8

    node3 = Node()
    node3.index, node3.daa = 3, 2

    node4 = Node()
    node4.index, node4.data = 4, 6

    node5 = Node()
    node5.index, node5.data = 5, 9

    node6 = Node()
    node6.index, node6.data = 6, 7

    a.add_node(0, 0, node1)
    a.add_node(0, 1, node2)
    a.add_node(1, 0, node3)
    a.add_node(1, 1, node4)
    a.add_node(2, 0, node5)
    a.add_node(2, 1, node6)

    a.preorder_traversal()
    print("---")
    a.inorder_traversal()
    print("---")
    a.postorder_traversal()
    print("---")
    a.delete_node(1)
    a.preorder_traversal()
    print("---")
    a.destroy_tree()
    a.preorder_traversal()