arr = [1, 2, 3, 1]
left = 0
right = len(arr) - 1
while left < right:
    mid = left + (right - left) // 2
    if arr[mid] < arr[mid + 1]:
        left = mid + 1
    else:
        right = mid
print(arr[left])
