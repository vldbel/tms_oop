from time import sleep

class SwimmingPool:
    def __init__(self, meters=100) -> None:
        if 100 > meters:
            raise ValueError("pool length has to be at least 100 meters")
        self.length = meters


class Swimmer:
    def __init__(self, swiming_speed) -> None:
        self.swiming_speed = swiming_speed
        
    def to_swim(self, swim_pool: SwimmingPool, distance):
        current_distance = 0
        while current_distance < distance:
            direction = -1 if current_distance // swim_pool.length % 2 else 1
            position_in_pool = current_distance % swim_pool.length if direction > 0 else -1 * current_distance % swim_pool.length - 1
            self.__print_frame(swim_pool.length, position_in_pool)
            sleep(10 / self.swiming_speed)
            current_distance += 10        
    
    @staticmethod
    def __print_frame(pool_size, swimmer_postion):
        pool = list(pool_size//10 * "=")
        pool[swimmer_postion//10] = "*"
        print("\r", end="")
        print(''.join(pool), end="")


def test():
    spool1 = SwimmingPool(100)
    swimmmer1 = Swimmer(swiming_speed=10)    
    swimmmer1.to_swim(spool1, 300)
    print()
    spool2 = SwimmingPool(500)
    swimmmer2 = Swimmer(swiming_speed=10)    
    swimmmer2.to_swim(spool2, 1000)
    
    
if __name__ == "__main__":
    test()
