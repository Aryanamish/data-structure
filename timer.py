import time


def performance(fun):
    def wrapper(*args, **kwargs):
        t = time.time()
        a = fun(*args, **kwargs)
        print(f"time taken for function `{fun.__name__}` is {time.time() - t} seconds")
        return a
    return wrapper