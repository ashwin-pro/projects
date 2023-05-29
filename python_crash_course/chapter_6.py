'''person = {}
first_name = input('Enter your first name.\n')
person['first_name'] = first_name
last_name = input('Enter your last name.\n')
person['last_name'] = last_name
age = int(input('Enter your age.\n'))
person['age'] = age
for information in person:
    print(person[information])'''

'''favourite_numbers = {'ashwin':7,'anush':10,'kasammy':3,'appy':27,'random':17}
for person in favourite_numbers:
    print(f"{person.title()}'s favourite number is {favourite_numbers[person]}.")'''

'''favourite_languages = {'ashwin':'python','anush':'java','kasammy':'python','appy':'javascript'}
for name,language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")'''

'''rivers = {'nile':'egypt','amazon':'brazil','indus':'india'}
for river,country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")'''

'''already_taken = {'Sarah':'C','edward':'ruby','phil':'python','jen':'python'}
should_take = {'Sarah':'c','jen':'python','ashwin':'python','anush':'java'}
for name in should_take:
    if name in already_taken:
        print(f"Thank you {name.title()}, for taking the favourite languages poll.")
    else:
        print(f"{name.title()}, you should take the favourite languages poll.")'''

'''info = {}
for i in range(15):
    name = input('Enter your name.\n')
    marks = float(input('Enter your marks out of 100.\n'))
    info[name] = marks
    print("Let's go to the next user.\n")

for name,marks in info.items():
    if marks >= 90:
        print(f"{name.title()} got a distinction.")
    elif marks >= 75:
        print(f"{name.title()} got merit.")
    elif marks >= 60:
        print(f"{name.title()} got first class.")
    elif marks >= 50:
        print(f"{name} just passed.")
    else:
        print(f"{name} failed.")'''

'''favourite_languages = {}
for _ in range(15):
    name = input('Enter your name.')
    language = input('Enter your name.')
    favourite_languages[name] = language

for name,language in favourite_languages.items():
    print(f"{name}'s favourite language is {language}.")'''

'''person_1 = {'first name' : 'ashwin','last name' : 'rao','location' : 'bengaluru'}
person_2 = {'first name' : 'anush','last name' : 'rao','location' : 'bengaluru'}
person_3 = {'first name' : 'random','last name' : 'random','location' : 'unknown'}
people = [person_1,person_2,person_3]
for person in people:
    for type,info in person.items():
        print(f"{person['first name'].title()}'s {type} is {info.title()}.")
    print('')'''

'''dog = {'name' : 'bruno','owner' : 'ashwin'}
cat = {'name' : 'smurfy','owner':'ashwin'}
rabbit = {'name' : 'betsy','owner' : 'dhanya'}
bird = {'name' : 'rio','owner' : 'ashwin'}
pets = [dog,cat,rabbit,bird]
for pet in pets:
    for type,info in pet.items():
        print(f"{pet['name'].title()}'s {type} is {info.title()}.")'''

'''ashwin = ['Tokyo','Mount Kilimanjaro','New york','london']
anush = ['US','London','Tokyo','Sydney']
kasammy = ['kerala','manali','hyderabad']
appy = ['kodaikanal','mount everest']
favourite_places = {'ashwin' : ashwin,'anush' : anush,'kasammy' : kasammy,'appy' : appy}
for name,places in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        if place == 'US':
            print(f"        US")
        else:
            print(f"        {place.title()}")
    print('')'''


'''ashwin = [7,11,15]
kasammy = [3,6,10]
anush = [16,4,8]
appy = [18,12,5]
favourite_numbers = {'ashwin' : ashwin,'kasammy' : kasammy,'anush' : anush,'appy' : appy}
for name,numbers in favourite_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"        {number}")
    print('')'''

