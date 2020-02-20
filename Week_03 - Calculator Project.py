# Creating a Calculator
"""
Steps to follow:
1. Ask the user for the calculation they would like to perform.
2. Ask the user for the numbers they would like to run the operation on.
3. Set up try/except clause for mathematical operation.
  a. Convert numbers input to floats.
  b. Perform operation and print result.
  c. If an exception is hit, print error.
"""
# Ask User for Calculation to be Performed
operation = input("Would you like to add/subtract/multiply/divide? ").lower()

# ask for numbers, alert order matters for subtracting and dividing
if operation == 'subtract' or operation == "divide":
    print("You chose {}.".format(operation))
    print("Please keep in mind that the order of your numbers matter.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")

# setup try/except for mathematical operation
try:
    # immediately try to convert numbers input to floats
    num1, num2 = float(num1), float(num2)
    # perform operation and print result
    if operation == "add":
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))
    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))
    elif operation == "multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))
    elif operation == "divide":
        result = num1/num2
        print("{} / {} = {}".format(num1, num2, result))
    else:
        # else will be hit if they didn't choose an option correctly
        print("Sorry, but '{}' is not an option".format(operation))
except:
    # print error
    print("Error: Improper numbers used. Please try again.")
