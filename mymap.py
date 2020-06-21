# author:CodingDog
# info: 基于矩阵构建图
"""
        A
      /  \
     B    D
    / \  / \
   C  F G - H
   \ /
    E
-----------------------
   A B C D E F G H
A    1   1
B  1   1     1
C    1     1
D  1           1 1
E      1
F    1
G        1       1
H        1     1
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False


class MyMap:
    def __init__(self, map_capacity):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.map_capacity = map_capacity
        self.node_array = [Node(self.alphabet[i]) for i in range(self.map_capacity)]
        self.node_count = len(self.node_array)
        self.matrix = [0 for i in range(self.map_capacity**2)]

    def map_destroy(self):
        pass

    def add_node(self, data):
        self.node_array[self.node_count].data = data
        self.node_count += 1

    def reset_node(self):
        for i in range(self.node_count):
            self.node_array[i] = Node(self.alphabet[i])
            self.node_array[i].visited = False

    def set_value_to_directed_matrix(self, row, col, val=1):
        if 0 <= row < self.map_capacity and 0 <= row < self.map_capacity:
            self.matrix[row * self.map_capacity + col] = val

    def set_value_to_undirected_matrix(self, row, col, val=1):
        if 0 <= row < self.map_capacity and 0 <= row < self.map_capacity:
            self.matrix[row * self.map_capacity + col] = val
            self.matrix[col * self.map_capacity + row] = val

    def get_value_from_matrix(self, row, col):
        if 0 <= row < self.map_capacity and 0 <= row < self.map_capacity:
            return self.matrix[row * self.map_capacity + col]

    def map_traversal(self):
        for row in range(self.map_capacity):
            temp = list()
            for col in range(self.map_capacity):
                temp.append(self.matrix[row * self.map_capacity + col])
            print(temp)

    def depth_first_traverse(self, node_index):
        print(self.node_array[node_index].data)
        self.node_array[node_index].visited = True
        for i in range(0, self.map_capacity):
            value = self.matrix[node_index * self.map_capacity + i]
            if value == 1:
                if self.node_array[i].visited:
                    continue
                else:
                    self.depth_first_traverse(i)
            else:
                continue

    def breadth_first_traverse(self, node_index):
        print(self.node_array[node_index].data)
        self.node_array[node_index].visited = True

        temp_list = list()
        temp_list.append(node_index)

        self.breadth_first_traverse_impl(temp_list)

    def breadth_first_traverse_impl(self, pre_list):
        cur_list = list()
        for i in range(len(pre_list)):
            for j in range(self.map_capacity):
                value = self.matrix[pre_list[i] * self.map_capacity + j]
                if value == 1:
                    if self.node_array[j].visited:
                        continue
                    else:
                        print(self.node_array[j].data)
                        self.node_array[j].visited = True
                        cur_list.append(j)
        if len(cur_list) == 0:
            return
        else:
            self.breadth_first_traverse_impl(cur_list)


if __name__ == '__main__':
    a = MyMap(8)

    a.set_value_to_undirected_matrix(0, 1)
    a.set_value_to_undirected_matrix(0, 3)
    a.set_value_to_undirected_matrix(1, 2)
    a.set_value_to_undirected_matrix(1, 5)
    a.set_value_to_undirected_matrix(3, 6)
    a.set_value_to_undirected_matrix(3, 7)
    a.set_value_to_undirected_matrix(6, 7)
    a.set_value_to_undirected_matrix(2, 4)
    a.set_value_to_undirected_matrix(4, 5)

    a.map_traversal()

    a.depth_first_traverse(0)
    print("---")

    a.reset_node()
    a.breadth_first_traverse(0)