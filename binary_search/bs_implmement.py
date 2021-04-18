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
                node.leftChild = Node(data, node)
        else:
            if node.rightNode:
                self.insert_node(data, node.rightNode)
            else:
                node.rightNode = Node(data, node)


if __name__ == '__main__':
    bs = BinarySearch()
    bs.insert(10)
    bs.insert(5)
    bs.insert(66)