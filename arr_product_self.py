arr = [1, 2, 3, 4]
res = 1

for i in range(len(arr)):
    res = res * arr[i]

d = [] 
for i in range(len(arr)):
    d.append(res // arr[i])

print(d)