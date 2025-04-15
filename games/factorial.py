num = input(f"Enter the positive integer for which the factorial must be found : ").strip()
while type(num)!=int or num<0 or num%1:
    num = input(f"Enter a positive integer : ").strip()
    try:
        num = int(num)
    except:  
        pass

factorial = 1
for i in range(1,num+1):
    factorial *= i
print(f"{num}! is equal to {factorial}")