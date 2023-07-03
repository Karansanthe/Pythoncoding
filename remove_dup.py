my_list = [1, 2, 2, 3, 4, 4, 5]

# Convert list to set to remove duplicates
unique_set = set(my_list)

# Convert set back to list
unique_list = list(unique_set)

print(unique_list)

# Using not in
arr = [1, 2, 1, 3, 1]
un = []
for i in arr:
    if i not in un:
        un.append(i)
print(un)
