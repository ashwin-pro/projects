def fib(fib_list=[0,1],end=int(input('Enter the end of the fibonacci sequence').strip()),iter=2):
    while iter < end:
        fib_list.append(fib_list[iter-1]+fib_list[iter-2])
        iter += 1
    return fib_list