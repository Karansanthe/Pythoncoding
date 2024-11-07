arr = [1, 2, 3, 4]
res = 1

# Iterate directly over the elements of arr
for num in arr:
    res = res * num  # Multiply res by each element

d = [] 
# Again, iterate directly over the elements of arr
for num in arr:
    d.append(res // num)  # Divide the product by each element and append to d

print(d)
