arr = [1, 2, -1, -2, 3, 4, 5, 3]

dict = {}

for i in arr:
    dict[i] = dict.get(i, 0) + 1

for i, j in dict.items():
    if j > 1:
        print(i , j)

