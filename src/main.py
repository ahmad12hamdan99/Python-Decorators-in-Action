import math
from task1 import timer_func
@timer_func
def quadratic_equation_solver(a, b, c):
    if a == 0:
        print('incorrect input')
        return 1

    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    
    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

@timer_func
def pascal_triangle(n):
    for i in range(n):
        # adjust space
        print(' '*(n-i), end='')

        # compute power of 11
        print(' '.join(map(str, str(11**i))))


if __name__ == '__main__':
    
    pascal_triangle(5)
    quadratic_equation_solver(1,2,3)
    pascal_triangle(5)
    quadratic_equation_solver(1,2,3)