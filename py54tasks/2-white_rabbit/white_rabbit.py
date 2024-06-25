class Kettle:
    HEADER = """|******************|
|                  |**/
|                  |*/
|                  |/\n"""
    FILLER   = "|                  |\n"
    FOOTER   = "|******************|\n"

    def __init__(self, ml=300) -> None:
        if 300 > ml:
            raise ValueError("Kettle volume has to be at least 300ml")
        
        self.volume = ml

    def __repr__(self) -> str:
        return f"{self.HEADER}{self.FILLER * (self.volume//100 - 3)}{self.FOOTER}"
    
def test():
    kt1 = Kettle(300)
    kt2 = Kettle(600)
    kt3 = Kettle(1200)

    print(kt1, end='\n\n')
    print(kt2, end='\n\n')
    print(kt3, end='\n\n')


if __name__ == "__main__":
    test()
