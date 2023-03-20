my_list = [1, 2, 2, 3, 4, 4, 5]

# Convert list to set to remove duplicates
unique_set = set(my_list)

# Convert set back to list
unique_list = list(unique_set)

print(unique_list)

# Alternatively, you can use a list comprehension to achieve the same result:

unique_list = [x for i, x in enumerate(my_list) if x not in my_list[:i]]

print(unique_list)
