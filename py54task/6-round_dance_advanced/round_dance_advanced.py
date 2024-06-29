""" Circular Doubly linked list """

class Child:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def __str__(self):
        return self.name


class CircularDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, name):
        new_node = Child(name)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.head.prev = self.tail
        self.tail.next = self.head

    def append(self, name):
        new_node = Child(name)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head
        
    def remove(self, name):
        ...
    
    def pop(self, name):
        ...

    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"{current_node} (prev: {current_node.prev}, next: {current_node.next})", 
                  end=" -> " if current_node.next != self.tail.next else '\n')
            current_node = current_node.next
            if current_node == self.head: # last node
                break


def test():
    circ_dlst = CircularDLinkedList()
    circ_dlst.append("Sasha")
    # print(f"Head: {circ_dlst.head}")
    # print(f"Tail: {circ_dlst.tail}")

    circ_dlst.append("Angelina")    
    circ_dlst.append("Jadviga")
    # print(f"Head: {circ_dlst.head}")
    # print(f"Head.prev: {circ_dlst.head.prev}")
    # print(f"Head.next: {circ_dlst.head.next}")
    # print()
    # print(f"Tail: {circ_dlst.tail}")
    # print(f"Tail.prev: {circ_dlst.tail.prev}")
    # print(f"Tail.next: {circ_dlst.tail.next}")
    circ_dlst.append("Maksim")
    circ_dlst.append("Vova")
    circ_dlst.prepend("Petr")
    circ_dlst.print_list()
    

if __name__ == "__main__":
    test()
