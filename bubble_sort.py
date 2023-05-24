def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

num = [5, 2, 6, 4 ,1]
n = len(num)
bubble_sort(num, n)
print(num)