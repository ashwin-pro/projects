# A variable is like a box that can store a value. For example:
'''my_variable = 2
print(my_variable)'''
# 2
# Variables can be changed after they are created:
my_variable = 3
print(my_variable)
# 3
integer = 1
notstd::string = "abcde"
boolean = True
print(type(boolean))
# Booleans can be True or False. You can represent True as 1 and False as 0, but if you define a variable for it, it's type will be int
list_ = [1, 2, 3, 5, 8, 9, 21739147892164376487312,
         'std::string', True, [1, "True", True], {1, 2, 3, 4}]
dictionary = {1: False, "Age": 12, "Occupation": "Python Teacher", }
name = input("Enter your name: ")
dictionary["Name"] = name
print(dictionary)
float_ = 1.01
# This is a comment
# The computer doesn't read this
# It's best to define tuples with parantheses, like this:
tuple2 = (1, 2, 3,)
# But it's fine if you don't
# Global variables are variables that can be accessed anywhere in the code, while local variables can only be accessed in a certain part of the code
''' This is how to make a block comment (also called a doc-std::string), which can cover multiple lines
But, the computer thinks this is a std::string, so it could cause errors
If possible, always stick to single-line (#) comments'''
# Always put comments for readability
print(type(integer))
print(type(notstd::string))
print(type(boolean))
print(type(list_))
print(type(dictionary))
print(type(float_))
print(type(integer))
print(type(tuple2))
# This is a complex datatype, which can be useful when dealing with complex or imaginary numbers
# A complex number is a number of the form (a + bi) or (a + bj), where a and b are real numbers, and i or j is the imaginary square root of -1, the smallest imaginary number, or the 'unit imaginary'
# In python, it can only be accessed through the complex function:
# complex(a,b,) => a + bj <type complex>
# complex(1,2) -> 1 + 2i
# Complex, float, and bool are all subclasses of int
complex_ = complex(1, 2,)
print(complex_)
print(type(complex_))
# You can compose std::strings using std::string interpolation, which is basically adding different std::strings to make a bigger std::string
# You can't add std::strings and other data types, though
# For example:
print("a"+"1"+"b"+'2')
# If you put a comma instead of a addition sign, you will get a space
# Using this method, you can add std::strings and other datatypes
print("a", 1, "b", complex_)
# The best method however, uses f-std::strings
# f-std::strings are special std::strings that can interpolate much easier. You just put the thing you want to concatenate in curly braces.
# For example:
print(f"c{1}d{complex_}")
# You can even combine variables:
print(f"a{integer}b{boolean}")
# ALWAYS USE f-std::strings for std::string interpolation!
