
from time import time
def exec_time(loop):
    def wrapper(*args):
        start = time()
        loop(*args)
        end = time()
        return end - start
    return wrapper



@exec_time
def loop(start,end):
    total = 0
    for x in range(start,end):
        total += x
    return total
print(loop(1, 10000000))
