# ~Dictionaries in Python~
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1']) # Values are called by their key

# Dictionaries are able to be flexible in the data that it holds
# Key 1: Integer
# Key 2: List of Integers
# Key 3: List of string items
my_dict2 = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Calling the dictionary item in this case it is a list
print(my_dict2['key3']) # Last dictionary item
# Calling the index within that dictionary item
print(my_dict2['key3'][0]) # First item

# Dictionary items can also call methods
print(my_dict2['key3'][0].upper()) # Making that index item upper cased while calling within print statement

# A key's values are mutable allowing for values to be adjusted
print(f"Value of my_dict2 key1 value: {my_dict2['key1']}")
my_dict2['key1'] = my_dict2['key1'] - 123
print(f"Value of key1 after modifying the key value: {my_dict2['key1']}\n\n")

# Dictionary values have can use shorthand operators and perform the same operations
print(f"Value of my_dict2 key1 value: {my_dict2['key1']}")
my_dict2['key1'] += 123
print(f"Value of key1 after using addition shorthand operator: {my_dict2['key1']}\n\n")

# Nesting with dictionaries
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}},'key2':{'nestkey2':{'subnestkey2':'value2'}}}
print(d['key1']['nestkey']['subnestkey']) # Keep calling the keys
print(d['key2']['nestkey2']['subnestkey2']) # Calling key2's values

# Some dictionary methods
# .keys() pulls all the keys from the dictionary
# .values() pulls all the keys' values from the dictionary
# .items () returns all the keys and their values as tuples

d2 = {'key1':1,'key2':2,'key3':3} # Generic dictionary
print(f"List of keys from dictionary d2:\n{d2.keys()}\n") # Printing all the keys from dictionary 'd2'
print(f"List of key values from dictionary d2:\n{d2.values()}\n") # Printing all the key values from dictionary 'd2'
print(f"Tuple list of keys and values from dictionary d2:\n{d2.items()}\n") # Printing dictionary 'd2' items as tuples
