def bin_ser(arr, t):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
t = 2

find = bin_ser(arr, t)
if find != -1:
    print(find)
else:
    print("Not Found")