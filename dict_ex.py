"""
A dictionary in Python is a collection of key-value pairs, where each unique key maps to a corresponding value. 
Dictionaries are unordered, which means that the items have no index, and are instead accessed by the key. 
The keys in a dictionary must be unique and of an immutable data type (e.g. strings, numbers, or tuples), while the values can be of any data type.
Dictionaries are declared using curly braces {} and each key-value pair is separated by a colon :, like this:
"""

d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(d['key1'])

# Add an item
d['key4'] = 'value4'
print(d)

# Update an item
d['key1'] = 'new_value1'
print(d)

# Delete an item
del d['key2']
print(d)

# Print only key-value pairs
for key, value in d.items():
    print(key, value)
