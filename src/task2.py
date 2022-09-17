import inspect
from time import time
import inspect

def inspector(func,*args, **kwargs):
    print(f'Name:\t{func.__name__}')
    print(f'Type:\t{type(func)}')
    print(f'Signs:\t{inspect.signature(func)}')
    #print(f'Args:\t{inspect.FullArgSpec(func)}')
    print(f'Doc:\t{inspect.getdoc(func)}')
    print(f'Source:\t{inspect.getsource(func)}')
    print('Output:', end='\t')
    func(*args, **kwargs)
    

def decorator_2(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        wrap_func.calls += 1
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{func.__name__} call {wrap_func.calls} excuted in {(t2-t1):.4f} sec')
        inspector(func,*args, **kwargs)
        #return func
    wrap_func.calls = 0
    return wrap_func