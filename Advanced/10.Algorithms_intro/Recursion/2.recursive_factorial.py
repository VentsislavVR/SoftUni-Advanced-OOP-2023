def get_factorial(n:int) -> int:
    if n == 0:
        return 1
    return n * get_factorial(n - 1)


n = int(input())
print(len(str(get_factorial(n))))
print(get_factorial(n))