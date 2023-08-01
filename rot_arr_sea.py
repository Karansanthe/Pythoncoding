def search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > arr[right]:
            if target < arr[mid] and target >= arr[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > arr[mid] and target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(arr, target))