# ~List Comprehensions~
# List comprehensions are a unique way of quickly creating a list with Python

# Beginner way of making a list
mystring = 'hello' # Making a list out of variable 'mystring'

mylist = [] # Creates list
for letter in mystring: # for loop to parse through string variable 'mystring'
    mylist.append(letter) # For every letter, append to list 'mylist'

print(mylist)
print("")
# Using list comprehension
# Let's compare the original method with the comprehension method

# Original method
print("Using original method:")
myname = 'Mark'

name_list = []
for letter in myname: # for b in c
    name_list.append(letter) # name_list.append(a)

print(name_list, "\n")

# List comprehension
print("Using List comprehension")
name_list = [letter for letter in myname] # [a for b in c]
print(name_list)

# Using arithmetic functions
print("Using arithmetic functions with list comprehensions\n")
print("Printing out numbers 0 - 100 in steps of 10:")
numlist = [num for num in range(0,101,10)]
print(numlist)

# You can type-cast as well since range is just a generator function
# and will not print out any values
print("\nType-casting the value into a list:")
print(list(num for num in range(0,101,10)), "\n")

# Modifying base values
# Getting values from range 0 - 100 in steps of 10 and multiplying by 2
print("Modifying base values to be multiplied by 2")
numlist2 = [num*2 for num in range(0,101,10)]
print(numlist2)

# Creating a Celsius to fahrenheit converter
# ((C) * (9/5)) + 35 = F
c_values = [20, 15, 12.5, 30] # Given Celsius values
f_values = [((num) * (9/5) + 35) for num in c_values] # Formula for converting into Fahrenheit
n = 0 # Counter for indexing through f_values generate list

print(f"Celsius values converted into Fahrenheit:")
for item in f_values:
    print("Celsius: {0:5} | Fahrenheit: {1:}".format(c_values[n], f_values[n]))
    n+=1
print("")

# This method can also utilize boolean functions
numlist1 = [1, 3, 4, 5, 6, 10, 19, 11]
even_numbers = [num for num in numlist1 if num%2 == 0]
print(f"Even numbers:\n{even_numbers}\n")

# Printing out the results but squared
even_numbers_squared = [num**2 for num in numlist1 if num%2 == 0]
print(f"Even numbers squared:\n{even_numbers_squared}\n")

# if-else statements can be put first in the comprehension but be careful about readability
print("Using boolean statements first before declaring range:")
arg_func = [(x if x%2 == 1 else 'EVEN') for x in range(0,11)] # ['(boolean)' for 'value' in 'range()']
print(arg_func)
print("")
# Nested loops in list comprehensions
# Construct basic format
print("Performing nested loops in list comprehensions")
nlist = [] # Creating space for list
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        nlist.append(x*y)
    if x < 6: # Find a way to add this append to the list comprehension
        nlist.append('|')
print(nlist)

# Construct using list comprehension
nlist1 = [x*y for x in [2,4,6] for y in [1, 10, 10]]
# Now reconstruct coding to take in variables
# Basic
print("Nested loop using variables")
var1 = [2, 4, 6]
var2 = [1, 10, 100]
nlist_b = []
for x in var1:
    for y in var2:
        nlist_b.append(x*y)
print("")

# List Comprehension
print("List comprehension using variables")
nlist_c = [x*y for x in var1 for y in var2]
print(nlist_c)
print("")

# Lastly de construct code to basic format:
"""
lst = [ x**2 for x in [x**2 for x in range(11)]]
"""
print("Deconstructing: lst = [ x**2 for x in [x**2 for x in range(11)]]\n")
print("List comprehension:")
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst,"\n")

print("Basic format")
lst1 = []
lvar1 = []

# Nested for loop
print("Nested \'for\' loop:")
for x in range(11):
    lvar1.append(x**2)
print(lvar1)

# Un-nested for loop
print("Un-nested \'for\' loop utilizing nested \'for\' loop:")
for x in lvar1:
    lst1.append(x**2)
print(lst1)

# List comprehension
print("\nList comprehension")
lvar1 = list(x**2 for x in range(11)) # Generation for range of numbers -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)