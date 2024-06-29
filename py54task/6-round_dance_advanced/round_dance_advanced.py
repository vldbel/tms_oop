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

    def take_my_hand(self, child: Child):
        self.head.prev = child
        child.next = self.head
        self.head = child
        self.head.prev = self.tail
        self.tail.next = self.head
    
    def prepend(self, name):
        new_node = Child(name)
        self.take_my_hand(new_node)
        
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


def print_ll_state(cls):
    print(f"Head: {cls.head}")
    print(f"Head.prev: {cls.head.prev}")
    print(f"Head.next: {cls.head.next}")
    print()
    print(f"Tail: {cls.tail}")
    print(f"Tail.prev: {cls.tail.prev}")
    print(f"Tail.next: {cls.tail.next}")


def test():
    circ_dlst = CircularDLinkedList()
    circ_dlst.append("Sasha")
    circ_dlst.append("Angelina")
    
    child_jad = Child("Jadviga")
    circ_dlst.take_my_hand(child_jad)    
    # print_ll_state(circ_dlst)
    
    circ_dlst.append("Maksim")
    circ_dlst.append("Vova")
    circ_dlst.prepend("Petr")
    circ_dlst.print_list()
    

if __name__ == "__main__":
    test()
