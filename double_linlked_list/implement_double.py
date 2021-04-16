class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinked:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d " % actual_node.data)
            actual_node = actual_node.next

    def traverse_back(self):
        actual_node = self.tail

        while actual_node is not None:
            print("%d " % actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__':
    d = DoubleLinked()
    d.insert(1)
    d.insert(2)
    d.insert(3)
    d.traverse_back()
