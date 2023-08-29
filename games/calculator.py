def add(a,b):
    return a+b

def subract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exponentialize(base,exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/exponentialize(base,abs(exponent))
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    
def root(num,index=2):
    if index > 0:
        return pow(num,1/index)
    else:
        return 'Invalid operation. Enter a positive index.'
    
