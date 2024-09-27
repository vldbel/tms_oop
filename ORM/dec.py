from time import sleep

def dec_delay(timer):
    def middle(func):
        def wrapper():
            print(f"sleeping for {timer} sec")
            sleep(timer)
            func()
        return wrapper
    return middle


@dec_delay(5)
def test_func():
    print("test_func is running")
    

test_func()
