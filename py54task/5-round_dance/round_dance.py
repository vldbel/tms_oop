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
    circ_lst = CircularLinkedList()
    circ_lst.append("Sasha")
    circ_lst.append("Angelina")
    circ_lst.append("Jadviga")
    circ_lst.append("Maksim")
    circ_lst.append("Vova")
    circ_lst.prepend("Petr")
    circ_lst.print_list()
    # print(f"Head: {circ_lst.head}")
    # print(f"Tail: {circ_lst.tail}")
    

if __name__ == "__main__":
    test()
    
# https://www.youtube.com/watch?v=Exol2HWE97k - great video about the topic
