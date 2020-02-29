# Lists and Loops
"""
Lists give us the ability to store large sets of data, while loops allow us to rerun sections of our code
A list is a data structure in Python that is a mutable, orderder sequence of elements. Mutable means that you can change
the items inside, while ordered sequence is in reference to index location. The first element in a list at index 0. Each element or value inside a list is known as an item
Also known as a data collection.
"""

# Declaring a List of Numbers
nums = [5, 10, 15.2, 20]
print(nums)

# Accessing Elements Within a List
print(nums[1])      # will output the value at index 1 = 10
num = nums[2]      # saves index value 2 into num
print(num)        # prints value assigned to num

# Declaring a List of Mixed Data Types
num = 4.3
data = [num, "word", True]      # the power of data collection
print(data)

# Lists Within Lists
data = [5, "book", [34, "hello"], True]      # lists can hold any type
print(data)
print(data[2])

# Accessing Lists Within Lists
# using double bracket notation to access lists within lists
print(data[2][0])     # will output 34
inner_list = data[2]   # inner list will equal [34, "hello"]
print(inner_list[1])  # will output "hello"
print(data[1][0])     # will output "b"

# Changing Values in a List
# changing values in a list through index
data = [5, 10, 15, 20]
print(data)
data[0] = 100       # change the value at index 0 - (5 to 100)
print(data)


# Variable Storage
"""
When variables are declared, the value assigned is put into a location in memory. These
locations have a specific reference ID. It’s not often you’ll need to check the ID of a
variable, but for educational purposes, it’s good to know how storage works. We would
use the id() function to check the storage location in memory for a variable:
"""
a = [5, 10]
print(id(a))     # large number represents location in memory

"""
When a list is stored in memory, each item is given its own location. Changing the
value using index notation will change the value stored within that memory block. Now,
if a variable’s value is another variable, like so:
"""
a = [5, 10]
b = a

"""
Changing the value at a specific index will change the value for both lists. Let’s see an
example:
"""

# understanding how lists are stored
a = [5, 10]
b = a
print("a: {}\t b: {}".format(a, b))
print("Location a[0]: {}\t Location b[0]: {}".format(id(a[0]), id(b[0])))
a[0] = 20                   # re-declaring the value of a[0] also changes b[0]
print("a: {}\t b: {}".format(a, b))

# copying a list
# using [:] to copy a list
data = [5, 10, 15, 20]
data_copy = data[:]         # a single colon copies the list
data[0] = 50
print("data: {}\t data_copy: {}".format(data, data_copy))

# Exercises
"""
1. Sports: Define a list of strings, where each string is a sport. Then output each
sport with the following line “I like to play {}”...
"""
# solution
sports = ["rugby", "soccer", "tennis", "cricket"]
print("I like to play {}".format(sports[0]))

"""
2. First Character: For the following list, print out each item’s first letter. (output
should be ‘J’, ‘A’, ‘S’, ‘K’)
names = [‘John’, ‘Abraham’, ‘Sam’, ‘Kelly’]
"""
# solution
names = ['John', 'Abraham', 'Sam', 'Kelly']
print(names[0][0], names[1][0], names[2][0], names[3][0])

# Loops give the ability to run code more than once.
# For Loops
"""
Every for loop begins with the keyword “for”. Then you define a temporary variable, sometimes
known as a counter or index. Next is the “in” keyword, followed by the range function
(which will be explained later). Lastly, we have a colon to end the statement. All for loop
will follow this exact structure of keyword, variable, keyword, function, and colon.
"""
# for loop using range
for num in range(5):
    print("Value: {}".format(num))

# Range()
"""
Range allows us to count from one number to another while being able to define where to start and end
and how much we increment or decrement by. When used with a for loop, it gives us the ability to loop a certain number of times.
Range defaults to starting a 0 and increments by 1 each time.
Note: range() counts up to but not including.
"""
# providing the start, stop and step for the range function
for num in range(2, 10, 2):
    print("Value: {}".format(num))      # will print all evens between 2 and 10

# Looping by Element
"""
 When working with data types that are iterable, meaning they have a collection of elements that can be looped over, we can write the for loop differently:
"""
# printing all characters in a name  using the 'in' keyword
name = "John Smith"
for letter in name:
    print("Value: {}".format(letter))


# Continue Statement
"""
Now that we’ve seen how a loop works, let’s talk about a few important statements that
we can use with loops. The first is the continue statement. Once a continue statement is
hit, the current iteration stops and goes back to the top of the loop. Let’s see an example:
"""
# using the continue statement within a foor loop
for num in range(5):
    if num == 3:
        continue
    print(num)

# Break Statement
"""
Break statement allows us to break out of a loop at any point in time. Once a break is read, the loop completely stops,and no more
code within the loop is run. These are useful for stopping a loop when a condition is met.

Note If you use a double loop, the break statement will only break out of the loop
that the statement is within. Meaning, it will not break out of both loops if the break
statement is used within the inner loop.
"""
# breaking out of a loop using the 'break' keyword
for num in range(5):
    if num == 3:
        break
    print(num)

# Pass Statement
"""
The pass statement is simply a placeholder so that the program doesn't break.
"""
# setting a placeholder using the 'pass' keyword
for i in range(5):
    # TODO: add code to print number
    pass

"""
Using "TODO" is general practice for setting a reminder.
"""

# Exercises
"""
1. Divisible by Three: Write a for loop that prints out all numbers from 1 to 100
that are divisible by three.
"""
# solution
for number in range(0, 100, 3):
    print("Multiples of 3 from 1 to 100: {}".format(number))
"""
2. Only Vowels: Ask for user input, and write a for loop that will output all the
vowels within it. For example:
>>> "Hello" ➔ "eo"
"""

# solution
#userInput = input("Please enter your input: ")


# While Loops
"""
A while loop is used when you need to loop based on a condition rather than counting.
"""
# while loop
health = 10
while health > 0:
    print(health)
    health -= 1         # forgetting this line will result in a infinite loop


# While Vs. For
"""
For loops are generally used when you need to count or iterate over a collection of elements. While loops are generally used when doing condition-based
looping. When using a while loop, often you’ll use boolean variables. Each loop has their use cases; in most cases it’s personal preference, but the general rule of thumb is
counting with for loops, conditions with while loops.
"""
"""
Note The pass, break, and continue statements all work the same way for while loops as well.
"""

# Infinite Loops
"""
An infinite loop will continue to run until the program breaks, the computer is shut down, or until time stops. Knowing
this, stay away from creating infinite loops. Here is an example of an infinite loop:
>>> game_over = False
>>> while not game_over:
>>>           print(game_over)

If you were to run this, eventually you would have to shut down your code editor and restart it (or at least the kernel). This is because the game_over variable
never becomes True, and the condition is running until game_over becomes True. Always make sure you have a way to exit your loops, whether it be by a break or by a condition.
"""

# Nested Loops
# A loop with a loop
# When using nested loops, the inner loop must always finish running, before the outer loop can continue.

# a nested loop
for i in range(2):        # outside loop
    for j in range(3):    # inside loop
        print(i, j)


# Exercises
"""
1. User Input: Write a while loop that continues to ask for user input and runs
until they type “quit”.
"""
# solution

"""
2. Double Loop: Write a for loop within a while loop that will count from 0 to 5,
but when it reaches 3, it sets a game_over variable to True and breaks out of
the loop. The while loop should continue to loop until game_over is True. The
output should only be 0, 1, 2.
"""
# solution


# Working with Lists
# Checking Length - how many items in a list? use len() function
# check number of items within a list
nums = [5, 10, 15]
length = len(nums)          # len() returns an integer
print(length)


# Slicing Lists
# Slicing follows the same arguments as the range function start, stop,step
# accessing specific items of a list with slices
print(nums[1:3])      # will output items in index 1 and 2
print(nums[:2])       # will output items in index 0 and 1
print(nums[::2])      # will print every other index -0,2,4, etc
print(nums[-2:])      # will output the last two items in list

# Adding Items to a List
# .append() - will always add the value within the parenthesis to the back of the list
# adding an item to the back of a list using append()
nums = [10, 20]
nums.append(5)
print(nums)     # outputs [10,20,5]

# .insert() - requires an index to insert a value into a specific location
# adding a value to the beginning of a list
words = ["ball", "base"]
words.insert(0, "glove")      # first number is the index, second is the value
print(words)


# Removing Items - two main methods are .pop() and .remove()

# .pop()
# By default, the pop method removes the last item in the list; however you can specify an index to remove it.
# This method is also used to save the removed item too. When pop is used, it not only removes the last item but also returns it.
# This allows saving of that value into a variable to be used later.

# using pop to remove items and saving to a variable to use later
items = [5, 'ball', True]
items.pop()         # by default removes the last item
removed_item = items.pop(0)         # removes 5 and saves it into the variable
print(removed_item, "\n", items)

# .remove()
# The method allows us to remove items from a list based on their given value:
# using the remove method with a try and except
sports = ["baseball", "soccer", "football", "hockey"]
try:
    sports.remove("soccer")
except:
    print("That item does not exist in the list")
print(sports)


# Working with Numerical List Data
# Frequently used functions are min, max and sum
# using min, max and sum
nums = [5, 3, 9]
print(min(nums))    # will find the lowest number in the list
print(max(nums))    # will find the highest number in the list
print(sum(nums))    # will add all numbers in the list and return the sum


# Sorting a List
# sorted() -  will work on either numerical or alphabetical lists but not one that is mixed.
# Also returns a copy of the list, so it doesn't alter the original.
# Usually used if you need to keep the original intact.
# using sorted on lists for numerical and alphabetical data
nums = [5, 8, 0, 2]
sorted_nums = sorted(nums)     # save to a new variable to use later
print(nums, sorted_nums)     # the original list is in tact

# .sort()
# Sort is used for the same purpose as the previous function but will change the original list directly.
# sorting a list with .sort()
nums = [5, 0, 8, 3]
nums.sort()
print(nums)


# Conditionals and Lists
# Using "in" and "not in" Keywords
# using conditional statements on a list
names = ['Jack', 'Robert', 'Mary']
if "Mary" in names:
    print("Found")          # will run since Mary is in the list
if "Jimmy" not in names:
    print("Not Found")      # will run since Jimmy is not in the list

# Checking an Empty List
# using conditionals to see if a list is empty
nums = []
if not nums:        # could also say 'if nums == []'
    print("empty")

# Loops and Lists

# Using For Loops
# using a for loop to print all items in a list
sports = ["Baseball", "Hockey", "Football", "Basketball"]
for sport in sports:
    print(sport)

# Using While Loops
# using the while loop to remove a certain value
names = ["Bob", "Jack", "Rob", "Bob", "Robert"]
while "Bob" in names:
    names.remove("Bob")     # removes all instances of 'Bob'
print(names)


# Exercises
"""
1. Remove Duplicates: Remove all duplicates from the list below. Hint: Use the
.count( ) method. The output should be [‘Bob’, ‘Kenny’, ‘Amanda’]
>>> names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']
"""
# solution
names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']


"""
2. User Input: Use a while loop to continually ask the user to input a word, until
they type “quit ”. Once they type a word in, add it to a list. Once they quit the
loop, use a for loop to output all items within the list.
"""
# solution
