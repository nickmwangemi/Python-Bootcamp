# User Input and Type Converting
# Accepting User Input
# accepting and outputting user input
print(input("What is your name?"))

# Storing User Input
# saving what the user inputs
ans = input("What is your name?")
print("Hello {}!".format(ans))

# Python defines type conversion functions to directly convert one data type to another.

# Checking the Type
# how to check the data type of a variable
num = 5
print(type(num))

# Converting Data Types
# converting a variable from one data type to another
num = "9"
num = int(num)      # re-declaring num to store an integer
print(type(num))    # checking type to make sure conversion worked

str(9)
float(5)
int(5.6)
int('9')
bool('True')
int(True)

""" 
Note: Not all data types can be converted properly. There are limits.
"""

# Converting User Input
# working with user input to perform calculations
ans = input("Type a number to add:")
print(type(ans))    # default type is string, must convert
result = 100 + int(ans)
print("100 + {} = {}".format(ans, result))


# Handling Errors
# using the try and except blocks, use tab to indent where necesary
try:
    ans = float(input("Type a number to add: "))
    print("100 + {} = {}".format(ans, 100 + ans))
except:
    print("You did not put in a valid number!")
# without try/except print statement would not get hit if error occurs
print("The program did not break!")

# Code Blocks and Indentation
"""
In Python, indentation is required for indicating a block of code.
"""

"""
Note: The indents must be consistent. 
It does not always need to be four spaces; however, a tab is four spaces, so it's usually easier to indent with tabs.
"""

# Exercises
"""
Converting: Try converting a string of “True” to a boolean, and then output its type to make sure it converted properly.
"""
# Solution
myString = bool("True")
print(type(myString))

"""
Sum of Inputs: Create two input statements, and ask the user to enter two
numbers. Print the sum of these numbers out.
"""
# Solution

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
ans = number1 + number2
print("The sum of the number is {}".format(ans))


"""
3. Car Information: Ask the user to input the year, make, model, and color of
their car, and print a nicely formatted statement like “2018 Blue Chevrolet
Silverado.”
"""
yearInput = input("Enter the year: ")
makeInput = input("Enter the make: ")
modelInput = input("Enter the model: ")
colorInput = input("Enter the color: ")
print("{} {} {} {}".format(yearInput, colorInput, makeInput, modelInput))


# If Statements
# using an if statement to only run code if the condition is met
x, y = 5, 10
if x < y:
    print("x is less than y")

# Comparison Operators
# == Equality     if x == y:
# != Inequality   if x!= y:
# > Greater than  if x > y:
# < Less than     if x < y:
# >= Greater or equal if x >= y:
# <= Less or equal    if <= y:

# Checking User Input
ans = int(input("What is 5+5? "))
if ans == 10:
    print("You got it right!")

# Logical Operators - used to combine conditional statements

# Logical Operator - "and"
""" 
Logical Operator "and" - ensures that when you check multiple conditions, both sides of the condition are True.
This means that if either the condition to the left or right of the "and" is False, then the code block will not run.
"""

# using the keyword 'and' in an 'if statement'
x, y, z = 5, 10, 5
if x < y and x == z:
    print("Both statements were true")


# Logical Operator - "or"
""" 
Logical Operator "or" checks for one or both conditions to be true. Such that if the condition to the left is False
and the condition to the right is True, the block of code will still run because at least one condition was true. An "if block" will not
run if both conditions are False.
"""
# using keyword 'or' in an 'if statement'
x, y, z = 5, 10, 5
if x < y or x != z:
    print("Both statements were true")

# Logical Operator - "not"
""" 
Logical Operator "not" checks for the opposite of a value.
"""
# using the keyword 'not' within and 'if statement'
flag = False
if not flag:                # same as saying if not true
    print("Flag is False")

"""
Note: We get the same result if we write "if flag == False".
"""

# Membership Operators
"""
Membership Operators - Used to test if a sequence appears in an object. Keywords used are "in" and "out"
"""
# Membership Operator "in" - Checks if a given object has a value in it
# using the keyword 'in' within an 'if statement'
word = 'Baseball'
if "b" in word:
    print("{} contains the character b".format(word))

# Membership Operator "out" - checks to see if an object does not include a specific value
# is essentially the opposite of "in"
# using the keyword 'not in' within an 'if statement'
word = 'Baseball'
if "x" not in word:
    print("{} does not contain the character x".format(word))

# Exercises
"""
1. Checking Inclusion – Part 1: Ask the user for input, and check to see if what
they wrote includes an “es”.
"""
# solution
userInput = input("Please enter a word: ")
if "es" in userInput:
    print("{} contains 'es'".format(userInput))
"""
2. Checking Inclusion – Part 2: Ask the user for input, and check to see if what
they wrote has an “ing” at the end. Hint: Use slicing.
"""
# solution
userInput = input("Please enter a word: ")

"""
3. Checking Equality: Ask the user to input two words, and write a conditional
statement to check if both words are the same. Make it case insensitive so that
capitals do not matter.
"""
# solution
"""
4. Returning Exponents: Ask for the user to input a number, and return that
number squared if it is lower than 10. Hint: Investigate arithmetic expressions
for exponents.
"""
# solution


"""
Elif statements - They give us the ability to run separate blocks of code depending on the condition.
They are also known as "else if statements". Elif statement is used to declare another decision based on a given condition.
Elif statements must be associated with an if statement.
Python works in top to bottom order, so
it checks the first if statement; if that statement is False, it continues to the first elif
statement and checks that condition. If that condition returns False as well, it continues
to the next conditional statement until there are no more to check. However, once a
single conditional statement returns True, all other conditionals are skipped, even if
they are True. It works so that the first conditional to return True is the only block of
code that runs.

"""
# checking more than one elif conditional statement
x, y = 5, 10
if x > y:
    print("x is greater")
elif (x+10) < y:                 # checking if 15 is less than 10
    print("x is less")
elif(x+5) == y:                   # checking if 10 is equal to 10
    print("equal")

"""
Note: Within the conditional, we perform addition, but we wrap it within parenthesis so that it executes te math operation first.
"""


# Conditionals Within Conditionals
# writing multiple conditionals within each other - multiple block levels
x, y, z = 5, 10, 5
if x > y:
    print("greater")
elif x <= y:
    if x == z:
        print("x is equal to z")          # resulting output
    elif x != z:
        print("x is not equal to z")        # won't get hit


# If Statements vs. Elif Statements

"""
A major difference that you’ll need to understand going forward is the use for elif
statements against using multiple if statements. All elif statements are connected to one
original if statement, so that once a single conditional is True, the rest do not run.
"""
# testing output of two if statements in a row that are both true
x, y, z = 5, 10, 5
if x < y:
    print("x is less")
if x == z:
    print("x is equal")

# testing output of an if and elif statement that are both true
x, y, z = 5, 10, 5
if x < y:
    print("x is less")
elif x == z:
    print("x is equal to z")


# Exercises
"""1. Higher/Lower: Ask the user to input a number. Type convert that number, and
use an if/elif statement to print whether it’s higher or lower than 100.
"""
# solution

"""
2. Find the Solution: Given the following code, fix any/all errors in order to make
it output “lower”:
x, y = 5, 10
if x > y:
      print("greater")
try x < y:
      print("lower")
"""
# solution


# Else Statements
"""
This is the default action of a decision. Else conditional statements are the end all be all of the if statement.
Sometimes you’re not able to create a condition for every decision you want to make, so that’s where the
else statement is useful. The else statement will cover all other possibilities not covered
and will always run the code if the program gets to it. This means that if an elif or if
statement were to return True, then it would never run the else; however, if they all
return False, then the else clause would run no matter what every time.

"""
# using an else statement
name = "John"
if name == "Jacob":
    print("Hello Jacob!")
else:
    print("Hello {}!".format(name))


# Complete Conditional Statement
# writing a full conditional statement with if, elif, else
name = "John"
if name[0] == "A":
    print("Name starts with an A")
elif name[0] == "B":
    print("Name starts with a B")
elif name[0] == "J":
    print("Name starts with a J")
else:                                    # Covers all other possibilities
    print("Name starts with a {}".format(name[0]))


# Exercises
"""
1. Fix the Errors: Given the following code, fix any/all errors so that it outputs
“Hello John” correctly:
>>> name = "John"
>>> if name == "Jack":
>>>           print("Hello Jack")
>>> elif:
>>>>          print("Hello John")
"""
# solution

"""
2. User Input: Ask the user to input the time of day in military time without a
colon (1100 = 11:00 AM). Write a conditional statement so that it outputs the
following:
a. “Good Morning” if less than 1200
b. “Good Afternoon” if between 1200 and 1700
c. “Good Evening” if equal or above 1700

"""
# solution
# solution
timeInput = int(input("Please enter the time in 24hr format: "))
if timeInput < 1200:
    print("Good Morning")
elif 1200 < timeInput < 1700:
    print("Good Afternoon")
else:
    print("Good Evening")
