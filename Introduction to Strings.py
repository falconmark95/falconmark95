# ~Introduction to strings~

# Assigning variable name for string
name = "Mark Falcon"

# Assigning variable namelen for length of string
namelen = len(name)

# Printing out length of name
print(namelen)
print(name, "has", namelen, "characters")

# Grab everything but the first letter
print(name[1:])

# Grab everything but the last letter
print(name[:-1])

# Grab Everything
print(name[:])

# Slicing can also allow for parsing in steps like so
# variable[start:end:step]
# Steps of 1
print(name[::1])

# Steps of 2
print(name[::2])

# Using -1 to print backwards
print(name[::-1])

name2 = "bob"
name3 = "Dylan"

fullname = name2 + " " + name3
print(fullname)

# Objects are constructed as:
# object.method(parameter)

# The object you are using needs to be treated like a value and has to be assigned to a variable
# other wise it will not work
# fullname is being assigned to the object that is using the 'upper' method
# Uppercasing fullname
fullname = fullname.upper()
print(fullname)

# Lowercasing fullname
fullname = fullname.lower()
print(fullname)

# Assigning string to randstr for split example
randstr = "Hello my name is mark"

# Splitting the string and assigning to randstr
randstr = randstr.split()
print(randstr)

# You can split a string and exclude the element it was split on
randstr = "Hello my name is mark"

# IF the letter is in the middle it will stop at that letter and move to the next iteration
# until reaching another 'm'
randstr = randstr.split('m')
print(randstr)

# Enter a period after fullname to see the the methods that can be used with this object
fullname