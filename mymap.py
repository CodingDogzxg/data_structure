# author:CodingDog
# info: 基于矩阵构建图


class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False


class MyMap:
    def __init__(self, map_capacity):
        self.map_capacity = map_capacity
        self.node_count = 0
        self.node_array = [Node(0) for i in range(self.map_capacity**2)]
        self.matrix = [0 for i in range(self.map_capacity**2)]

    def map_destroy(self):
        pass

    def add_node(self, data):
        self.node_array[self.node_count].data = data
        self.node_count += 1

    def reset_node(self):
        for i in range(self.node_count):
            self.node_array[i] = Node(0)
            self.node_array[i].visited = False

    def set_value_to_directed_matrix(self, row, col, val):
        if 0 <= row < self.map_capacity and 0 <= row < self.map_capacity:
            self.matrix[row * self.map_capacity + col] = val

    def set_value_to_undirected_matrix(self, row, col, val):
        if 0 <= row < self.map_capacity and 0 <= row < self.map_capacity:
            self.matrix[row * self.map_capacity + col] = val
            self.matrix[col * self.map_capacity + row] = val

    def get_value_from_matrix(self, row, col):
        if 0 <= row < self.map_capacity and 0 <= row < self.map_capacity:
            return self.matrix[row * self.map_capacity + col]

    def map_traversal(self):
        for row in range(self.map_capacity):
            for col in range(self.map_capacity):
                print(self.matrix[row * self.map_capacity + col])

    def depth_first_traverse(self, node_index):
        print(self.node_array[node_index].data)
        self.node_array[node_index].visited = True