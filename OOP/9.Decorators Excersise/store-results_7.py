class store_results:
    def __init__(self,func):
        self.func = func

    _file_name = "result.txt"

    def __call__(self, *args, **kwargs):
        with open(store_results._file_name,"a") as result_file:
            result_file.write(f"Function {self.func.__name__} was called. Result:{self.func(*args)}")


@store_results
def add(a,b):
    return a+b