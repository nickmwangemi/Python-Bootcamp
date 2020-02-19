# Comments & Basic Data Types
# this is a comment
print("Hello")  # this is also a comment

"""
  This is a multi-line comment
"""

print("Hello")  # this is also a comment

# Integers
# the following are all integers
print(2)
print(10)

# Floats - any number with a decimal point is known as floating point data types
# the following are all floats
print(10.953)
print(8.0)  # even this number is a float

# Booleans
# the following are booleans
print(True)
print(False)

# Strings - Also known as "String Literals"
# Actual definition is Strings in Python are arrays of bytes representing unicode characters
"""
Strings are a set of characters, symbols, numbers, whitespace, 
and even empty space between two sets of quotation marks.
"""

# the following are strings
print("")
print("There's a snake in my boot!")
print('True')

# Variables
"""
We declare a name on the left side of the equals operator("="),
and on the right side, we assign the value that we want to save to use later.
"""
first_name = "Nick"
print(first_name)

# Handling Naming Errors
Sport = 'baseball'    # capital 'S'
print(Sport)          # lowercase 'S'

# Integer and Float Variables
num1 = 5      # storing an integer into a variable
num2 = 8.4    # storing an float into a variable
print(num1, num2)   # you can print multiple items using commas

# Boolean Variables
# storing a boolean into a variable
switch = True
print(switch)

# String Variables
# storing strings into a variable
name = 'John Smith'
fav_number = '9'
print(name, fav_number)

# Using Multiple Variables
# using two variables to create another variable
result = num1 + num2
print(result)

# Using Operators on Numerical Variables
# adding, deleting, multiplying, dividing from a variable
result += 1  # same as saying result = result + 1
print(result)
result *= num1  # same as saying result = result * num1
print(result)

# Overwriting Previously Created Variables
# defining a variabl and overwriting it's value
name = 'John'
print(name)
name = "Sam"
print(name)

# Whitespace - characters used for spacing and have an "empty" representation.
# In the context of python, it means tabs and spaces.

# Working With Strings
# String Concatenation
# using the addition operator without variables
name = "John" + " " + "Smith"
print(name)

# using the addition operator with variables
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

# Formatting Strings
""" .format() method - works by putting a period directly after the ending string quotation,
followed by the keyword "format". Within the parenthesis after the keyword are the variables that will be
injected into the string.
"""
# injecting variables using the format method
name = "John"
print("Hello {}".format(name))
print("Hello {}, you are {} years old!".format(name, 28))

# f Strings
""" By putting the letter "f" in front of a string, you're able to inject a variable into a
string directly in line. This is important, as it makes the string easier to read when it gets
longer, making it the preferred method to format a string.
"""
# using f strings
name = "John"
print(f"Hello {name}")

# Formatting in Python 2
""" Python 2 doesn’t include the .format() method; instead you would use percent
operators to mark the location of the variable being injected. The following is an
example to inject the variable “name” into the location of “%s”. The letter after the
percent operator signifies the data type. For integers, you would use “%d” for digit.
After the string closes, you would place a percent operator, followed by the variables
you would like to use. Let’s look at an example:
"""
# one major difference between versions 2 & 3
name = "John"
print('Hello, %s' % name)

# python 2 multiple variable formatting
first_name = "John"
last_name = "Smith"
print("Hello, %s %s" % (first_name, last_name))
# surround the variables in parenthesis

# String Index
"""
When a computer saves a string into memory, each character within the string is
assigned what we call an “index.” An index is essentially a location in memory. Think of
an index as a position in a line that you’re waiting in at the mall. If you were at the front
of the line, you would be given an index number of zero. The person behind you would
be given index position one. The person behind them would be given index position two and so on.
"""
# using indexes to print each element
word = "Hello"
print(word[0])    # outputs 'H'
print(word[1])  # outputs 'e'
print(word[-1])   # outputs 'o'

# String Slicing
"""
Slicing is used mostly with Python lists; however, you can use it on strings as well. Slicing is essentially when you only want
a piece of the variable, such that if I only wanted “He” from the word “Hello”, we would
write the following:
"""
print(word[0: 2])            # will output 'He'
print(word[0: 4])            # will output 'Hell'
print(word[0: 5])            # will output 'Hello'

# printing every other letter
print(word[0:5:2])            # will output 'Hlo'

"""
The first number in the bracket is the starting index; the second is the stopping index
"""
name = "John"
print("Hello {}".format(name))
print("Hello {}, you are {} years old!".format(name, 28))

# Exercises
"""Variable Injection: Create a print statement that injects an integer,
float, boolean, and string all into one line. The output should look like
“23 4.5 False John”.
"""
# Solution
number1 = 5
number2 = 4.5
isMarried = True
name = "John"
print("{} {} {} {}".format(number1, number2, isMarried, name))


"""Fill in the Blanks: Using the format method, fill in the following
blanks by assigning your name and favorite activities into variables:
"{ }'s favorite sports is { }."
"{ } is working on { } programming!"
"""
# Solution
name = "Nick"
sport = "rugby"
subject = 'Python'
print("{}'s favorite sports is {}.".format(name, sport))
print("{} is working on {} programming!".format(name, subject))


# String Manipulation

# .title() - Capitalizes all first letters in each word of a string
# using the title method to capitalize a string
name = 'john smith'
print(name.title())

# other methods
# .lower()
print(name.lower())     # outputs "john smith"
# .upper()
print(name.upper())     # outputs "JOHN SMITH"

# .replace() -
"""works like a find and replace tool. It takes in two values within its parenthesis, 
one it searches for and the other it replaces the searched value with:
"""
# replacing an exclamation point with a period
words = "Hello there!"
print(words.replace("!", "."))      # outputs "Hello there."

"""
Note: For the replace to be stored properly afterward, 
we would have to redeclare our words variable: words = words.replace("!", ".")
"""

# .find() - Will search for any string we ask it to
# finding the starting index of our searched term
s = "Look over that way"
print(s.find("over"))     # outputs "5"

# .strip()
"""In cases where you want to get rid of a certain character on the left and right side of
a string, you would use the strip method. By default, it will remove spaces. Let’s try
running the following:
"""
# removing white space with strip
name = "    john    "
print(name.strip())

# other methods
# .lstrip
print(name.lstrip())
# .rstrip
print(name.rstrip())

# .split()
# It returns a list i.e separates the words in a sentence into a group of words, stored within a list.
# converting a string into a list of words
s = "These words are separated by spaces"
print(s.split(" "))

# Exercises
"""Uppercasing: Try manipulating the string “uppercase” so it prints out as all
uppercase letters. You’ll need to look up a new method.
"""
# solution
myString = "uppercase"
print(myString.upper())

"""Strip Symbols: Strip all the dollar signs from the left side of this string “$$John
Smith”. Try it with .lstrip( ) and .strip( ). To see a description on how to use
the strip method further, try using the help function in Python by typing the
following:
>>> help(" ".strip)"""

# solution
myString = "$$John Smith"
print(myString.strip('$'))
