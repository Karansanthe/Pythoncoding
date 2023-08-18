def find(arr, k):
    ans = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                ans.append((arr[i], arr[j]))
    return ans

arr = [1, 2, 3, 4, 5, 6, 7]
k = 8
print(find(arr, k))