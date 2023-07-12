arr = [1, 2, 3, 1, 5, 4]
peak = arr[0]

for i in range(1, len(arr)):
    if arr[i] > peak:
        peak = arr[i]
print(peak)
