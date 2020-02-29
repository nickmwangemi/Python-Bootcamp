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
