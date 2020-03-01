# Functions
"""
Functions give us the ability to make our programs much more powerful and clean
while also saving us time. We use functions is because of the ability to write once and call repeatedly.


Overview
• How to use functions and what they are
• Passing data around using parameters
• Returning data from functions
• Understanding scope and its importance
• Creating a shopping cart program
"""

# Creating and Calling Functions
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""
# writing a function


def printInfo():      # defines what the function does when called
    print("Name: John Smith")   # calls the function to run
    print("Age: 45")            # calls the function again


printInfo()
printInfo()

# Function Stages
"""
There are two stages: function definition and function call.
Function definition is where you define the function name, any parameters it's supposed to accept,
and what it's supposed to do in the block of code associated with it.
The second stage is known as the function call. Functions will never run until called,
so you can define as many functions as you’d like, but if you never call one of them, then
nothing will happen. When you call a function, it will run the block of code within the
definition
"""

# UDF vs. Built-in
"""
Built-in functions are included in Python to serve a specific purpose to help build applications.
UDFs are user-defined functions.
"""
# performing a calculation in a function


def calc():
    x, y = 5, 10
    print(x+y)


calc()      # will run the block of code within calc and output 15

# Exercises
"""
1. Print Name: Define a function called myName, and have it print out your name
when called.
"""
# solution


def myName():
    name = "Nick"
    print(name)


myName()

"""
2. Pizza Toppings: Define a function that prints out all your favorite pizza toppings
called pizzaToppings. Call the function three times.
"""
# solution


def pizzaToppings():
    topping1, topping2, topping3 = "Cheese,", "Pepperoni,", "Chicken"
    print(topping1, topping2, topping3)


pizzaToppings()
pizzaToppings()
pizzaToppings()


# Parameters
"""
Parameters are temporary variables declared on the function definition. To call a function with
different values, you need to use parameters. This is an arbitrary variable name that you use to reference the value within the function block; however, you usually want it to
be relevent to the data that you're working with. When calling the function, you would pass in the necessary value to run the block of code with.
"""
# Passing a Single Parameter


def printName(full_name):
    print("Your name is: {}".format(full_name))


printName("John Smith")
printName("Amanda")


# Multiple parameters
# passing multiple parameters into a function
def addNums(num1, num2):
    result = num1+num2
    print("{} + {} = {}".format(num1, num2, result))


addNums(5, 8)
addNums(3.5, 5.5)

# passing a list
# using a function to square all information
numbers1 = [2, 4, 5, 10]
numbers2 = [1, 3, 6]


# def squares(nums):
#     for num in nums:
#         print(nums**2)


# squares(numbers1)
# squares(numbers2)


# Default Parameters
"""
A parameter can be associated with a default value. Take the value of pi for instance, it will always be 3.14,
so we can set a parameter called pi to that exact value to allow us to call the function with an already defined value for pi.
"""
# setting default parameter values


def calcArea(r, pi=3.14):
    area = pi*(r**2)
    print("Area: {}".format(area))


calcArea(2)   # assuming radius is the value of 2

"""
Note: Default parameters must always go after non-default parameters.
"""

# Making Parameters Optional
"""
Sometimes you need to make functions that take optional arguments. The best example
is always middle names; some people have them, and some don’t. If we wanted to write
a function that would print out properly for both situations, we would need to make the
middle name an optional parameter. We do this by assigning an empty string value as
the default:
"""
# setting default parameter values


def printName(first, last, middle=""):
    if middle:
        print("{} {} {}".format(first, middle, last))
    else:
        print("{} {}".format(first, last))


printName("John", "Smith")
printName("John", "Smith", "Paul")      # will output with middle name


# Keep in mind the order of our parameters! Parameters must line up from left to right according to the function definition.

# Named Parameter Assignment
"""
During the function call, you can explicity assign values into parameter names. This is useful
when you don’t want to mix up the order of values being passed in, as they work from left
to right by default. You can use parameter names to assign values for every parameter if
you choose, but it’s not necessary most of the time. Let’s check out an example:
"""
# explicity assigning values to parameters by referencing the name


def addNums(num1, num2):
    print(num2)
    print(num1)


addNums(5, num2=2.5)

# *args
"""
The use of *args allows you to pass a variable number of arguments into a function. This
allows you to make functions more modular. The magic isn’t the “args” keyword here
though; it’s really the unary operator ( * ) that allows us to perform this feature. You could
theoretically replace the word args with anyone, like “ *data”, and it would still work.
However, args is the default and general standard throughout the industry.
"""
# using args parameter to take in a tuple of arbitrary value


def outputData(name, *args):
    print(type(args))
    for arg in args:
        print(arg)


outputData("John Smith", 5, True, "Jess")


# **kwargs
"""
Like args, kwargs allows us to take in an arbitrary number of values in a function;
however, it works as a dictionary with keyword arguments instead. Keyword arguments
are values passed in with keys, which allow us to access them easily within the function
block. Again, the magic here is in the two unary operators ( ** ) not the keyword of
kwargs. Let’s check it out:

"""

# using kwargs parameter to take in a dictionary of arbitrary value


def outputData(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["num"])


outputData(name="John Smith", num=5, b=True)

# Exercises
"""
1. User Input: Ask the user to input a word, and pass that word into a function
that checks if the word starts with an uppercase. If it does output “True”,
otherwise “False”.
"""
# solution


def checkCaps(name):

    if name[0].isupper() == True:
        print("True")
    else:
        print("False")


name = input("Enter your name")
checkCaps(name)
"""
2. No Name: Define a function that takes in two arguments, first_name and last_
name, and makes both optional. If no values are passed into the parameters, it
should output “No name passed in”; otherwise, it should print out the name.
"""
# solution


# def checkName(first_name, last_name):
#     print("{} {}".format(first_name, last_name))


# checkName()


# Return Statement - is used to send info back to where the function call occured.
# using return keyword to return the sum of two numbers
def addNums(num1, num2):
    return num1+num2


num = addNums(5.5, 4.5)      # saves returned value into num
print(num)
print(addNums(10, 10))       # doesn't save returned value

# Ternary Operator
"""
A ternary operator is a shorthand python branching statement.
These operations can be used to assign values into a variable, or in this case, deciding what the return from a function
"""
# shorthand syntax using a ternary operator


def searchList(aList, el):
    return True if el in aList else False


result = searchList(["one", 2, "three"], 2)    # result = True
print(result)

# Exercises
"""
Full Name: Create a function that takes in a first and last name and returns the
two names joined together.
"""
# solution


def joinNames(firstName, lastName):
    return firstName + lastName


firstName, lastName = "Nick ", "Mwangemi"
print(joinNames(firstName, lastName))

"""
2. User Input: Within a function, ask for user input. Have this function return that
input to be stored in a variable outside of the function. Then print out the input.
"""

# solution


def userInput(userInput):
    faveSport = input("What's your favourite sport?")
    return faveSport


faveSport = userInput("rugby")
print(faveSport)

# Scope -deals with the accessibility of variables declared within a program
# Types: global, function, class
# Global - when you declare a variable to be accessible to an entire file or application
# Function scope is in reference to variables being declared and accessible only withi functions

# Global Scope Access - accessible to the rest of the file
# where global variables can be accessed

# number = 5


# def scopeTest():
#     number += 1       # not accessible due to function level scope


# scopeTest()

"""
Note: When passed in, it only passes the value, not the variable
"""
# Handling Function Scope

"""
When dealing with variables declared in a function, you generally won't need to access
it outside of the function. However, in order to access that value, best practice is to return it:
"""
# accessing variables defined in a function


def scopeTest():
    word = "function"
    return word


value = scopeTest()
print(value)


# In-Place Algorithms
"""
When passing variables into a function, you're simply passing the value of that variable and not the variable 
itself. Such that the following will not alter the variable num
"""

num = 5


def changeNum(n):
    n += 5
    print(num)


changeNum(num)

# Exercises
"""
1. Names: Create a function that will change the list passed in with a parameter
of name at a given index. Such that if I were to pass in “Bill” and index 1,
it would change “Rich” to “Bill.” Use the list and function definition in the
following:
>>> names = ['Bob', 'Rich', 'Amanda']
>>> def changeValue(aList, name, index):
"""
# solution

# names = ['Bob', 'Rich', 'Amanda']


# def changeValue(aList, name, index):
#     for name in names:
#         names.insert(1, "Bill")
#         return names


# print(changeValue(names, "Bill", 1))
