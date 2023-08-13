def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
        # if num not in wrapper.log / slower
            wrapper.log[num] = func(num)

        return wrapper.log[num]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))

