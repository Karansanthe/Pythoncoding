# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to the set
my_set.add(6)
my_set.add(3)  # Adding an element that already exists in the set will have no effect

# Removing elements from the set
my_set.remove(2)
# If the element does not exist, the remove() method raises a KeyError.
# To avoid this, you can use discard(), which does not raise an error if the element is not present.
my_set.discard(7)

# Iterating through the set
for element in my_set:
    print(element)

# Output:
# 1
# 3
# 4
# 5
# 6

# Checking membership
print(3 in my_set)  # True
print(2 in my_set)  # False

# Length of the set
print(len(my_set))  # 5
