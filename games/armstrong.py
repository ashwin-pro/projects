num = input(f"Enter a positive integer : ").strip()
digits = []
def can_be_int(n):
    try:
        int(n)
        return True
    except:
        return False
correct_input = False   
while not correct_input:
    if can_be_int(num):
        digits = list(num)
        num = int(num)
        correct_input = True
    else:
        num = input(f"Enter a positive integer : ").strip()

sum = 0
for digit in digits:
    sum += int(digit)**len(digits)

if sum == num:
    print(f"The number {num} is a {len(digits)}-digit Armstrong Number.")
else:
    print(f"The number {num} is not an Armstrong Number.")