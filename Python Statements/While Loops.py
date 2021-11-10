# ~Introduction to while loops~
# One of the most general ways to perform an iteration
# A 'while' statement will continually perform that statement as long as the condition is true
"""
General Format

while some_condition:
    code statements...
else:
    code statements...
"""

# Printing and incrementing x up to but not included at 10
x = 0
while x < 10:
    print(x)
    x+=1
print(" ")

# Incrementing until y equals 10
y = 0
while y < 10:
    print(f"{y} is still less than 10. Adding one more")
    y += 1
    print(y)
else:
    print(f"{y} is equal to 10")
print(" ")
# Break, Continue, and Pass statements
"""
break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all.
"""

# Break statement
xlist = [1,2,3,4]
print(f"The working list: {xlist}")
print("Using the break statement if \'2\' is detected")
for item in xlist:
    if item == 2: # If item equals '2' then break out of the closest loop entirely
        break
    print(item)
print("")

# Continue statement
print("Using the continue statement if \'2\' is detected")
for item in xlist:
    if item == 2: # If item is equal to '2' then break out of current iteration and start next one
        continue
    print(item)   # Take note where you have your print statement to allow for the detection to occur first
print(" ")        # to get the desire results

# Pass statement
"""
x= [1,2,3]

for item in x:
    # This comment will cause EOF parse issue if ran
    pass # This pass statement allows program to pass this parameter with no expectations
print('End of my script')
"""