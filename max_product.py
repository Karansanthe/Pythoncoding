numbers = [1, 2, 3, 4, 5, -9, -9]

max1 = float('-inf')  
max2 = float('-inf')
min1 = float('inf')
min2 = float('inf')

for num in numbers:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

if max1 * max2 > min1 * min2:
    result = max1 * max2
else:
    result = min1 * min2

print(result)
