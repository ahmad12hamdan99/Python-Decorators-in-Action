import inspect
from time import time
import inspect


    

def decorator_2(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        wrap_func.calls += 1
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{func.__name__} call {wrap_func.calls} excuted in {(t2-t1):.4f} sec')
        print(f'Name:\t{func.__name__}')
        print(f'Type:\t{type(func)}')
        print(f'Signs:\t{inspect.signature(func)}')
        print(f'Args: \tpositional {args} \n\tkey_worded {kwargs}\n')
        print(f'Doc:\t{inspect.getdoc(func)}'.replace('\n', '\n\t'), end='\n\n')
        print(f'Source:\t{inspect.getsource(func)}'.replace('\n', '\n\t'), end='\n')
        print(f'Output:\t{result}'.replace('\n', '\n\t'))
    wrap_func.calls = 0
    return wrap_func