class Node:

    def __init__(self, data, parent):
        self.data = data
        self.patent = parent
        self.leftNode = None
        self.rightNode = None


class BinarySearch:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftNode:
                self.insert_node(data, node.leftNode)
            else:
                node.leftNode = Node(data, node)
        else:
            if node.rightNode:
                self.insert_node(data, node.rightNode)
            else:
                node.rightNode = Node(data, node)

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftNode:
            self.traverse_in_order(node.leftNode)

        print("%s " % node.data)

        if node.rightNode:
            self.traverse_in_order(node.rightNode)

        # print("%s " % node.data)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightNode:
            return self.get_max(node.rightNode)
        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftNode:
            return self.get_min(node.leftNode)
        return node.data



if __name__ == '__main__':
    bs = BinarySearch()
    bs.insert(10)
    bs.insert(5)
    # bs.insert(1)
    bs.insert(66)
    # bs.insert(67)
    bs.traverse()
    print(bs.get_max_value())
