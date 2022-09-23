from time import time
from contextlib import redirect_stdout
import io
import inspect
import contextlib

#  really smooth looking way to structure the class
class decorator_3:
    dic_time = {}

    def __init__(self, func):
        self.function = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        f = io.StringIO()
        self.count += 1
        start_time = time()
        with contextlib.redirect_stdout(f):
            self.function(*args, **kwargs)
            

        end_time = time()
        result = f.getvalue()
        self.dic_time[self.function.__name__] = end_time-start_time
        with open('Task3_Output.txt', 'a+') as f:
            f.write('{} call {} excuted in {} sec\n'.format(self.function.__name__ , self.count, end_time-start_time))
            #f.write(f'{self.function.__name__} call {self.count} excuted in {(result):.4f} sec')
            f.write(f'Name:\t{self.function.__name__}\n')
            f.write(f'Type:\t{type(self.function)}\n')
            f.write(f'Signs:\t{inspect.signature(self.function)}\n')
            f.write(f'Args: \tpositional {args} \n\t\tkey=worded {kwargs}\n\n')
            f.write(f'Doc:\t{inspect.getdoc(self.function)}'.replace('\n', '\n\t\t')+'\n\n')
            f.write(f'Source:\t{inspect.getsource(self.function)}'.replace('\n', '\n\t\t')+'\n')
            f.write(f'Output:\t{result}'.replace('\n', '\n\t\t') + '\n\n')
        
        return result

    @staticmethod
    def ranking():
        print('PROGRAM  |  RANK  |  TIME ELAPSED')
        res = dict(sorted(decorator_3.dic_time.items(), key=lambda item: item[1]))
        i = 0
        for k in res:
            i += 1
            print(f'{k: <14}{i: <8}{res[k]:.9f}s')


