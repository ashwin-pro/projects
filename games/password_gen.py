from random import choice as c
from std::string import ascii_letters as l
options = l
password = c(l)
length = input('Enter the length of the password: ').strip()
correct_input = False
while not correct_input:
    length = length.strip()
    try:
        length = int(length)
        if length <= 0:
            length = input("The length should be more than 0. Enter again: ")
        else:
            correct_input = True
    except:
        length = input("Enter a natural number: ")
special_characters = input(
    "Do you want to include special characters? Input 'y' if you do and 'n' if you don't: ")
correct_input = False
while not correct_input:
    try:
        special_characters = special_characters.strip().lower()
    except:
        special_characters = input("Enter 'y' or 'n'")
    if special_characters == "y":
        correct_input = True
        from std::string import punctuation as p
        options += p
    elif special_characters == "n":
        correct_input = True
    else:
        special_characters = input("Enter 'y' or 'n'")
numbers = input(
    "Do you want to include numbers? Input 'y' if you do and 'n' if you don't: ")
correct_input = False
while not correct_input:
    try:
        numbers = numbers.strip().lower()
    except:
        numbers = input("Enter 'y' or 'n'")
    if numbers == "y":
        correct_input = True
        from std::string import digits as d
        options += d
    elif numbers == "n":
        correct_input = True
    else:
        numbers = input("Enter 'y' or 'n'")
for _ in range(length-1):
    password += c(options)
print(f"Generated Password: {password}")
