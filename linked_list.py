class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
    
    
llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.display()