def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 3, 4, 9, 11]
target = 9
search = linear_search(arr, target)
print(search)