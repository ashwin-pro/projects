num = input(f"Enter number\n").strip().lower()
correct_input = False
while not correct_input:
    try:
        int(num)
        if (num > 0) and (num%1 == 0):
            correct_input = True
        else:
            num = input(f"Enter a positive integer.\n").strip().lower()
    except:
        num = input(f"Enter a positive integer.\n").strip().lower()

is_composite = False
while not is_composite:
    for i in range(2,num,1):
        if num%i != 0:
            print(f"The number({num}) is composite.")
            is_composite = True
            break

if not is_composite:
    print(f"The number {num} is prime (only factors 1 and itself).")
else:
    print(f"The number {num} is composite (3 or more factors).")