# class store_results:
#     def __init__(self, func):
#         self.func = func
#
#     _file_name = "result.txt"
#
#     def __call__(self, *args, **kwargs):
#         with open(store_results._file_name, "a") as result_file:
#             result_file.write(f"Function {self.func.__name__} was called. Result:{self.func(*args)}\n")
#
#
# @store_results
# def add(a, b):
#     return a + b
#
#
# @store_results
# def mult(a, b):
#     return a * b
#
#
# add(2, 2)
# mult(6, 4)


class store_results_with_param:
    def __init__(self, param):
        self.param = param

    _file_name = "result.txt"

    def __call__(self, func):
        def wrapper(*args):
            with open(store_results_with_param._file_name, "a") as result_file:
                result_file.write(f"Function {func.__name__} was called. Result:{func(*args)}\n")
        return wrapper

@store_results_with_param(2)
def add(a, b):
    return a + b


@store_results_with_param
def mult(a, b):
    return a * b
