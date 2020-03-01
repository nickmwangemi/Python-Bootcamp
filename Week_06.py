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
