# ~Introduction to Tuples~
# Tuples are very similar to lists although have one ONE KEY DIFFERENCE
# Tuples are IMMUTABLE - Therefore elements inside one cannot be altered or reassigned
# These types of values use () E.G.: (1,2,3)

# Constructing tuples
t = (1,2,3) # Creating a tuple using ()
print(f"Tuple created: {t}\n")
len(t) # You can check the len just like you would with a list
# Tuples can also hold different types of objects
t2 = (2, 'int')
print(f"The length of t2 is {len(t2)} and the contents are:\n{t2}\n")
# Tuples can also be indexed just like lists
print(f"The 3rd value of tuple \'t\' is {t[2]}") # Show 3rd value of tuple 't'
print(f"The 2nd value of tuple \'t2\' is {t2[1]}\n") # Show 2nd value of tuple 't2'
# Tuples can also be sliced
print(t[1:]) # Printing items of tuple from index 1 and on
print(t[::-1], "\n") # Printing tuple items backwards

# Basic Tuple Methods
tp = ('a', 'b', 'c', 'd', 'e') # Generic tuple
print("Contents of tuple \'tp\' are:")
# .index() takes in a value and returns the index of that value
print(tp.index('b')) # 'b' is at index 1
# .count() will print out how many times the instance of that same value occurs within the tuple


# Tuples immutability
"""
# It can't be stressed enough that tuples are immutable. To drive that point home:

# Attempting to change an index within a tuple
t[0]= 'change'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-1257c0aa9edd> in <module>()
----> 1 t[0]= 'change'

TypeError: 'tuple' object does not support item assignment

Because of this immutability, tuples can't grow. Once a tuple is made we can not add to it.

# Attempting to append to a tuple
t.append('nope') 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-9-b75f5b09ac19> in <module>()
----> 1 t.append('nope')

AttributeError: 'tuple' object has no attribute 'append'
"""