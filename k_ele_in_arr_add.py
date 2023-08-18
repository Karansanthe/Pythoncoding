def find(arr, k):
    count = 0
    ans = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                count += 1
                ans.append((arr[i], arr[j]))
    return count, ans

arr = [1, 2, 4, -1, 5]
k = 3
print(find(arr, k))