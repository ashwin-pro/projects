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