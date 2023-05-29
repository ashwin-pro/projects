'''favourite_pizzas = ['double paneer chipotle','moroccan pasta pizza','margherita']
for pizza in favourite_pizzas:
    print(f"I like {pizza.title()} pizza.")
print('I really love pizza.')'''

'''animals = ['dog','cat','rabbit','fish','hamster','bird']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print('Any of these animals would make a great pet.')'''

'''for i in range(1,21):
    print(i)'''

'''numbers = list(range(1,1000001))
for number in numbers:
    print(number)'''

'''numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))'''

'''for i in range(1,21,2):
    print(i)'''

'''for i in range(3,31,3):
    print(i)'''

'''for i in range(1,11):
    print(i**3)'''

'''list = [i**3 for i in range(1,11)]
print(list)'''

'''foods = ['pizza','pasta','noodles','gojjin','red owlaki','biriyani','cake','cupcake','chocolate']
print(f"The first three items in the list are {foods[:2]} and {foods[2]}.")
print(f"The three items from the middle of the list are {foods[3:5]} and {foods[5]}.")
print(f"The last three items in the list are {foods[6:8]} and {foods[-1]}.")'''

'''pizzas = ['double paneer chipotle','moroccan pasta pizza','margherita']
friend_pizzas = pizzas[:]
pizzas.append('garden fresh veggies')
friend_pizzas.append('paneer tikka')
print('My favourite pizzas are:\n')
for pizza in pizzas:
    print(f"\t{pizza}")
print("My friend's favourite pizzas are:\n")
for pizza in friend_pizzas:
    print(f"        {pizza}")'''

'''foods = ('bread','tea','dosa','coffee','idli')
print(foods)
foods = ('bread','tea','coffee','muffin','porridge')
print(foods)'''

'''alien_color = 'yellow'
points = 0

if alien_color == 'blue':
    points += 1
elif alien_color == 'yellow':
    points += 3
else:
    points += 5

print(f"You have {points} points.")'''

'''age = int(input('Enter your age.\n'))
if age < 2:
    type = 'a baby'
elif age < 4:
    type = 'a toddler'
elif age < 13:
    type = 'a kid'
elif age < 20:
    type = 'a teenager'
elif age < 65:
    type = 'an adult'
else:
    type = 'an elder'

print(f"You are {type}.")'''


'''favourite_fruits = ['orange','strawberry','blueberry']
check = ['banana','orange','blueberry','strawberry','apple','pineapple','jackfruit']
for fruit in check:
    if fruit in favourite_fruits:
        print(f"You would really like a {fruit}!")'''


'''usernames = ['ashwin','anush','kasammy','appy','admin']
if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thanks for logging in again.")
else:
    print("We need to find some users!")'''

'''current_users = ['ashwin','anush','kasammy','appy','admin']
username_attempt = input("Please enter your wanted username.\n")
if username_attempt.lower() not in current_users:
    print("Your username is accepted!")
else:
    print("This username is already taken.")'''

'''numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")'''

