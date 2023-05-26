def selection_sort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
arr = [5, 2, 6, 4 ,1]
n = len(arr)
selection_sort(arr, n)
print(arr)