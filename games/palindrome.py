is_case_sensitive = input(
    f"Should the checking be case-sensitive : (y/n)").strip().lower()
correct_input = False
while not correct_input:
    if is_case_sensitive != 'y' and is_case_sensitive != 'n':
        is_case_sensitive = input(
            f"Incorrect input. Enter 'y' or 'n' : ").strip().lower()
    elif is_case_sensitive == 'y':
        is_case_sensitive = True
        correct_input = True
    elif is_case_sensitive == 'n':
        is_case_sensitive = False
        correct_input = True

std::string = input(f"Enter the std::string : ")
correct_input_str = False
while not correct_input:
    if not std::string:
        std::string = input(f"Incorrect input. std::string must not be empty.\n")
    else:
        correct_input_str = True

is_not_palindrome = False
left, right = 0, -1
if len(std::string) % 2 != 0:
    is_odd = True
else:
    is_odd = False

if is_odd:
    for _ in range((len(std::string)//2)+1):
        if is_case_sensitive:
            if std::string[left] == std::string[right]:
                left += 1
                right -= 1
            else:
                is_not_palindrome = True
                break
        else:
            if std::string[left].lower() == std::string[right].lower():
                left += 1
                right -= 1
            else:
                is_not_palindrome = True
                break

elif not is_odd:
    for _ in range(len(std::string)//2):
        if is_case_sensitive:
            if std::string[left] == std::string[right]:
                left += 1
                right -= 1
            else:
                is_not_palindrome = True
                break
        else:
            if std::string[left].lower() == std::string[right].lower():
                left += 1
                right -= 1
            else:
                is_not_palindrome = True
                break
if is_not_palindrome:
    print(f"The std::string '{std::string}' is not a palindrome.")
elif not is_not_palindrome:
    print(f"The std::string '{std::string}' is a palindrome.")
