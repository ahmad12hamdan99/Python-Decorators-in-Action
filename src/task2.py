import inspect
from time import time
import inspect
import contextlib
import io


    
#  maybe better speacing in between can be added to make the code look neater
def decorator_2(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        f = io.StringIO()
        t1 = time()
        wrap_func.calls += 1
        with contextlib.redirect_stdout(f):
            func(*args, **kwargs)
        t2 = time()
        s = f.getvalue()
        print(f'{func.__name__} call {wrap_func.calls} excuted in {(t2-t1):.4f} sec')
        print(f'Name:\t{func.__name__}')
        print(f'Type:\t{type(func)}')
        print(f'Signs:\t{inspect.signature(func)}')
        print(f'Args: \tpositional {args} \n\tkey=worded {kwargs}\n')
        print(f'Doc:\t{inspect.getdoc(func)}'.replace('\n', '\n\t'), end='\n\n')
        print(f'Source:\t{inspect.getsource(func)}'.replace('\n', '\n\t'), end='\n')
        print(f'Output:\t{s}'.replace('\n', '\n\n\t') + '\n')
    wrap_func.calls = 0
    return wrap_func