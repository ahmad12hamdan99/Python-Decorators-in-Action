import math
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3


@decorator_3
def solver(a, b, c):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """ 
    if a == 0:
        return 'incorrect input'

    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        #print(" real and different roots ")
        return [(-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a)]
    
    elif dis == 0:
        #print(" real and same roots")
        return [-b / (2 * a)]
    else:
        #print("Complex Roots")
        return [str(-b / (2 * a)) + " + i" + str(sqrt_val) , str(-b / (2 * a)) + " - i" + str(sqrt_val)]

@decorator_3
def pascal(n):
    """
    This function prints the pascal triangle
    :param n: number of rows
    """ 
    for i in range(n):
        # adjust space
        print(' '*(n-i), end='')

        # compute power of 11
        print(' '.join(map(str, str(11**i))))


if __name__ == '__main__':
    
    # pascal_triangle(5)
    # quadratic_equation_solver(1,2,3)
    # pascal_triangle(5)
    # quadratic_equation_solver(1,2,3)
    # quadratic_equation_solver(1,2,3)
    # pascal_triangle(10)

    solver(1,2,3)
    pascal(5)
    solver(1,2,3)
    pascal(5)
    decorator_3.ranking()

