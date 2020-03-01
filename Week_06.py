# Data Collections and Files
# dictionaries, sets, tuples, frozensets

# Dictionaries
"""
Is a collection of unordered data, which is stored in key-value pairs.
"Unordered" refers to the way it is stored in memory as it is not accessible through an index, rather it 
is accessed through a key.
Dictionaries work like a real-life dictionary, where the key is the word and the values are the definition.
Dictionaries are useful for working with large data, mapped data, CSV files, APIs, sending or receiving data and much more.
"""

# declaring a dictionary variable
import csv
empty = {}    # empty dictionary
person = {"name": "John Smith"}
# dictionary with one key/value pair
customer = {
    "name": "Morty",
    "age": 26
}     # dictionary with two key/value pairs
print(customer)

# accessing dictionary information
# acccessing dictionary information through keys
person = {"name": "John"}
print(person["name"])  # access information through the key

# Using the get method
"""
the get() method can be used to retrieve information. The major difference
between using this method and the previous way of accessing a value is that the get
method won’t throw a key error. If the key doesn’t exist, it will simply return “None”. You
may also add in a second argument in the call, in order to have the program return a
more specific data type. 
"""
# using the get method to access dictionary information
person = {"name": "John"}
print(person.get("name"))     # retrieves value of name key as before
# get is a secure way to retrieve information
print(person.get("age", "Age is not available."))

# dictionaries with lists - dictionaries become powerful when you start working with data collections as values
# storing a list within a dictionary and accessing it
data = {"sports": ["baseball", "football", "hockey", "soccer"]}
print(data[["sports"][0]])      # first access the key, then the index

# improperly storing a list within a dictionary
sports = ["baseball", "football", "hockey", "soccer"]
# sports_dict = dict(sports)    # will produce error, no key
sports_dict = dict({"sports": sports})


# Lists with Dictionaries
"""
The combination of lists within dictionaries and vice-versa can become confusing when
trying to figure out how to access information. Always remember lists are indexed, and
dictionaries use keys. Depending on the order of the data stored, you’ll need to do one
or the other first. When a list is storing a dictionary, you need to access that dictionary
by the index first. After that you have access to the key-value pairs within the dictionary.
"""
# storing a dictionary within a list and accessing it
data = ["John", "Dennis", {"name": "Kirsten"}]
print(data[2])    # the dictionary is in index 2
print(data[2]["name"])    # first access the index, then access the key

"""
Note: Be very careful when using nummbers for keys
"""

# Dictionaries with Dictionaries
"""
Dictionaries are powerful and efficient due to how they're stored in memory. Often, you'll want 
to use dictionaries as the value for your key-value pairs.
"""
# storing a dictionary within a dictionary and accessing it
data = {
    "team": "Boston Red Sox",
    "wins": {"2018": 108, "2017": 93}
}
print(data["wins"])   # will output the dictionary within the wins key
print(data["wins"]["2018"])   # first access the wins key, then the next key

# Exercises
"""
1. User Input: Ask the user for their name and age, and then create a dictionary
with those key-value pairs. Output the dictionary once created.
"""
# solution
person = {}

name = input("What's your name? ")
person["name"] = name

age = int(input("What's your age? "))
person["age"] = age

print(person)
"""
2. Accessing Ingredients: Output all the ingredients from the following list within
the “ingredients” key using a for loop:
133Chapter 6
Data Collections and Files
>>> pizza = {
>>>     'ingredients': ['cheese', 'sausage', 'peppers']
>>> }
"""
# solution
"""
Data collections allow us to work with large data as they are stored in key-value pairs. 
Remember that data is accessed through keys.
"""

# Working with Dictionaries -  add data, manipulating data, removing key-value pairs and iterating
# Adding New Information
# adding new key/value pairs to a dictionary
car = {"year": 2018}
car["color"] = "Blue"
print("Year: {} \t Color: {}".format(car["year"], car["color"]))


"""
Note: As of Python, 3.7 dictionaries are ordered by default. In older versions of
Python, key-value pairs didn’t always keep their order. You would have needed to
use an OrderedDict( ).
"""

# Changing Information
# Altering key-value pairs is exactly like adding a new pair. If the key exists, it simply
# overwrites the previous value; however, if it doesn't exist, it will create a new key-value pair
# updating a value for a key/value pair that already exists
car = {"year": 2018, "color": "Blue"}
car["color"] = "Red"
print("Year: {} \t Color: {}".format(car["year"], car["color"]))

# Deleting Information
# deleting a key/value pair from a dictionary
car = {"year": 2018}
try:
    del car["year"]
    print(car)
except:
    print("That key does not exist")

"""
When deleting key-value pairs, if the key doesn't exist, it will crash the program. 
To avoid that, we use a try/except.
"""

# Looping a Dictionary
# Dictionaries are iterable like lists with 3 methods for doing so.
# You can iterate over both the keys and values together,only keys, or only values.

# Looping only keys
# looping over a dictionary via the keys
person = {"name": "John", "age": 26}
for key in person.keys():
    print(key)
    print(person[key])      # will output the value at the current key

"""
As we iterate over person, our temporary variable of key will be equal to each key name. This still gives us the ability to access each value by using
our key variable.
"""

# looping only values
# looping over a dictionary via the values
person = {"name": "John", "age": 26}
for value in person.values():
    print(value)

"""
We won’t have access to the key names, but for this method, we’re only trying to get the values anyways. Our temporary variable value will
store each value from the key-value pairs as we iterate over person.
"""

# looping key-value pairs
"""
If you need the ability to access both the key and value, then you’ll want to use the
.items() method. This approach will assign two temporary variables instead of one:
"""
# looping over a dictionary via the key/value pair
person = {"name": "John", "age": 26}
for key, value in person.items():
    print("{}:{}".format(key, value))
"""
As we iterate over person, the key-value pairs are assigned to their respective temporary variables of key and value. We now have access
to both easily.
Note: The temporary variable names are usually called “k” and “v.”
"""

# EXERCISES
"""
1. User Input: Declare an empty dictionary. Ask the user for their name, address,
and number. Add that information to the dictionary and iterate over it to show
the user.
"""
# solution
person = {}
name = input("Enter your name: ")
person["name"] = name

address = input("Enter your address: ")
person["address"] = address

number = input("Enter your phone number: ")
person["number"] = number

for key, value in person.items():
    print("{}:{}".format(key, value))

"""
2. Problem-Solving: What is wrong with the following code:
>>> person = { 'name', 'John Smith' }
>>> print(person['name'])
"""
# solution
person = {'name': 'John Smith'}
print(person['name'])


# Tuples, Sets, Frozensets

# Tuples
# A tuple is identical to a list, except it is immutable, meaning it cannot be altered once declared.
# Tuples are useful for storing info that you don't want to change.
# They're ordered like lists, so you can iterate through them using an index.

# declaring a tuple
"""
To declare a tuple, you use a comma to separate two or more items. Lists are denoted
by their square brackets on the outside, whereas tuples can be declared with optional
parenthesis. It’s more likely they’re declared with parenthesis as it’s easier to read. Let’s
see an example:
"""
# declaring a tuple
t1 = ("hello", 2, "hello")    # with parens
t2 = True, 1                  # without parens
print(type(t1), type(t2))     # both are tuples
# t1[0] = 1     # will crash, tuples are immutable once declared
# Only way to overwrite the data within a tuple is to re-declare the entire tuple.


# Sets
# Share the same characteristics of lists and dictionaries.
"""
A set is a collection of info like a list; however, like a key in a dictionary, sets can only contain unique values.
They're unordered meaning that they cannot be accessed by index but rather by the value itself like dictionary keys.
They can be iterated through just like dictionary keys.
Sets are practical in situations of storing unique items.
"""
# Declaring a set
"""
Set can be declared in two ways:
1. By using the keyword "set" followed by parenthesis and enclosing square brackets.
2. By using a set of curly brackets.
"""
# declaring a set
s1 = set([1, 2, 3, 1])    # using the set keyword and square brackets
s2 = {4, 4, 5}            # using curly brackets, like a dictionary
print(type(s1), type(s2))
s1.add(5)   # using the add methos to add new items to a set
s1.remove(1)  # using the remove method to get rid of the value 1
print(s1)     # notice when printed it removed the second "1" at the end


# Frozensets
# Are essentially the combination of a set and tuple.
# They're immutable, unordered and unique.
# These are perfect for sensitive info like bank account numbers, as you wouldn't want to alter those.
# They can be iterated over, but not indexed.

# Declaring a Frozenset
# Use the the keyword "frozenset" followed by parenthesis and enclosing square brackets.
# declaring a frozenset
fset = frozenset([1, 2, 3, 4])
print(type(fset))

# Exercise
"""
1. User Input: Ask the user to input as many bank account numbers as they’d
like, and store them within a list initially. Once the user is done entering
information, convert the list to a frozenset and print it out.
"""
# solution
userInput = int(
    input("How many bank account numbers would you like to enter? "))

# create list to store bank accounts
bankAccounts = []
# loop the user input to capture the number of bank accounts
for s in range(userInput):
    bankAccNo = int(input("Enter bank account number: "))
    bankAccounts.append(bankAccNo)

# convert list into a frozenset
bankAccountsFSet = frozenset(bankAccounts)
print(bankAccountsFSet)


"""
2. Conversion: Convert the following list into a set of unique values. Print it out
after to check there are no duplicates:
>>> nums = [3, 4, 3, 7, 10]
"""
# solution
nums = [3, 4, 3, 7, 10]

# convert to frozenset since they hold unique values
numFSet = frozenset(nums)
print(numFSet)


# Reading and Writing Files
# Depending on the type of program you're writing, you'll need to save or access info.

# Working with Text Files
"""
Python comes with an open() function that allows creation and modification of files.
This function accepts two parameters, the file name and the mode. If the file name exists, then
it will simply open the file for modification; otherwise, it will create the file.
The mode refers to how Python opens and works with the file.
For instance, to grab info from a file, you open it up to read. This allows you to work with the file while not accidentally changing it.
"""
# opening/creating and writing to text file
f = open("test.txt", "w+")   # open file in writing and reading mode
f.write("this is a test")
f.close     # anytime you open a file, you must close it
# reading from a text file
f = open("test.txt", "r")
data = f.read()
f.close     # anytime you open a file, you must close it
print(data)

"""
Note: Mode “w” will overwrite the entire file. Use “a” for appending.
"""

# Writing to CSV Files
"""
CSV files work with  data by separating a comma between each cell. Also known as tabular data structure.
Python has a default library known as "csv" to work with CSV files.
You need to import that in order to work with CSV files. After importing, we'll use the second method of opening 
files using the "with" keyword.
This concept looks like a while loop, so that while the file is open, we can work with it, and once the block of code is done 
running, it closes the file automatically.
"""
# opening/creating and writing to a csv file
with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "City"])
    writer.writerow(["Nick Mwangemi", "Taiwan"])

# Reading from CSV Files
with open("test.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)
