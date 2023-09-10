from math import tanh as t
'''Importing the package pygal.'''
numbers = [i for i in range(1,11)]
'''List containing a range of numbers from 1 to 10.'''
squares = [number**2 for number in numbers]
'''List containing the squares of all the numbers from 1 to 10.'''
def complex(sin,radian):
    '''Defining function'''
    if t(sin) > t(radian):
        '''Checking if tanh of parameter "sin" is greater than tanh of parameter "radian".'''
        if t(sin) > 0-t(radian):
            return t(pow(radian,sin))
        '''If tanh "sin" > additive inverse of tanh "radian" then returns tanh "radian"^"sin"'''