from time import sleep

class SwimmingPool:
    def __init__(self, meters=100) -> None:
        if 100 > meters:
            raise ValueError("pool length has to be at least 100 meters")
        self.length = meters


class Swimmer:
    def __init__(self, swimming_speed) -> None:
        self.swimming_speed = swimming_speed
        
    def to_swim(self, swim_pool: SwimmingPool, distance):
        current_distance = 0
        while current_distance < distance:
            direction = -1 if current_distance // swim_pool.length % 2 else 1
            position_in_pool = current_distance % swim_pool.length if direction > 0 \
                else -1 * current_distance % swim_pool.length - 1
            self.__print_frame(swim_pool.length, position_in_pool)
            sleep(10 / self.swimming_speed)
            current_distance += 10        
    
    @staticmethod
    def __print_frame(pool_size, swimmer_position):
        pool = list(pool_size//10 * "=")
        pool[swimmer_position//10] = "*"
        print("\r", end="")
        print(''.join(pool), end="")


def test():
    spool1 = SwimmingPool(100)
    swimmer1 = Swimmer(swimming_speed=10)
    swimmer1.to_swim(spool1, 300)
    print()
    spool2 = SwimmingPool(500)
    swimmer2 = Swimmer(swimming_speed=10)
    swimmer2.to_swim(spool2, 1000)
    
    
if __name__ == "__main__":
    test()
