arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
res = 1
platform = 1
i = 1
j = 0

while (i < n and j < n):
    if arr[i] <= dep[j]:
        platform += 1
        i += 1
    elif arr[i] > dep[j]:
        platform -= 1
        j += 1
if platform > res:
    res = platform
print(res)