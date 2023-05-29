'''names = ['Ashwin','Anush','Kasammy','Appy']
for person in names:
    message = f"Hello, {person}."
    print(message)'''

'''favourite_vehicles = ['aeroplane','ship','car']
for vehicle in favourite_vehicles:
    message = f"I would like to own a {vehicle}."
    print(message)'''

'''guest_list = ["Ashwin","Ashwin's clone","Ashwin_bot"]
for person in guest_list:
    message = f"Hello, {person}, would you like to come to dinner?"
    print(message)'''

'''guest_list = ["Ashwin","Ashwin's clone","Ashwin_bot"]
not_coming = "Ashwin_bot"
not_coming_index = 2
guest_list.remove(not_coming)
guest_list.insert(not_coming_index,"Ashwin_friend")
for person in guest_list:
    message = f"Hello, {person}, would you like to come to dinner?"
    print(message)
print(f"{not_coming} can't come for dinner.")'''

'''guest_list = ["Ashwin","Ashwin's clone","Ashwin_bot"]
not_coming = "Ashwin_bot"
not_coming_index = 2
guest_list.remove(not_coming)
guest_list.insert(not_coming_index,"Ashwin_friend")
guest_list.insert(0,"Ashwin's boss")
guest_list.insert(2,"Ashwin's employee")
guest_list.append("Ashwin's brother")
for person in guest_list:
    message = f"Hello, {person}, would you like to come to dinner?"
    print(message)
print(f"{not_coming} can't come for dinner.")
print('Hello guests, we found a bigger dinner table.')'''

'''guest_list = ["Ashwin","Ashwin's clone","Ashwin_bot"]
not_coming = "Ashwin_bot"
not_coming_index = 2
guest_list.remove(not_coming)
guest_list.insert(not_coming_index,"Ashwin_friend")
guest_list.insert(0,"Ashwin's boss")
guest_list.insert(2,"Ashwin's employee")
guest_list.append("Ashwin's brother")
cancelled_guests = []
cancelled_guests.append(guest_list.pop(0))
cancelled_guests.append(guest_list.pop(2))
cancelled_guests.append(guest_list.pop(3))
cancelled_guests.append(guest_list.pop(1))
for person in cancelled_guests:
    message = f"Sorry {person}, we cannot let you join the dinner party."
    print(message)
for guest in guest_list:
    message = f"Hello, {guest}, you are still invited to the party."
    print(message)
for person in guest_list:
    message = f"Hello, {person}, would you like to come to dinner?"
    print(message)
print(f"{not_coming} can't come for dinner.")
print('Hello guests, we found a bigger dinner table.')
print('Hello guests, the new dinner table will not arrive in time for the dinner, so we are only inviting 2 guests.')'''

'''places = ['New York','Australia','Mount Kilimanjaro','Tokyo','London']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
print(places.reverse())
print(places.reverse())
print(places.sort())
print(places.sort())'''

'''guest_list = ["Ashwin","Ashwin's clone","Ashwin_bot"]
not_coming = "Ashwin_bot"
not_coming_index = 2
guest_list.remove(not_coming)
guest_list.insert(not_coming_index,"Ashwin_friend")
guest_list.insert(0,"Ashwin's boss")
guest_list.insert(2,"Ashwin's employee")
guest_list.append("Ashwin's brother")
cancelled_guests = []
cancelled_guests.append(guest_list.pop(0))
cancelled_guests.append(guest_list.pop(2))
cancelled_guests.append(guest_list.pop(3))
cancelled_guests.append(guest_list.pop(1))
for person in cancelled_guests:
    message = f"Sorry {person}, we cannot let you join the dinner party."
    print(message)
for guest in guest_list:
    message = f"Hello, {guest}, you are still invited to the party."
    print(message)
for person in guest_list:
    message = f"Hello, {person}, would you like to come to dinner?"
    print(message)
print(f"{not_coming} can't come for dinner.")
print('Hello guests, we found a bigger dinner table.')
print('Hello guests, the new dinner table will not arrive in time for the dinner, so we are only inviting 2 guests.')
print(len(guest_list))'''

'''list_of_things = ['Mount Everest','Marianna Trench','Farlands','Japan']
print(sorted(list_of_things))
print(sorted(list_of_things,reverse=True))
print(list_of_things.sort())
print(list_of_things.reverse())
print(len(list_of_things))
print(list_of_things[-1])'''

'''favourite_pizzas = ['double paneer chipotle','moroccan pasta pizza','margherita']
for pizza in favourite_pizzas:
    print(f"I like {pizza.title()} pizza.")
print('I really love pizza.')'''

'''animals = ['dog','cat','rabbit','fish','hamster','bird']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print('Any of these animals would make a great pet.')'''