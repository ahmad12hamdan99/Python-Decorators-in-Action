from time import time
from task3 import decorator_1

class A:
    def __init__(self):
        self.count = 0
        self.ltime = 555

    @decorator_1
    def func(self, a):
        print(a, self.ltime)

#decorator function
def decorator(fun):
    def wr(*args, **kwarge):
        fun()
    return wr

a = A()
a.func(a, 500)