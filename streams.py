from functools import reduce
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(list(map(lambda x: x * 2, arr)))
print(list(filter(lambda x: x % 2 == 0, arr)))
print(reduce(lambda x, y : x + y, arr))
