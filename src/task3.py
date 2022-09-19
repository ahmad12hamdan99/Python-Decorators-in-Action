from time import time
from contextlib import redirect_stdout
import io
class decorator_3:
    dic_time = {}

    def __init__(self, func):
        self.function = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        with redirect_stdout(io.StringIO()) as _:
            start_time = time()
            result = self.function(*args, **kwargs)
            end_time = time()
            self.dic_time[self.function.__name__] = end_time-start_time
            with open('Task3_Output.txt', 'a+') as f:
                f.write('{} call {} excuted in {} sec\n'.format(self.function.__name__ , self.count, end_time-start_time))

        
        return result


