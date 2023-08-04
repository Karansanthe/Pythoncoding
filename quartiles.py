def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) // 2
    else:
        return arr[n // 2]

def quartiles(arr):
    q1 = find_median(arr)
    
    mid = len(arr) // 2
    q2 = find_median(arr[:mid])
    q3 = find_median(arr[mid + 1:])
    
    return q1, q2, q3

arr = [3, 7, 8, 5, 12, 14, 21, 13, 18]
arr.sort()
res = quartiles(arr)
print(res)