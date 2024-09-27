def custom_cache(func):
    cache = {}
    def wrapper(a, b):
        if ((a, b) not in cache) and ((b, a) not in cache):
            cache[(a, b)] = func(a, b)
        return cache.get((a, b)) or cache.get((b, a))
    return wrapper


@custom_cache
def sum_num(a, b):
    res = a + b
    print(f"Calculating: {a} + {b} = {res}")
    return res

def test():
    for i in range(5):
        for j in range(5):
            # print(i, j)
            sum_num(i, j) 

if __name__ == "__main__":
    test()
