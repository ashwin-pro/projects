# Some code that I use very often in my programs, so that I can import them and use them easily:
# tbc means to be checked:

def input_with_validation(prompt, condition, default):
    if not condition in ["integer", "whole number", "positive integer", "negative integer", "float", "positive float", "negative float",]:
        raise AttributeError("The condition has to be valid")
    tbc = input(prompt) or default
    while True:
        try:
            if condition == "whole number" or "integer" in condition:
                tbc = int(tbc)
            elif "float" in condition:
                tbc = float(tbc)
            if condition == "whole number" and tbc >= 0:
                return tbc
            elif "positive" in condition and tbc > 0:
                return tbc
            elif "negative" in condition and tbc < 0:
                return tbc
            elif "positive" not in condition and "negative" not in condition:
                return tbc
            raise ValueError
        except ValueError:
            tbc = input("Enter valid input: ").strip()
        except Exception as e:
            print(f"An error ocurred:\n{e}")


def yes_or_no(prompt, default):
    tbc = input(prompt) or default
    while True:
        tbc = tbc.strip().lower()
        if tbc in ["yes", "y",]:
            return True
        if tbc in ["no", "n",]:
            return False
        tbc = input("Enter 'y', 'yes', 'n', or 'no': ")


def in_list(raw_tbc, list_, condition, default=None, prompt='That value is already taken, please enter another: '):
    if default:
        tbc = input(raw_tbc) or default
    else:
        tbc = input(raw_tbc)
    if condition not in ['in', 'not in']:
        raise AttributeError("Condition has to be 'in' or 'not in'")
    while True:
        if (condition == 'in' and tbc in list_) or (condition == 'not in' and tbc not in list_):
            return tbc
        else:
            if default:
                tbc = input(prompt) or default
            else:
                tbc = input(prompt)


def in_range(tbc, ll, hl, condition, default):
    while True:
        tbc = input_with_validation(tbc, condition, default=default)
        if ll <= tbc <= hl:
            return tbc
        tbc = input_with_validation(
            input(f"Enter a number between {ll} and {hl} (inclusive): "), condition, default)


class Queue(list):
    def __init__(self, maxsize):
        self.data = []
        self.maxsize = maxsize
        self.size = len(self.data)

    def isfull(self):
        self.update_size()
        if self.size == self.maxsize:
            return True
        else:
            return False

    def isempty(self):
        self.update_size()
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, element):
        if not self.isfull():
            self.data.append(element)
            self.size += 1
        else:
            return -1

    def dequeue(self):
        if not self.isempty:
            self.size -= 1
            return self.data.pop(0)
        else:
            return -1

    def update_size(self):
        self.size = len(self.data)

    def update_maxsize(self, value):
        self.maxsize = value


def forbidden_character(char, iterable_p):
    iterable = input(iterable_p)
    while True:
        if char not in iterable:
            return iterable
        else:
            iterable = input(
                f"The character '{char}' is not allowed, enter again: ")
