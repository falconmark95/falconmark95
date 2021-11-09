# ~Sets and Booleans~

# Sets are an unordered collection of 'unique' elements. We can construct them by using the set() function
x = set() # Assigning a set to variable 'x'
x.add(1) # Set use .add() to add values to it
print(x)
# If you try to add the same value again it will not save
x.add(2)
print(f"Set \'x\' before attempting to add another \'1\':\n{x}")
x.add(1)
print(f"Set \'x\' after attempting to add \'1\':\n{x}\n") # The '1' will not show because sets only show unique values

# Sets do however allow for the ability to separate out the unique values from a list
list1 = [1,1,2,2,3,4,5,6,1,1] # A list with repeats
print(set(list1), "\n") # Prints out only the first occurrence of each number

# Booleans
"""
 True = 1
 False = 0
 None = None
"""
print("Booleans\n")
# You can assign a boolean value to a variable
a = True # Assigning True to a variable
print(f"The value \'a\' is assigned: {a}") # Printing out variable's value
# You can print the result of two comparisons
print("Is 1 > 2?", 1>2)
# If a variable does not have a value assigned to it then 'None' will return
b = None # Assigning \'b\' to None
print(f'What is the value of b?\n{b}')