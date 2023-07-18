arr = [1, 4, 2, 8 ,9, 5]
n = len(arr)
tar = 6
ans = []

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == tar:
            ans.append([arr[i], arr[j]])
for i in ans:
    print(i)