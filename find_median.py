arr = [1, 4, 2, 3, 5]
arr.sort()
n = len(arr)

if n % 2 == 0:
    med = (arr[n // 2 - 1] + arr[n // 2])// 2
else:
    med = arr[n//2]

print(med)