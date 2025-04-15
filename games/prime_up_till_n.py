n = input(f"Enter a positive integer greater than 2.\n").strip()
correct_input = False
while not correct_input:
    try:
        n = int(n)
        if n > 0 and n%1 == 0 and n>2:
            correct_input = True
        else:
            n = input(f"Enter a positive integer greater than 2.\n").strip()
    except:
            n = input(f"Enter a positive integer greater than 2.\n").strip()

primes = []

for i in range(2,n+1,1):
    is_composite = False
    for sub_i in range(2,i,1):
          if i%sub_i == 0:
               is_composite = True
               break
    if not is_composite:
        primes.append(i)

prime_std::string = f"The prime numbers coming before {n} are : "
for prime in primes[:-2]:
    prime_std::string += f"{prime}, "
prime_std::string += f"and {primes[-1]}."

print(prime_std::string)