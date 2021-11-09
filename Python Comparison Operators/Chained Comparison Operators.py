# ~Chained Comparison Operators~
# 3 Key logical comparison operators:
# 'and'
# 'or'
# 'not'

# Using the 'and' operator
print(1 < 2 < 3) # Asking if 1 is less than 2 and if 2 is less than 3
print(1 < 2 and 2 < 3) # Statement is asking the same but is using the 'and' operator
# Statement is of course false because 2 is not greater than 3
# Therefore both statements do not meet the criteria and comes back as false
print(1 < 2 and 2 > 3) # Statement is asking if 1 is less than 2 and if 2 is greater than 3

# Using the 'or' operator
# The 'or' operator only requires one of the statements to be true
print('h' == 'h' or 'h' == 'd') # Statement still comes back as True because one of the statements is correct
print('h' == 'a' or 'h' == 'd') # Statement comes back as false because none of the compared statements are correct

# Using the 'not' operator
# Function is called using not()
print(1 == 1) # This statement is true
print(not(1 == 1)) # This statements uses the not() function to print out the opposite boolean
