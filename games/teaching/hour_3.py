# Functions are basically objects that when given an input (or multiple inputs), give out an output.
# They usually perform some operations on the data and return (give back) a value (or multiple).
# The syntax for a function is:
'''def function_name(parameters [optional], can be defined without parameters too):
    do something
    return some_value [optional, some functions don't return values]
    '''
# When a function is made to run, it is said to be called. Functions are not called when they are defined. They have to be called seperately in the code.
# For example:
def square(x):
    print(f"Squaring {x}")
    return x*x
print(square(5))
# print() is a function that doesn't return anything.
# In some cases, functions are recursive (repeating). In these cases, a function calls itself inside it's definition, so when it's called, there's a loop of itself.
# Recursions are very dangerous for unbounded functions (functions without any conditions). To illustrate this, let's take up an example: 
'''def poop():
    print('poop')
    poop()
poop()'''
# RecursionError: maximum recursion depth exceeded while calling a Python object
# This error is shown because this function is unbounded, and will continue calling itself forever, which will eventually crash the computer, causing a stack overflow.
# To recurse in a bounded function is much safer.
# For example:
def factorial(num):
    if num > 0:
        if num == 1:
            return 1
        else:
            return num*factorial(num-1)
    else:
        return "Can't calculate factorial for negative numbers."
# Here, the bound is num = 1, after which it doesn't recurse farther, therefore avoiding RecursionError
# Recursion is EXTREMELY IMPORTANT! You need to get a very good grip over it.
# Functions are objects. They can be put into variables, and can be taken as arguments. In an Object Oriented Programming Language (OOP) such as Python, everything is an object.
# To prove this, let's look at an example:
def cube(num):
    return num*num*num
multiply_by_itself_thrice = cube
print(cube(5))
# 125
print(multiply_by_itself_thrice(5))
# Also 125, which proves that the two objects are the exact same