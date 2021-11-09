# ~if, elif, else Statements~
# Statement syntax goes as follows:
"""
function.variable:
    code-statement
"""

# Using the 'if' statement
# If 'x' is true then print out 'x is true'
x = True
if x == True:
    print('x is true')

# If 'x' is true then print out 'x is true'
# Otherwise print out 'x is not true

x = False
if x == True:
    print('x is true')
else:
    print('x is not true\n')

# Creating multiple branches
# Using elif (else if) or else you can add more parameters to the comparison statements

car_color = 'red'
if car_color == 'blue':
    print('The car is blue')
elif car_color == 'white': # elif statements require a boolean statement for a comparison
    print(f"The car's color is white")
else:
    print("The car is a red color")
