class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def delete_node(self, data):
        current_node = self.head
        previous_node = None
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        # If the current node is the head node, update the head node

        if previous_node is None:
            self.head = current_node.next
        else:
            # Otherwise, update the next node of the previous node
            previous_node.next = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

list = LinkedList()
list.add_node(1)
list.add_node(2)
list.add_node(3)
list.print_list()
list.delete_node(2)
list.print_list()
