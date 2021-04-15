class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_data(self, data):
        new_node = Node(data)
        self.numOfNodes += 1

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        self.numOfNodes += 1
        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_linked_list(self):
        return self.numOfNodes

    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode


if __name__ == '__main__':
    liked_list = LinkedList()
    liked_list.insert_data(1)
    liked_list.insert_data(2)
    liked_list.insert_data(3)

    liked_list.insert_end(100)
    # print(liked_list.size_of_linked_list())
    liked_list.traverse()
