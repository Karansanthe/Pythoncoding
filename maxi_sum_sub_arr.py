arr = [1, 2, -1, -2, 3, 4, 5]
sum = 0
maxi = float('-inf')

for i in range(len(arr)):
    if sum + arr[i] > 0:
        sum += arr[i]
    else:
        sum = 0
    if maxi < sum:
        maxi = sum
print(maxi)