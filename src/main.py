import math
import random
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4


@decorator_4
@decorator_3
def even(input_list):
    """
    This function return even numbers in the given list
    :param input_list: List that we want to search for even number inside
    This function return the even numbers in the list
    """
    return list(filter(lambda x: x % 2 == 0, input_list))

@decorator_3
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_3
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i



@decorator_4
@decorator_3
def solver(a, b, c):
    """
    This function solve a quadratic equation a*x^2 + b*x + c = 0
    :param a: x^2 coeffecient
    :param b: x   coeffecient
    :param c:     constant
    This function return the solution if it exist in form of list 
    """
    if a == 0:
        return 'incorrect input'

    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        #dis is positive -> 2 solution 
        return [(-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a)]
    
    elif dis == 0:
        #dis is 0 -> duplicated solution
        return [-b / (2 * a)]
    else:
        #Complex Roots
        return [str(-b / (2 * a)) + " + i" + str(sqrt_val) , str(-b / (2 * a)) + " - i" + str(sqrt_val)]


@decorator_4
@decorator_3
def pascal(n):
    """
    This function print pascal triangle
    :param n: The number of pascal triangle rows
    This function return None
    """
    main_v = [1]
    added_v = [0]
    for _ in range(n):
        print(main_v)
        main_v = [left + right for left, right in zip(main_v + added_v, added_v + main_v)]

@decorator_4
@decorator_3
def err(n):
    """
    This function divides 1 by n
    :param n: int
    This function return float is n is not 0
    """
    return 1/n

if __name__ == '__main__':

    func()
    funx()
    func()
    funx()
    func()
    even([0,2,3,4,5,6])
    solver(1,2,3)
    pascal(5)
    solver(0,0,0)
    pascal(4)
    decorator_3.ranking()
    err(0)

