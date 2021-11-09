# ~Introduction to Loop statements~

# The 'for' loop statement
"""
General Statement

for ITEM in OBJECT:
    (statements to execute action)

- For example
# Printing out all the letters in the alphabet
for LETTER in ALPHABET:
    print(LETTER)
"""
# Creating list of integers 1 - 10
list1 = [1,2,3,4,5,6,7,8,9,10]
# 'for' loop that is printing out the numbers from first index to last each on a new line
for num in list1:
    print(num)

# Printing out only the even numbers in that list
for num in list1: # For the number in list1
    if num%2 == 0: # If that number modulo 2 is equal to zero (indicating an even number)
        print(num) # Print out that number
print(" ")

# Printing out the even numbers in the list
# Unless (else) it is an odd number
for num in list1:
    if num%2 == 0:
        print(num)
    else:
        print(f"Odd number:{num}")
print("")

# Using the 'for' loop iteration to keep a running tally
# E.G. summing up the integers in the list
list_sum = 0 # Creating list sum variable to store the running data in
for num in list1:
    list_sum += num
print(f"The sum of the list is: {list_sum}")

# The same iteration can be done with a string
myString = 'This is a string'
for letter in myString: # The variable letter is being created when the for loop is coded in
    print(letter)
print(" ")

# For loops can also iterate through a tuple just as it would with a list
tup = (1, 2, 3, 4, 'int')
for item in tup:
    print(item)
print(" ")

# Tuples have a special quality with 'for' loops allowing the tuple to be printed as a whole
# If the Tuples are within a list then they can be called as an item just as you would with an item within a tuple
# Setting 3 tuple variables
tup1 = ('cat', 'dog', 5)
tup2 = (4, 'eight')
tup3 = ('kite', 'flag', 'horse')

list2 = [tup1, tup2, tup3]
for t in list2: # Calling each tuple item using the 'for' loops statement
    print(t)
print(" ")

# Tuple Unpacking
list3 = [(2, 4), (6, 8), (10, 12)]
for t in list3: # Printing each pair out
    print(t)

for(x, y) in list3: # Printing out the y values of the tuples
    print(y)
