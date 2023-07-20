filename = "txt1.txt"

with open(filename, "r") as file:
    content = file.read()

replaced_content = content.replace("coding", "code")
count = content.count("coding")

with open(filename, "w") as file:
    file.write(replaced_content)

print("Replaced content:", replaced_content)
print("Number of occurrences of 'coding':", count)

with open(filename, "r") as file:
    line = 0
    for i in file:
        line += 1
    print("Number of line:", line)
