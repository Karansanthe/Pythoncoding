arr = [3, 4, 5, 1, 2]
left, right = 0, len(arr) - 1

while left < right:
    mid = left + (right - left) // 2
    if arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid
        
print(arr[left])