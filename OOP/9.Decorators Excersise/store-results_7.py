class store_results:
    def __init__(self, func):
        self.func = func

    _file_name = "result.txt"

    def __call__(self, *args, **kwargs):
        with open(store_results._file_name, "a") as result_file:
            result_file.write(f"Function {self.func.__name__} was called. Result:{self.func(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
