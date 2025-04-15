# This is an if statement. It checks whether the given condition is true. If it is, it performs a task. The format is: 
# if (condition):
#   task
# The task it has to perform has to be indented one tab (four spaces)
# You can even put pass as the task if you want it to do nothing
# For example: 
if (1 == 1):
    print(1)
    print("Hello")
# The given code printed to the console, because the condition evaluated to True (the condition was correct)
# You can even pass (do nothing)
if (1 == 1):
    pass
# You can check for anything and do anything with an if-condition.
# Now, we are going to look at an if-else clause. It's syntax is similar to an if statement's, except it has an additional else statement, which tells the computer what to do if the condition evaluates to False.
if (1 != 1):
    print(7)
else:
    print(4)
# The else part doesn't need a condition
# You can even add multiple elif(s) between the if and the else. For example: 
if (1 != 1):
    print(0)
elif (1 == 1):
    print(9)
# The first elif statement is only evaluated if the if statement evaluates to False, and so on for the second and third elifs. The second elif only evaluates if the first elif fails, and the third elif only evaluates if the second elif fails, and so on.
# The else part only operates if all the preceding if(s) and elif(s) fail
# For a condition, if is the only part that is necessary, and the elif(s) and else are just optional
# A for statement repeats a statement multiple times
# It's syntax is: 
# for i in range(start, stop, step):
#   statement to be repeated
# It has an indexing variable. It is usually set to (i), but you can set it to whatever you want.
# The range function has three parameters: start, stop, and step (IN ORDER!!!!!!!!!!!!)
# The start tells the loop what to define the indexing variable at before the first iteration, the stop tells the loop when to stop (it stops when the indexing variable is at the value it will be just before the stop)), and the step tells it how much to increase the indexing variable by after each iteration
# Only the stop is necessary. The start, if no value is given, is automatically set to 0, and the step is set to 1.
# For example:
for i in range(7):
    print("Hello World")
# Or:
for j in range(2,91,2):
    print(j)
# Or:
for j in range(3,41,2):
    if j > 19:
        print(j)
    elif j == 19:
        print("ffurgfiwr")
    else:
        print("uregfwignfifogn")
# You can add an else, to make a for-else statement. The else part executes when the loop finishes
# For example:
for i in range(10,0,-1):
    print(f"T-minus {i} seconds!")
else:
    print("Take-off!")
# A negative step means the indexing variable is decreasing
# You can add a break statement in the loop. A break statement 'breaks out of' or exits the loop.
# For example:
for i in range(3,10,2):
    print(i)
    if i == 7:
        print("Breaking out!")
        break
# The break statement breaks out of the loop at 7. The loop is supposed to go till 9, but the break breaks out of it at i = 7.
# Another statement is the continue statement. If the continue statement is run, it skips to the next iteration of the loop.
# For example:
for i in range(1,11,1):
    if i == 5:
        continue
    print(i)
# In this, 5 isn't printed, because of the if-condition.
# Because of the continue statement, it skips to the next iteration (6) without printing.
# IN FOR-ELSE, THE ELSE PART DOESN'T RUN IF THE LOOP BREAKS OR CONTINUES!
# A while statement repeats not for a fixed duration, but till the condition proves to be False. It has no indexing variable.
# It checks the condition at every iteration. If the condition is False, it stops.
# While loops can be infinite (while True, while 1 == 1, while 1 != 2), or they may never run (while False, while 1 != 1, while 1 == 2).
# For example:
counter = 0
while counter < 10:
    print(counter)
    counter += 1
# Or:
'''while True:
    print("a")'''
# This code is commented because it will crash the computer, as it goes on forever.
# Or:
while False:
    print("This will not run")
# This code will never run
# A while-else clause can also be put.
# The else part will run when the condition evaluates to False.
# For example:
counter = 10
while counter > 0:
    print(f"T-minus {counter} seconds!")
    counter -= 1
else:
    print("Take-off!")
# A flag is basically a general-purpose 'off-switch' for any control flow.
# For example, in a program that checks whether a given std::string contains only 'a':
std::string = input("Enter a std::string: ").strip().lower()
flag = False
counter = len(std::string)-1
while counter >= 0:
    if std::string[counter] != "a":
        flag = True
        break
    counter -= 1
if flag:
    print("This input does not only contain 'a'.")
else:
    print("This input only contains 'a'.")
# In another example, which checks whether a number is prime or composite:
num = int(input("Enter a number: "))
flag = False
if num == 1:
    print("Neither prime nor composite!")
else:
    for number in range(2,num,1):
        if num % number == 0:
            flag = True
            break
    if flag:
        print("Composite!")
    else:
        print("Prime!")