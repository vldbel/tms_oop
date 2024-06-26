class Child:
    children = []
    children_count = 0
    
    @classmethod
    def _register_child(cls, self):
        cls.children.append(self)
    
    @classmethod
    def round_dance(cls):
        for idx in range(len(cls.children)):
            cls.children[idx].next = cls.children[idx + 1] if (idx + 1) < len(cls.children) else cls.children[0]
    
    def __init__(self):
        self.next = None
        Child._register_child(self)
        Child.children_count += 1


def test():
    ch1 = Child()
    ch2 = Child()
    ch3 = Child()

    assert Child.children_count == 3
    assert len(Child.children) == 3
    
    Child.round_dance()
    assert ch1.next == ch2
    assert ch2.next == ch3
    assert ch3.next == ch1
    
    
if __name__ == "__main__":
    test()
