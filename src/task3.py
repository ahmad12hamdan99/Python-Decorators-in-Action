from time import time

class decorator_3:

    def __init__(self, func):
        self.function = func
        self.count = 0
        self.ltime = 0.0

    def __inspector(self,*args, **kwargs):
        discription = f'Name:\t{self.function.__name__}\n'

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        self.ltime = end_time-start_time
        self.count += 1
        # print("Execution took {} seconds".format(self.ltime))
        print('{} call {} excuted in {} sec'.format(self.function.__name__ , self.count, self.ltime))
        return result


