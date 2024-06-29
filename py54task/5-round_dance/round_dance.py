"""Circular Singly linked list (forward connection)"""

class Child:
    def __init__(self, name):
        self.next = None
        self.name = name
        
    def __str__(self):
        return self.name
        
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, name):
        new_node = Child(name)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        
    def append(self, name):
        new_node = Child(name)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
    
    def remove(self, name):
        ...
    
    def pop(self, name):
        ...
                    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"{current_node} ({current_node.next})", end=" -> " if current_node.next != self.tail.next else '\n')
            current_node = current_node.next
            if current_node == self.head: # last node
                break
            
    
def test():
    Circ_lst = CircularLinkedList()
    Circ_lst.append("Sasha")
    Circ_lst.append("Angelina")
    Circ_lst.append("Jadviga")
    Circ_lst.append("Maksim")
    Circ_lst.append("Vova")
    Circ_lst.prepend("Petr")
    Circ_lst.print_list()
    # print(f"Head: {Circ_lst.head}")
    # print(f"Tail: {Circ_lst.tail}")
    

if __name__ == "__main__":
    test()
    
# https://www.youtube.com/watch?v=Exol2HWE97k - great video about about the topic 