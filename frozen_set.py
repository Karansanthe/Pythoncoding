# Creating a frozenset
my_frozenset = frozenset([10, 20, 30, 40, 50])

# Attempting to add or remove elements from a frozenset will raise an AttributeError.
# For example:
# my_frozenset.add(60)  # This will raise an AttributeError
# my_frozenset.remove(10)  # This will raise an AttributeError

# Iterating through the frozenset
for element in my_frozenset:
    print(element)

# Output:
# 40
# 10
# 50
# 20
# 30

# Checking membership
print(30 in my_frozenset)  # True
print(60 in my_frozenset)  # False

# Length of the frozenset
print(len(my_frozenset))  # 5
