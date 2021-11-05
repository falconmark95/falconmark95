# ~Introduction to String Formatting~

# Variables 'player' and 'points' for string formatting example
player = 'Thomas'
points = 33

# Concatenation method
# The value of points is wanted as a literal or a string in this case
# the use of str() converts the selected value into a string
print("Last night, "+player+" scored "+str(points)+" points." )

# String formatting method
# Brackets {} provide placeholders for desired values
print(f'Last night, {player} scored {points} points.')

# Formatting with placeholders
# The modulo '%' is referred to as a "string formatting operator"
# You can use '%s' to inject strings into print statements for example:
print("I am inserting %s here" %'something')

# You are able to insert multiple string values
# This requires the values to be set in order. For example:
print("I am inserting something %s and %s" %('right here','over here'))

# If 'right here' and 'over here' have been switched, this will cause the strings
# to print in a different order. For example:
print("I am inserting something %s and %s" %('over here','right here'))

# You can assign these strings to variables then call them within the statement
first_name = 'Mark'
location = 'Southwest Airlines'
print("My name is %s and I am working at %s" %(first_name, location))

# Format Conversion Methods
# Two methods to note are '%s' and '%r' using str() and repr().
# '%r' and repr() deliver the string reprsentation of the object INCLUDING:
# QUOTATION MARKS AND ANY ESCAPE CHARACTERS
print('He said his name was %s.' %'Fred') # First output shows Fred without quotation marks
print('He said his name was %r.' %'Fred') # Second output shows Fred with the quotation marks

# The '%s' operator converts what it detects into a string that is also including INTEGERS and FLOATS
# The '%d' operator converts numbers to integers first, without rounding
print('I wrote %s programs today.' %3.75) # The first statement will show the '3.75' but as a literal character
print('I wrote %d programs today.' %3.75) # The second statement converts to an integer and does not round

# Python has the ability to parse multiple conversion tools in a statement.
# For example:
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))

# ~The .format() method~
print('This is a string with an {}'.format('insert')) # Basic Syntax

# Objects can be called by position
print('The {2} {1} {0}'.format('fox','brown','quick'))

# Objects an also be assigned keywords
# IF you had noticed you can also assign a variable within those keywords instead the values
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))

# Use .format() to avoid using any duplications making the work easier
print('A %s saved is a %s earned.' %('penny','penny')) # This statement requires the keyword to be coded twice
print('A {p} saved is a {p} earned.'.format(p='penny')) # This statement assigns keyword to a variable(p) instead
print('\n')

# Alignment, padding and precision with .format()
# Curly braces allow for assignment of field lengths, left/right alignments, rounding parameters and more
# Syntax for curly braces goes as:
# {Placevalue of keyword : Length of padding}
print('{0:8} | {1:9}'.format('Fruit', 'Quantity', 'placeholder')) # E.G. 1 = Fruit, 2 = Quantity, 3 = placeholder
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
print('\n')

# You can align text using <, ^, or >
# For example
print('Padding with alignments')
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
print('\n')
# This also allows preceding the alignment operator with a padding character
print('Padding with desired leading character')
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
print('\n')

# Field widths and float precision are handled in a way similar to placeholders
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}\n'.format(13.579))

# Formatted string literals (f-strings)
# Offers several benefits over .format() method
# E.G. Bringing variables immediately into the string rather than passing them through the method .format(var)
myName = 'Mark'
print(f"He said his name is {myName}")
# You can get the string representation using !r
print(f"He said his name is {myName!r}\n")

# f-strings Float formatting {value:{width}.{precision}}
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}\n")
