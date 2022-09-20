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

Output: I am ready to do serious stuff
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

