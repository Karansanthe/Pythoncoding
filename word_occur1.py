input_str = "This is a string"
input_str = input_str.lower()
count = {}

for i in input_str:
    if i.isalpha():  
        count[i] = count.get(i, 0) + 1
    
for i, j in count.items():
    print(f"{i} = {j}")