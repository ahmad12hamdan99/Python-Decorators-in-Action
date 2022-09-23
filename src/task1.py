from time import time
import contextlib
import io

#  maybe it  is better to use doc quotes instead of comment to explain what the function does
def decorator_1(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        f = io.StringIO()
        wrap_func.calls += 1
        t1 = time()
        with contextlib.redirect_stdout(f):
            func(*args, **kwargs)
        t2 = time()
        s = f.getvalue()
        print(f'{func.__name__} call {wrap_func.calls} excuted in {(t2-t1):.4f} sec')
        return s
    wrap_func.calls = 0
    return wrap_func
  