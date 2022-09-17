from time import time

def decorator_1(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        wrap_func.calls += 1
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{func.__name__} call {wrap_func.calls} excuted in {(t2-t1):.4f} sec')
        return func
    wrap_func.calls = 0
    return wrap_func
  