# ~Lists in Python~
my_list = ['one','two','three',4,5]
v1 = my_list[1]
v2 = len(v1)

# Printing the range of items to display from the list
print(my_list[2:4])

# Getting the length of the item in the list
print(len(my_list[2:4]))

# Concatenating strings
# Note: Concatenating strings does not make a permanent change to the list
print(my_list + ['new item']) # 'new item' cannot be printed unless called within the print statement

# 'new item' needs to be assigned to the my_list variable
my_list += ['new item']
print(my_list)

# You can use the '*' operator for duplicates
# This change is not permanent
print(f"\n{my_list*4}")

# Basic List Methods
# the .append() method allows for permanently adding an item at the end of a list
new_list = ['a', 'b', 'c']
new_list.append('added item')
print(new_list)

# The .pop() method can be used to "pop off" an item from a list
# by default the last index is popped off
new_list.pop() # No index specified
print(new_list) # Last item or index was popped off
new_list.pop(0) # Pops first item off list
print(new_list)

# You are also able to assign a popped off item
new_list.append('added item') # adding 'added item' for pop off assignment example
print(new_list, "\n")

popped_item = new_list.pop()
print(f"Now assigning {popped_item!r} to: popped_item")

# Print statements allow for .sort() and .reverse() to organize items in a list
# Reversing this list will just print it out backwards
l1 = [1, 'a', 2, 'b', 3, 'c']
print(f"List before .reverse():\n{l1}")
l1.reverse()
print(f"List after using .reverse():\n{l1}\n")

# Using .sort() on this list will not work because it is not supported between
# instances of str and int in the same statement
l2 = [1, 'a', 2, 'b', 3, 'c']
print(f"List before using .sort():\n{l2}")
# l2.sort()
# print(f"List after using .sort():\n{l2}") # Error will happen here

# Nesting Lists
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
# Syntax goes [List item within matrix][item within list item]
matrix = [lst_1,lst_2,lst_3]
print(matrix[1][1]) # Printing '5' out of the second list
print(matrix[2]) # Printing the last list item
print(matrix[1]) # Printing the second list item