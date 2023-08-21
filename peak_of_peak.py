def find(arr):
    n = len(arr)
    peak = 0
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > peak:
            peak = arr[i]
    return peak

arr = [10, 5, 9, 6, 7, 2, 10]
print(find(arr))