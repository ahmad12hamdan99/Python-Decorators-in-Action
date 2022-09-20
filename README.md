# Python-Decorators-in-Action
This repository contains solutions for Software Design with Python course at Innopolis University Fall 2022

## Intructions: 
main.py imports all decorators and the user has the freedome to apply any of them to any function available in the main. just run 
```console
$ python3 main.py

```

## Task1: 
Create a function decorator that calculates function execution time and the number of times the decorated function was called.

```console
ahmad@WorkStation:~/Git/Python-Decorators-in-Action/src$ python3 main.py
func call 1 excuted in 0.0002 sec
funx call 1 excuted in 0.0004 sec
func call 2 excuted in 0.0003 sec
funx call 2 excuted in 0.0004 sec
func call 3 excuted in 0.0003 sec
even call 1 excuted in 0.0000 sec
solver call 1 excuted in 0.0000 sec

```

## Task2:
Extend your implementation so that the decorator could dump original source code of the function.

```console
ahmad@WorkStation:~/Git/Python-Decorators-in-Action/src$ python3 main.py
func call 1 excuted in 0.0001 sec
Name:   func
Type:   <class 'function'>
Signs:  ()
Args:   positional () 
        key=worded {}

Doc:    None

Source: @decorator_2
        def func():
            print("I am ready to Start")
            result = 0
            n =  random.randint(10,751)
            for i in range(n):
                result += (i**2)

Output: None

funx call 1 excuted in 0.0002 sec
Name:   funx
Type:   <class 'function'>
Signs:  (n=2, m=5)
Args:   positional () 
        key=worded {}

Doc:    None

Source: @decorator_2
        def funx(n=2, m=5):
            print("I am ready to do serious stuff")
            max_val = float('-inf')
            n =  random.randint(10,751)
            res = [pow(i,2) for i in range(n)]
            for i in res:
                if i > max_val: 
                    max_val = i

Output: None

func call 2 excuted in 0.0001 sec
Name:   func
Type:   <class 'function'>
Signs:  ()
Args:   positional () 
        key=worded {}

Doc:    None

Source: @decorator_2
        def func():
            print("I am ready to Start")
            result = 0
            n =  random.randint(10,751)
            for i in range(n):
                result += (i**2)

Output: None

funx call 2 excuted in 0.0001 sec
Name:   funx
Type:   <class 'function'>
Signs:  (n=2, m=5)
Args:   positional () 
        key=worded {}

Doc:    None

Source: @decorator_2
        def funx(n=2, m=5):
            print("I am ready to do serious stuff")
            max_val = float('-inf')
            n =  random.randint(10,751)
            res = [pow(i,2) for i in range(n)]
            for i in res:
                if i > max_val: 
                    max_val = i

Output: None

func call 3 excuted in 0.0003 sec
Name:   func
Type:   <class 'function'>
Signs:  ()
Args:   positional () 
        key=worded {}

Doc:    None

Source: @decorator_2
        def func():
            print("I am ready to Start")
            result = 0
            n =  random.randint(10,751)
            for i in range(n):
                result += (i**2)

Output: None

even call 1 excuted in 0.0000 sec
Name:   even
Type:   <class 'function'>
Signs:  (input_list)
Args:   positional ([0, 2, 3, 4, 5, 6],) 
        key=worded {}

Doc:    This function return even numbers in the given list
        :param input_list: List that we want to search for even number inside
        This function return the even numbers in the list

Source: @decorator_4
        @decorator_2
        def even(input_list):
            """
            This function return even numbers in the given list
            :param input_list: List that we want to search for even number inside
            This function return the even numbers in the list
            """
            return list(filter(lambda x: x % 2 == 0, input_list))

Output: [0, 2, 4, 6]

solver call 1 excuted in 0.0000 sec
Name:   solver
Type:   <class 'function'>
Signs:  (a, b, c)
Args:   positional (1, 2, 3) 
        key=worded {}

Doc:    This function solve a quadratic equation a*x^2 + b*x + c = 0
        :param a: x^2 coeffecient
        :param b: x   coeffecient
        :param c:     constant
        This function return the solution if it exist in form of list 

Source: @decorator_4
        @decorator_2
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

Output: ['-1.0 + i2.8284271247461903', '-1.0 - i2.8284271247461903']
```

## Task3:
Implement the decorator behavior in tasks 1 & 2 using a class decorator. All the program output (from the decorator) should be dumped into a .txt file. Rank the 4 functions used to test the implementation and plot a rankings table.

```console
ahmad@WorkStation:~/Git/Python-Decorators-in-Action/src$ python3 main.py
PROGRAM  |  RANK  |  TIME ELAPSED
even          1       0.000009060s
solver        2       0.000016689s
pascal        3       0.000028133s
func          4       0.000173092s
funx          5       0.000198126s
```

## Task4:
Extend your program (function or class decorator) so that if a decorated function encounters an error it wouldn’t put it back into stdout. Instead, pipe the error stream into a log file together with a timestamp.

```console
ahmad@WorkStation:~/Git/Python-Decorators-in-Action/src$ python3 main.py
PROGRAM  |  RANK  |  TIME ELAPSED
solver        1       0.000001907s
even          2       0.000008345s
pascal        3       0.000056505s
funx          4       0.000085831s
func          5       0.000251532s
Error in calling err written in the log file.
```

