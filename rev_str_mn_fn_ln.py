full_name = "John Doe Smith"
name_parts = full_name.split()
print(name_parts[1] + " " + name_parts[0] + " " + name_parts[2])

"""
# Without split

full_name = "John Doe Smith"
first_space = full_name.find(" ")
second_space = full_name.find(" ", first_space + 1)
first_name = full_name[:first_space]
middle_name = full_name[first_space + 1:second_space]
last_name = full_name[second_space + 1:]
print(middle_name + " " + first_name + " " + last_name)
"""