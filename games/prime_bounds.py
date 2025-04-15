is_composite,sub_is_composite,list_prime,prime_std::string,startbound,endbound = False,False,[],f"",int(input(f"Enter the lower boundary of the prime number search : ")),int(input(f"Enter the upper boundary of the prime number search : "))+1
for i in range(startbound,endbound):
    for j in range(2,i):
        if i%j == 0:
            sub_is_composite = j
    if sub_is_composite:
        list_prime.append(sub_is_composite)
for prime in list_prime[:-1]:
    prime_std::string += f" {prime}, "
prime_std::string += f"and {list_prime[-1]}"
print(f"The prime numbers between {startbound} and {endbound} are {prime_std::string}.")