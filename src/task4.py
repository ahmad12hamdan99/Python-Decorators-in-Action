from time import time
from contextlib import redirect_stdout
import io
import inspect
import sys
import traceback
from datetime import datetime

from task3 import decorator_3

class decorator_4(decorator_3):
    dic_time = {}

    def __init__(self, func):
        self.function = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        try:
            res = super().__call__(*args, **kwargs)
            return res
        except Exception as e:
            tb = sys.exc_info()[-1]
            stk = traceback.extract_tb(tb)
            with open('log_file.txt', 'a+') as f:
                f.write(f'{datetime.strftime(datetime.now(), f"%y-%m-%d %H:%M:%S: ")}function {stk[2][2]} {e} \n')
            print(f'Error in calling {stk[2][2]} written in the log file.')
        return None