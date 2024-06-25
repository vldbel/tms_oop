""" 1. Реальные строки """

class StrLen(str):
    def __init__(self, string):
        self.string = str(string)

    @staticmethod
    def _check_type(value):
        if not isinstance(value, (str, StrLen)):
            raise TypeError(f"Wrong operand type for comparison: {type(value)}")
    
    @staticmethod
    def _choose_value_type(value):
        return value if isinstance(value, str) else value.string

    def __eq__(self, value: object) -> bool:
        self._check_type(value)
        return len(self.string) == len(self._choose_value_type(value))
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
        # self._check_type(value)
        # return len(self.string) != len(self._choose_value_type(value))
    
    def __gt__(self, value: object) -> bool:
        self._check_type(value)
        return len(self.string) > len(self._choose_value_type(value))

    def __lt__(self, value: object) -> bool:
        self._check_type(value)
        return len(self.string) < len(self._choose_value_type(value))
    
    def __ge__(self, value: str) -> bool:
        return not self.__lt__(value)

    def __le__(self, value: str) -> bool:
        return not self.__gt__(value)
    

def test():
    str1 = StrLen("abc")
    str2 = StrLen("def")
    str3 = StrLen("gh")
    str4 = StrLen("ijkl")

    # wrong type check
    try: 
        assert (1 == str1) == Exception
    except:
        ... # it is fine
    else:
        # it is not fine
        raise Exception("wrong result of operation")

    # eq, not eq
    assert (str1 == "xyz") == True
    assert ("xyz" == str1) == True
    assert (str1 == str2) == True
    assert (str1 != str2) == False 
    assert (str1 == str3 == str4) == False
    assert (str2 != str3 != str4) == True
    
    # gt, lt
    assert str1 > "a"
    assert "abcd" > str1
    
    assert str1 < "abcd"
    assert "a" < str1

    assert str1 > str3
    assert str3 < str1


if __name__ == "__main__":
    test()
