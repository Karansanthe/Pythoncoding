name = "Durgesh Pandey"
first_name, last_name = name.split()
reversed_name = last_name + " " + first_name
print(reversed_name)


"""
# Without Split

name = "Durgesh Pandey"
space_index = name.index(" ")
first_name = name[:space_index]
last_name = name[space_index+1:]
reversed_name = last_name + " " + first_name
print(reversed_name)
"""