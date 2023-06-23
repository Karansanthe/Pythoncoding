numbers = [1, 2, 3, 4, 5, -9, -9]

# Initialize the maximum and minimum numbers
max1 = float('-inf')  # Initialize first maximum as negative infinity
max2 = float('-inf')  # Initialize second maximum as negative infinity
min1 = float('inf')   # Initialize first minimum as positive infinity
min2 = float('inf')   # Initialize second minimum as positive infinity

# Find the two maximum numbers and two minimum numbers
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

# Compare the product of the two maximums and the two minimums
if max1 * max2 > min1 * min2:
    result = max1 * max2
else:
    result = min1 * min2

print(result)  # Output: 81 (9 * 9 = 81)
