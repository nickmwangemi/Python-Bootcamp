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
